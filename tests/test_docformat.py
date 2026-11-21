"""The --doc-format / --markdown extension (hand-written, shipped as codapact_jira._docformat)."""

from __future__ import annotations

import argparse
from types import SimpleNamespace

import pytest

from codapact_jira import _docformat as docformat

DOC = {"type": "doc", "version": 1, "content": [{"type": "paragraph", "content": [{"type": "text", "text": "hi", "marks": [{"type": "strong"}]}]}]}


def op(name: str) -> SimpleNamespace:
    return SimpleNamespace(name=name, params=())


def test_markdown_strings_become_adf_on_rich_text_keys() -> None:
    hook = docformat.MarkdownHook()
    sent = hook.before(op("create_issue"), {"body": {"fields": {"summary": "**not**", "description": "**hi**"}}})
    assert sent["body"]["fields"]["summary"] == "**not**"
    assert sent["body"]["fields"]["description"] == DOC


def test_adf_in_responses_becomes_markdown() -> None:
    result = docformat.MarkdownHook().after(op("get_issue"), {"fields": {"description": DOC, "comment": {"comments": [{"body": DOC}]}}})
    assert result["fields"]["description"] == "**hi**\n"
    assert result["fields"]["comment"]["comments"][0]["body"] == "**hi**\n"


@pytest.mark.parametrize(
    ("name", "path"),
    [("create_issue", ("fields", "description")), ("add_comment", ("body",)), ("add_worklog", ("comment",))],
)
def test_markdown_option_fills_the_right_field(name: str, path: tuple[str, ...]) -> None:
    sent = docformat.MarkdownHook("**hi**").before(op(name), {"body": {}})
    value = sent["body"]
    for key in path:
        value = value[key]
    assert value == DOC


def test_markdown_option_rejects_other_commands() -> None:
    with pytest.raises(ValueError, match="--markdown"):
        docformat.MarkdownHook("x").before(op("get_issue"), {})


def test_doc_format_adf_turns_conversion_off(monkeypatch: pytest.MonkeyPatch) -> None:
    extension = docformat.extension(SimpleNamespace(env_prefix="JIRA"))
    assert extension.hooks(argparse.Namespace(doc_format="adf")) == []
    monkeypatch.setenv("JIRA_DOC_FORMAT", "adf")
    assert extension.hooks(argparse.Namespace()) == []
    with pytest.raises(ValueError, match="needs --doc-format markdown"):
        extension.hooks(argparse.Namespace(markdown="x"))
    monkeypatch.delenv("JIRA_DOC_FORMAT")
    assert len(extension.hooks(argparse.Namespace())) == 1


def test_plain_string_descriptions_elsewhere_are_untouched() -> None:
    arguments = {"body": {"description": "**plain**", "name": "scheme"}}
    assert docformat.MarkdownHook().before(op("update_notification_scheme"), arguments) == arguments
