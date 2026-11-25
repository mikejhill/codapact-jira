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

    def as_dict(self) -> dict[str, Any]:
        return dict(vars(self))


def patched(scenario: Scenario, code_key: str | None) -> Callable[..., str]:
    """``sign_in_headless`` that also notes page errors and, with a key, enters the code."""
    original = runtime.sign_in_headless

    def run(
        page: Any, login: BrowserLogin, filled: set[str], error: type[Exception]
    ) -> str:
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
) -> list[Any]:
    original = runtime.sign_in_headless
    runtime.sign_in_headless = patched(scenario, code_key)
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
        if args.manual:
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
    report = [s.as_dict() for s in results]
    text = json.dumps(report, indent=2).replace(password, "<password>")
    (ROOT / f"report-{stamp}.json").write_text(text, encoding="utf-8")
    lines = [f"# Live sign-in check {stamp}", ""]
    for item in results:
        mark = "PASS" if item.ok else "FAIL"
        lines.append(f"## {mark}: {item.name} ({item.result}, {item.seconds} s)")
        lines += [f"- {step}" for step in item.steps]
        lines += [f"- page said: {e}" for e in item.page_errors]
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
