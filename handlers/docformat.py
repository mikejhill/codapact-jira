"""Markdown in, Markdown out: Jira rich-text fields as Markdown instead of ADF JSON.

Jira stores descriptions, comments and other rich text as Atlassian Document Format
(ADF). With ``--doc-format markdown`` (the default; ``JIRA_DOC_FORMAT`` sets it too):

* a string given for ``description``, ``environment``, a comment ``body`` or a worklog
  ``comment`` is converted from Markdown to ADF before it is sent;
* every ADF document in a response is converted to Markdown.

``--doc-format adf`` sends and returns ADF unchanged. Conversion uses adflux with its Jira
profile (Jira emoji, panels as ``> [!NOTE]`` alerts, ``:status[...]``...); run
``uvx adflux syntax`` for the dialect.
"""

from __future__ import annotations

import argparse
import os
from typing import Any

from adflux import to_adf, to_markdown

PROFILE = "jira"
FIELDS = frozenset({"description", "environment", "body", "comment"})
CHOICES = ("markdown", "adf")


def is_adf(value: Any) -> bool:
    """Whether ``value`` is an ADF document."""
    return (
        isinstance(value, dict)
        and value.get("type") == "doc"
        and isinstance(value.get("content"), list)
        and "version" in value
    )


def to_wire(value: Any, key: str | None = None) -> Any:
    """Convert Markdown strings under rich-text keys to ADF, recursively."""
    if isinstance(value, dict):
        return {k: to_wire(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return [to_wire(v, key) for v in value]
    if isinstance(value, str) and key in FIELDS:
        return to_adf(value, PROFILE)
    return value


def from_wire(value: Any) -> Any:
    """Convert every ADF document in ``value`` to Markdown, recursively."""
    if is_adf(value):
        return to_markdown(value, PROFILE)
    if isinstance(value, dict):
        return {k: from_wire(v) for k, v in value.items()}
    if isinstance(value, list):
        return [from_wire(v) for v in value]
    return value


# Operations whose request bodies carry ADF. Elsewhere ``description`` and friends are
# plain strings (project, field and scheme descriptions), so they are left alone.
SLOTS: dict[str, tuple[str, ...]] = {
    "create_issue": ("fields", "description"),
    "edit_issue": ("fields", "description"),
    "add_comment": ("body",),
    "update_comment": ("body",),
    "add_worklog": ("comment",),
    "update_worklog": ("comment",),
}
RICH_TEXT_OPERATIONS = frozenset({*SLOTS, "create_issues", "do_transition", "link_issues"})


def _slot(operation: Any) -> tuple[str, ...]:
    """Where ``--markdown`` goes in this operation's request body."""
    try:
        return SLOTS[str(getattr(operation, "name", ""))]
    except KeyError:
        raise ValueError("--markdown is for creating or editing issues, comments and worklogs") from None


class MarkdownHook:
    """Call hook that converts rich text between Markdown and ADF."""

    def __init__(self, markdown: str | None = None) -> None:
        self.markdown = markdown

    def before(self, operation: Any, arguments: dict[str, Any]) -> dict[str, Any]:
        if self.markdown is not None:
            request = dict(arguments.get("body") or {})
            path = _slot(operation)
            target = request
            for key in path[:-1]:
                target[key] = dict(target.get(key) or {})
                target = target[key]
            target[path[-1]] = self.markdown
            arguments = {**arguments, "body": request}
        if str(getattr(operation, "name", "")) not in RICH_TEXT_OPERATIONS:
            return arguments
        return {k: to_wire(v) if isinstance(v, dict | list) else v for k, v in arguments.items()}

    def after(self, operation: Any, result: Any) -> Any:
        del operation
        return from_wire(result)


class Extension:
    """``cli.extensions`` entry: the ``--doc-format`` option."""

    def __init__(self, runtime: Any) -> None:
        self.prefix = getattr(runtime, "env_prefix", "JIRA")

    def add_options(self, group: argparse._ArgumentGroup, hidden: bool) -> None:
        group.add_argument(
            "--doc-format",
            choices=CHOICES,
            default=argparse.SUPPRESS,
            help=argparse.SUPPRESS
            if hidden
            else f"rich text as markdown (default) or raw adf JSON (env {self.prefix}_DOC_FORMAT)",
        )
        group.add_argument(
            "--markdown",
            metavar="TEXT|@FILE|@-",
            default=argparse.SUPPRESS,
            help=argparse.SUPPRESS
            if hidden
            else "issue description, comment or worklog text as Markdown (text, @file, @- for stdin)",
        )

    def format(self, args: argparse.Namespace) -> str:
        chosen = getattr(args, "doc_format", None) or os.environ.get(f"{self.prefix}_DOC_FORMAT") or "markdown"
        if chosen not in CHOICES:
            raise ValueError(f"{self.prefix}_DOC_FORMAT must be markdown or adf")
        return chosen

    def hooks(self, args: argparse.Namespace) -> list[Any]:
        markdown = _read(getattr(args, "markdown", None))
        if self.format(args) != "markdown":
            if markdown is not None:
                raise ValueError("--markdown needs --doc-format markdown")
            return []
        return [MarkdownHook(markdown)]

    def notes(self) -> list[str]:
        return [
            "Rich text (description, environment, comment body, worklog comment) is Markdown "
            "in and out; --markdown TEXT|@file|@- sets an issue description, comment or worklog; "
            "--doc-format adf sends and returns ADF JSON. Dialect: uvx adflux syntax.",
        ]


def _read(value: str | None) -> str | None:
    if value is None:
        return None
    if value == "@-":
        import sys

        return sys.stdin.read()
    if value.startswith("@"):
        from pathlib import Path

        return Path(value[1:]).read_text(encoding="utf-8")
    return value


def extension(runtime: Any) -> Extension:
    """Factory named in ``cli.extensions``."""
    return Extension(runtime)
