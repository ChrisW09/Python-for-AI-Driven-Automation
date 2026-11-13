"""Request-shape tests for ``GoogleLLM`` (google-genai SDK) — offline, against a fake SDK.

Run from the repo root:  python -m pytest tests/
"""
import sys
import types
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # repo-root llm_providers.py

from llm_providers import GoogleLLM  # noqa: E402

MESSAGES = [
    {"role": "system", "content": "Be brief."},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello!"},
    {"role": "user", "content": "Bye"},
]


@pytest.fixture
def fake_genai(monkeypatch):
    calls, clients = [], []

    class FakeModels:
        def generate_content(self, *, model, contents, config=None):
            calls.append({"model": model, "contents": contents, "config": config})
            usage = SimpleNamespace(prompt_token_count=5, candidates_token_count=1,
                                    thoughts_token_count=3)
            return SimpleNamespace(text="ok", usage_metadata=usage,
                                   model_version="gemini-2.5-flash-001")

    class FakeClient:
        def __init__(self, api_key=None):
            clients.append(api_key)
            self.models = FakeModels()

    genai = types.ModuleType("google.genai")
    genai.Client = FakeClient
    google = types.ModuleType("google")
    google.genai = genai
    monkeypatch.setitem(sys.modules, "google", google)
    monkeypatch.setitem(sys.modules, "google.genai", genai)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    return SimpleNamespace(calls=calls, clients=clients, monkeypatch=monkeypatch)


def test_messages_map_to_gemini_contents_and_config(fake_genai):
    r = GoogleLLM(api_key="k").chat(MESSAGES, max_tokens=64, top_p=0.9)
    sent = fake_genai.calls[-1]
    assert sent["model"] == "gemini-2.5-flash"
    assert sent["contents"] == [
        {"role": "user", "parts": [{"text": "Hi"}]},
        {"role": "model", "parts": [{"text": "Hello!"}]},
        {"role": "user", "parts": [{"text": "Bye"}]},
    ]
    assert sent["config"] == {"system_instruction": "Be brief.", "temperature": 0.0,
                              "max_output_tokens": 64, "top_p": 0.9}
    assert r["text"] == "ok" and r["model"] == "gemini-2.5-flash-001"
    assert (r["tokens_in"], r["tokens_out"]) == (5, 4)  # output = answer + thinking tokens
    assert set(r) == {"text", "model", "tokens_in", "tokens_out", "latency_s"}


def test_none_and_missing_system_are_omitted(fake_genai):
    GoogleLLM(api_key="k").chat([{"role": "user", "content": "x"}],
                                temperature=None, max_tokens=None)
    assert fake_genai.calls[-1]["config"] == {}


def test_api_key_falls_back_to_env(fake_genai):
    fake_genai.monkeypatch.setenv("GEMINI_API_KEY", "from-env")
    GoogleLLM()
    assert fake_genai.clients[-1] == "from-env"


def test_missing_key_is_a_clear_error(fake_genai):
    with pytest.raises(RuntimeError, match="GOOGLE_API_KEY"):
        GoogleLLM()


def test_installed_sdk_has_the_fields_the_wrapper_uses():
    gtypes = pytest.importorskip("google.genai.types")
    cfg = gtypes.GenerateContentConfig.model_fields
    assert {"system_instruction", "temperature", "max_output_tokens"} <= set(cfg)
    resp = gtypes.GenerateContentResponse.model_fields
    assert {"usage_metadata", "model_version"} <= set(resp)
    usage = gtypes.GenerateContentResponseUsageMetadata.model_fields
    assert {"prompt_token_count", "candidates_token_count", "thoughts_token_count"} <= set(usage)
