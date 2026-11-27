"""Live browser sign-in check against a real Jira Cloud site (run by hand, never in CI).

The person who owns the account runs this; it signs in with credentials they saved in
their OS keyring and writes a report (no secrets) for whoever fixes what failed.

Setup, once (Windows, macOS or Linux):

    python -m keyring set codapact-live:atlassian site       # https://<team>.atlassian.net
    python -m keyring set codapact-live:atlassian email
    python -m keyring set codapact-live:atlassian password
    python -m keyring set codapact-live:atlassian totp       # base32 secret or otpauth:// URI

Run from the repository root (its .venv has codapact[browser] and Chromium):

    .venv\\Scripts\\python.exe scripts\\live_auth_check.py [--window]
    .venv\\Scripts\\python.exe scripts\\live_auth_check.py --compare

``--compare`` runs two windows with a network log: first you type the password and code
yourself, then codapact types them. The log keeps request and field names, value lengths,
statuses and error messages, never values (the email and password show as <email> and
<password>), so the two sign-ins can be compared.

Each scenario uses its own browser profile under .live/ (deleted afterwards) and records
the steps codapact traced, the visible error text on the last page, and the outcome. The
report goes to .live/report-<time>.json and .live/report-<time>.md.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import shutil
import struct
import sys
import time
import traceback
import urllib.parse
from collections.abc import Callable
from dataclasses import replace
from pathlib import Path
from typing import Any

import keyring
from codapact.runtime import browser as runtime
from codapact.runtime.browser import BrowserLogin, playwright_capture

SERVICE = "codapact-live:atlassian"
ROOT = Path(__file__).resolve().parent.parent / ".live"
# the coda's own settings (codapact.yaml, cli.auth.session.browser)
SETTINGS = {
    "browser": {
        "login_url": "{base_url}/jira",
        "cookies": ["tenant.session.token"],
        "headers": {"X-Atlassian-Token": "no-check"},
        "signin_hosts": ["id.atlassian.com", "*.okta.com"],
    }
}
ERROR_TEXT = """() => Array.from(document.querySelectorAll(
  '[role=alert], [aria-live], .error, [data-testid*=error], [id*=error]'))
  .map((el) => el.innerText.trim()).filter(Boolean).slice(0, 5)"""


def secret(name: str) -> str:
    value = keyring.get_password(SERVICE, name)
    if not value:
        sys.exit(f"missing: python -m keyring set {SERVICE} {name}")
    return value


def totp(key: str) -> str:
    if key.startswith("otpauth://"):
        key = urllib.parse.parse_qs(urllib.parse.urlsplit(key).query)["secret"][0]
    raw = base64.b32decode(key.upper() + "=" * (-len(key) % 8))
    digest = hmac.new(
        raw, struct.pack(">Q", int(time.time() // 30)), hashlib.sha1
    ).digest()
    offset = digest[-1] & 15
    code = (
        struct.unpack(">I", digest[offset : offset + 4])[0] & 0x7FFFFFFF
    ) % 1_000_000
    return f"{code:06d}"


class Scenario:
    """One run of ``playwright_capture`` with what it traced and what the page said."""

    def __init__(self, name: str, expect: str) -> None:
        self.name = name
        self.expect = expect
        self.steps: list[str] = []
        self.page_errors: list[str] = []
        self.codes_sent = 0
        self.result = ""
        self.ok = False
        self.seconds = 0.0
        self.network: list[str] = []
        self.pending: list[Any] = []  # responses whose bodies are read between polls
        self.watched: set[int] = set()

    def as_dict(self) -> dict[str, Any]:
        return dict(vars(self))


# headers whose values are kept; any other value shows only its length
OPEN_HEADERS = {
    "content-type",
    "origin",
    "referer",
    "user-agent",
    "accept",
    "accept-language",
    "sec-ch-ua",
    "sec-ch-ua-mobile",
    "sec-ch-ua-platform",
    "sec-fetch-site",
    "sec-fetch-mode",
    "sec-fetch-dest",
    "x-requested-with",
}
# response fields whose text is kept (error messages)
OPEN_FIELDS = {"error", "message", "code", "errorCode", "status", "type", "reason"}
STATIC = {"image", "stylesheet", "font", "media"}


class Redact:
    """Turn values into their shape: names, types and lengths, never the value."""

    def __init__(self, email: str, password: str) -> None:
        self.email, self.password = email, password

    def value(self, value: Any, key: str = "", keep: bool = False) -> Any:
        if isinstance(value, dict):
            return {k: self.value(v, k, keep) for k, v in value.items()}
        if isinstance(value, list):
            return [self.value(v, key, keep) for v in value[:5]]
        if isinstance(value, str):
            if self.password and self.password in value:
                return "<password>"
            if value == self.email:
                return "<email>"
            if keep and key in OPEN_FIELDS and len(value) < 300:
                return value
            return f"<str {len(value)}>"
        return value  # numbers, booleans, null

    def body(self, text: str | None, content_type: str, keep: bool = False) -> str:
        if not text:
            return ""
        if "json" in content_type or text[:1] in "{[":
            try:
                return json.dumps(self.value(json.loads(text), keep=keep))
            except ValueError:
                pass
        if "x-www-form-urlencoded" in content_type or (
            "=" in text and " " not in text[:200]
        ):
            form = urllib.parse.parse_qsl(text, keep_blank_values=True)
            return json.dumps({k: self.value(v, k, keep) for k, v in form})
        if self.password and self.password in text:
            return "<text with the password>"
        return f"<text {len(text)}>"

    def headers(self, headers: dict[str, str]) -> str:
        shown = {
            k: (v if k.lower() in OPEN_HEADERS else f"<{len(v)}>")
            for k, v in sorted(headers.items())
        }
        return json.dumps(shown)


def watch(scenario: Scenario, page: Any, redact: Redact) -> None:
    """Log the context's requests (redacted) from the first poll on."""
    context = page.context
    if id(context) in scenario.watched:
        return
    scenario.watched.add(id(context))
    started = time.monotonic()

    def stamp() -> str:
        return f"{time.monotonic() - started:6.1f}s"

    def on_request(request: Any) -> None:
        if request.resource_type in STATIC:
            return
        line = f"{stamp()} > {request.method} {request.url.split('?')[0]}"
        line += f" [{request.resource_type}]"
        if request.method not in ("GET", "HEAD", "OPTIONS"):
            content_type = request.headers.get("content-type", "")
            try:
                line += f"\n      body {redact.body(request.post_data, content_type)}"
            except Exception as error:  # noqa: BLE001 - a log line, never fatal
                line += f"\n      body <unreadable: {error}>"
            line += f"\n      headers {redact.headers(request.headers)}"
        scenario.network.append(line)

    def on_response(response: Any) -> None:
        request = response.request
        if request.resource_type in STATIC:
            return
        line = f"{stamp()} < {response.status} {request.method} {response.url.split('?')[0]}"
        scenario.network.append(line)
        if request.method not in ("GET", "HEAD", "OPTIONS"):
            scenario.pending.append((len(scenario.network) - 1, response))

    context.on("request", on_request)
    context.on("response", on_response)
    scenario.steps.append(
        "(check script) user agent: " + str(page.evaluate("() => navigator.userAgent"))
    )


def read_bodies(scenario: Scenario, redact: Redact) -> None:
    """Add the redacted bodies of non-GET responses (read outside the event handlers)."""
    pending, scenario.pending = scenario.pending, []
    for index, response in pending:
        try:
            content_type = response.headers.get("content-type", "")
            text = response.text()
            scenario.network[index] += (
                f"\n      response {redact.body(text, content_type, keep=True)}"
            )
        except Exception:  # noqa: BLE001 - gone with a navigation
            scenario.network[index] += "\n      response <gone>"


def patched(
    scenario: Scenario, code_key: str | None, redact: Redact | None = None
) -> Callable[..., str]:
    """``sign_in_headless`` that also notes page errors and, with a key, enters the code."""
    original = runtime.sign_in_headless

    def run(
        page: Any, login: BrowserLogin, filled: set[str], error: type[Exception]
    ) -> str:
        if redact:
            try:
                watch(scenario, page, redact)
            except error:
                pass  # the next poll attaches it
            read_bodies(scenario, redact)
        outcome = original(page, login, filled, error)
        if not any(
            step.startswith("(check script) webdriver") for step in scenario.steps
        ):
            try:  # whether the page can see an automated browser
                flag = page.evaluate("() => navigator.webdriver")
                scenario.steps.append(f"(check script) webdriver flag: {flag}")
            except error:
                pass  # the page moved on while it was read; the next poll reads it
        try:
            for text in page.evaluate(ERROR_TEXT):
                if text not in scenario.page_errors:
                    scenario.page_errors.append(text)
        except error:
            pass  # the page moved on while it was read; the next poll reads the new one
        if outcome == "challenge" and code_key and scenario.codes_sent < 2:
            box = page.locator(
                "input[autocomplete='one-time-code'], input[name*=otp i]"
            ).first
            box.fill(totp(code_key))
            box.press("Enter")
            scenario.codes_sent += 1
            scenario.steps.append("(check script) entered the TOTP code")
        return outcome

    return run


def clear_site_cookies(profile: Path, names: tuple[str, ...]) -> None:
    """Expire the site session only; the identity provider's session stays."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        context = playwright.chromium.launch_persistent_context(
            str(profile), headless=True
        )
        for name in names:
            context.clear_cookies(name=name)
        context.close()


def run(
    scenario: Scenario,
    login: BrowserLogin,
    profile: Path,
    *,
    headless: bool = True,
    code_key: str | None = None,
    timeout: float = 60.0,
    redact: Redact | None = None,
) -> list[Any]:
    original = runtime.sign_in_headless
    runtime.sign_in_headless = patched(scenario, code_key, redact)
    started = time.monotonic()
    cookies: list[Any] = []
    try:
        cookies = playwright_capture(
            replace(login, trace=scenario.steps.append),
            profile,
            headless,
            timeout,
            None,
        )
        scenario.result = "signed in" if cookies else "no session"
    except Exception as error:  # noqa: BLE001 - the report records any failure
        scenario.result = f"error: {error}"
        scenario.steps.append(traceback.format_exc(limit=3))
    finally:
        runtime.sign_in_headless = original
        scenario.seconds = round(time.monotonic() - started, 1)
        if redact:
            read_bodies(scenario, redact)
    scenario.ok = scenario.result == scenario.expect
    return cookies


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--window", action="store_true", help="also run the window scenarios"
    )
    parser.add_argument(
        "--manual",
        action="store_true",
        help="only a window where you type the password and code yourself",
    )
    parser.add_argument(
        "--compare",
        action="store_true",
        help="two windows with a network log: you sign in, then codapact does",
    )
    args = parser.parse_args()
    site = secret("site").rstrip("/")
    email, password, code_key = secret("email"), secret("password"), secret("totp")
    base = BrowserLogin.from_settings(SETTINGS, site)
    assert base is not None
    login = replace(base, username=email, password=password)
    ROOT.mkdir(exist_ok=True)
    original = runtime.sign_in_headless
    results: list[Scenario] = []

    def profile(name: str) -> Path:
        path = ROOT / f"profile-{name}"
        shutil.rmtree(path, ignore_errors=True)
        return path

    try:
        if args.compare:
            redact = Redact(email, password)
            yours = Scenario(
                "compare 1: codapact types the email, you type password and code",
                "signed in",
            )
            run(
                yours,
                replace(login, password=""),
                profile("compare-yours"),
                headless=False,
                timeout=180.0,
                redact=redact,
            )
            results.append(yours)
            ours = Scenario(
                "compare 2: codapact types email, password and code", "signed in"
            )
            run(
                ours,
                login,
                profile("compare-ours"),
                headless=False,
                code_key=code_key,
                redact=redact,
            )
            results.append(ours)
        elif args.manual:
            # tells Atlassian refusing automation apart from refusing codapact's typing
            manual = Scenario(
                "window: codapact types the email only, you type password and code",
                "signed in",
            )
            run(
                manual,
                replace(login, password=""),
                profile("manual"),
                headless=False,
                timeout=180.0,
            )
            results.append(manual)
        else:
            main_profile = profile("main")
            first = Scenario("new device: email, password, 2FA (headless)", "signed in")
            run(first, login, main_profile, code_key=code_key)
            results.append(first)
            again = Scenario("still signed in: no typing", "signed in")
            run(again, login, main_profile)
            results.append(again)
            clear_site_cookies(main_profile, login.cookies)
            sso = Scenario(
                "site cookie expired: renew from the identity session", "signed in"
            )
            run(sso, login, main_profile)
            results.append(sso)
            no_code = Scenario("new device without a code: stops at 2FA", "no session")
            run(no_code, login, profile("no-code"), timeout=30.0)
            results.append(no_code)
            wrong = Scenario("wrong password: sent once, stops", "no session")
            run(
                wrong,
                replace(login, password=password + "-wrong"),
                profile("wrong"),
                timeout=30.0,
            )
            results.append(wrong)
            if args.window:
                window = Scenario(
                    "window: email and password typed, code entered", "signed in"
                )
                run(window, login, profile("window"), headless=False, code_key=code_key)
                results.append(window)
    finally:
        runtime.sign_in_headless = original
        for path in ROOT.glob("profile-*"):
            shutil.rmtree(path, ignore_errors=True)

    stamp = time.strftime("%Y%m%d-%H%M%S")
    report = [
        {k: v for k, v in s.as_dict().items() if k not in ("pending", "watched")}
        for s in results
    ]
    text = json.dumps(report, indent=2).replace(password, "<password>")
    (ROOT / f"report-{stamp}.json").write_text(text, encoding="utf-8")
    lines = [f"# Live sign-in check {stamp}", ""]
    for item in results:
        mark = "PASS" if item.ok else "FAIL"
        lines.append(f"## {mark}: {item.name} ({item.result}, {item.seconds} s)")
        lines += [f"- {step}" for step in item.steps]
        lines += [f"- page said: {e}" for e in item.page_errors]
        if item.network:
            lines += ["", "```", *item.network, "```"]
        lines.append("")
    (ROOT / f"report-{stamp}.md").write_text(
        "\n".join(lines).replace(password, "<password>"), encoding="utf-8"
    )
    print(
        "\n".join(
            f"{'PASS' if s.ok else 'FAIL'}  {s.name}: {s.result}" for s in results
        )
    )
    print(f"report: {ROOT / f'report-{stamp}.md'}")
    return 0 if all(s.ok for s in results) else 1


if __name__ == "__main__":
    sys.exit(main())
