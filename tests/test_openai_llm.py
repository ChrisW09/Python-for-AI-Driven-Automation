"""Request-shape tests for ``OpenAILLM`` — offline, against a fake ``openai`` module.

Run from the repo root:  python -m pytest tests/
"""
import inspect
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # repo-root llm_providers.py

from llm_providers import OpenAILLM  # noqa: E402

MESSAGES = [{"role": "system", "content": "Be brief."},
            {"role": "user", "content": "Hi"}]


class _FakeCompletions:
    def __init__(self):
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            model=kwargs["model"] + "-2026-01-01",
            choices=[SimpleNamespace(message=SimpleNamespace(content="hello"))],
            usage=SimpleNamespace(prompt_tokens=7, completion_tokens=2),
        )


@pytest.fixture
def fake_openai(monkeypatch):
    completions = _FakeCompletions()

    class FakeOpenAI:
        def __init__(self, api_key=None):
            self.chat = SimpleNamespace(completions=completions)

    monkeypatch.setitem(sys.modules, "openai", SimpleNamespace(OpenAI=FakeOpenAI))
    return completions


def test_sends_max_completion_tokens_not_deprecated_max_tokens(fake_openai):
    OpenAILLM().chat(MESSAGES, max_tokens=64)
    sent = fake_openai.calls[-1]
    assert sent["max_completion_tokens"] == 64
    assert "max_tokens" not in sent  # rejected by o-series / GPT-5 reasoning models


def test_defaults_keep_the_shared_contract(fake_openai):
    r = OpenAILLM(model="gpt-5.4-mini").chat(MESSAGES)
    sent = fake_openai.calls[-1]
    assert sent["model"] == "gpt-5.4-mini" and sent["messages"] == MESSAGES
    assert sent["temperature"] == 0.0 and sent["max_completion_tokens"] == 512
    assert r["text"] == "hello" and r["model"] == "gpt-5.4-mini-2026-01-01"
    assert (r["tokens_in"], r["tokens_out"]) == (7, 2)
    assert set(r) == {"text", "model", "tokens_in", "tokens_out", "latency_s"}


def test_none_omits_temperature_and_limit(fake_openai):
    OpenAILLM().chat(MESSAGES, temperature=None, max_tokens=None)
    sent = fake_openai.calls[-1]
    assert "temperature" not in sent and "max_completion_tokens" not in sent


def test_provider_kwargs_pass_through_and_win(fake_openai):
    OpenAILLM().chat(MESSAGES, reasoning_effort="low", max_completion_tokens=99)
    sent = fake_openai.calls[-1]
    assert sent["reasoning_effort"] == "low" and sent["max_completion_tokens"] == 99


def test_installed_sdk_accepts_max_completion_tokens():
    openai = pytest.importorskip("openai")
    from openai.resources.chat.completions import Completions

    params = inspect.signature(Completions.create).parameters
    assert "max_completion_tokens" in params, (
        f"openai {openai.__version__} is too old; the shim needs openai>=1.45")
