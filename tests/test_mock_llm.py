"""Interface tests for the offline ``MockLLM`` and the ``get_llm`` factory.

Run from the repo root:  python -m pytest tests/
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # repo-root llm_providers.py

from llm_providers import MockLLM, get_llm  # noqa: E402

MESSAGES = [
    {"role": "system", "content": "Classify the sentiment of the message."},
    {"role": "user", "content": "I love the new dashboard"},
]


def test_default_model_name_is_unchanged():
    r = MockLLM().chat(MESSAGES)
    assert r["model"] == "mock-mini"
    assert r["text"] == "positive"


def test_model_is_a_constructor_argument_like_every_real_provider():
    llm = MockLLM(model="mock-large")
    assert llm.model == "mock-large"
    assert llm.chat(MESSAGES)["model"] == "mock-large"


def test_get_llm_passes_model_through_for_mock():
    # Used to raise TypeError: MockLLM.__init__() got an unexpected keyword argument 'model'
    llm = get_llm("mock", model="mock-large")
    assert isinstance(llm, MockLLM)
    assert llm.chat(MESSAGES)["model"] == "mock-large"


def test_seed_stays_the_first_positional_argument():
    assert MockLLM(42).model == "mock-mini"
    assert MockLLM(seed=42, model="x").model == "x"


def test_per_call_model_override_still_works():
    assert MockLLM(model="a").chat(MESSAGES, model="b")["model"] == "b"


def test_response_has_the_shared_provider_keys():
    r = MockLLM().chat(MESSAGES, temperature=0.7, max_tokens=5, top_p=0.9)
    assert set(r) == {"text", "model", "tokens_in", "tokens_out", "latency_s"}


def test_unknown_provider_is_rejected():
    with pytest.raises(ValueError, match="unknown provider"):
        get_llm("nope")
