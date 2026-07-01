"""Unified LLM-provider toolkit.

This single module gives every AI notebook in the course a way to swap between
four hosted providers and one local option *without changing application code*.

Every provider implements the same minimal interface:

    response = client.chat(messages=[...], temperature=0.0, max_tokens=512)
    response["text"]       # the assistant's reply, as a string
    response["model"]      # the actual model name returned by the provider
    response["tokens_in"]  # input tokens billed (or estimated)
    response["tokens_out"] # output tokens billed (or estimated)
    response["latency_s"]  # wall-clock time in seconds

Pick the provider that fits your situation:

    MockLLM       — fully offline. Default for the course's notebooks. No internet, no keys.
    OpenAILLM     — gpt-5.4-mini (default) / gpt-5.5. Set OPENAI_API_KEY.
    AnthropicLLM  — claude-haiku-4-5 (default) / claude-sonnet-5 / claude-opus-4-8. Set ANTHROPIC_API_KEY.
    GoogleLLM     — gemini-2.5-flash (default) / gemini-2.5-pro. Set GOOGLE_API_KEY (or GEMINI_API_KEY).
    OllamaLLM     — any model you've `ollama pull`ed locally. No key needed.

Usage in any notebook:

    from llm_providers import MockLLM, OpenAILLM, AnthropicLLM, GoogleLLM, OllamaLLM

    # Choose ONE — same interface across all five
    llm = MockLLM()                                    # default for the course
    # llm = OpenAILLM(model="gpt-5.4-mini")
    # llm = AnthropicLLM(model="claude-haiku-4-5")
    # llm = GoogleLLM(model="gemini-2.5-flash")
    # llm = OllamaLLM(model="llama3.2:3b")

    r = llm.chat(messages=[
        {"role": "system", "content": "You are a classifier..."},
        {"role": "user",   "content": "Refund please."},
    ])
    print(r["text"], r["tokens_in"], r["tokens_out"])

The provider classes lazy-import their SDKs, so you only need to pip-install the
ones you actually use:

    pip install openai            # for OpenAILLM
    pip install anthropic         # for AnthropicLLM
    pip install google-generativeai   # for GoogleLLM
    pip install ollama            # for OllamaLLM   (plus a local Ollama server)
"""
from __future__ import annotations

import os
import re
import json
import time
import hashlib
import random
from typing import Any
from textwrap import shorten


# =========================================================================
#  Provider interface (informal — just a docstring)
# =========================================================================
#
# Every concrete provider must expose a single method:
#
#     chat(self, messages: list[dict], *,
#          temperature: float = 0.0,
#          max_tokens: int | None = 512,
#          **provider_kwargs) -> dict
#
# returning a dict with at minimum the keys:
#   text, model, tokens_in, tokens_out, latency_s
# =========================================================================


# =========================================================================
#  MockLLM — the offline default the course's notebooks use
# =========================================================================
class MockLLM:
    """A deterministic, offline LLM impostor.

    It's not intelligent; it follows hard-coded keyword rules so the course's
    notebooks run without internet or API keys. Plug in any real provider to
    get real intelligence — the calling code does not change.
    """

    POSITIVE = {"love", "great", "amazing", "excellent", "happy", "fantastic",
                "perfect", "delight", "smooth", "fast", "thank", "good"}
    NEGATIVE = {"hate", "terrible", "awful", "bad", "slow", "broken", "bug",
                "crash", "angry", "frustrating", "refund", "cancel", "worst"}
    BILLING  = {"refund", "invoice", "charge", "bill", "subscription", "renew", "payment", "price"}
    TECH     = {"error", "crash", "bug", "broken", "login", "password", "loading", "freeze", "stuck"}
    FEATURE  = {"feature", "request", "missing", "wish", "could you", "add", "support for"}

    def __init__(self, seed: int = 0):
        self._rng = random.Random(seed)

    @staticmethod
    def _count_tokens(s: str) -> int:
        return max(1, len(re.findall(r"\w+|\S", s or "")))

    @staticmethod
    def _kw_score(text: str, vocab: set) -> int:
        return sum(1 for w in re.findall(r"[a-zA-Z']+", text.lower()) if w in vocab)

    def _classify_sentiment(self, text: str) -> str:
        pos, neg = self._kw_score(text, self.POSITIVE), self._kw_score(text, self.NEGATIVE)
        return "positive" if pos > neg else "negative" if neg > pos else "neutral"

    def _classify_topic(self, text: str) -> str:
        scores = {"billing": self._kw_score(text, self.BILLING),
                  "tech":    self._kw_score(text, self.TECH),
                  "feature": self._kw_score(text, self.FEATURE)}
        best = max(scores, key=scores.get)
        return best if scores[best] > 0 else "other"

    def _summarise(self, text: str, max_chars: int = 120) -> str:
        """Naive summary: first sentence, shortened."""
        first_sentence = re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=1)[0]
        return shorten(first_sentence, width=max_chars, placeholder="…")

    def chat(self, messages, *, model: str = "mock-mini",
             temperature: float = 0.0, max_tokens: int = 512, **_):
        t0 = time.perf_counter()
        sys_msg  = next((m["content"] for m in messages if m["role"] == "system"), "").lower()
        user_msgs = [m["content"] for m in messages if m["role"] == "user"]
        user_msg  = user_msgs[-1] if user_msgs else ""

        if "json" in sys_msg and ("sentiment" in sys_msg or "topic" in sys_msg):
            out = json.dumps({"sentiment": self._classify_sentiment(user_msg),
                              "topic":     self._classify_topic(user_msg)})
        elif "json" in sys_msg and "extract" in sys_msg:
            amount = re.search(r"(\$|€|£)\s*\d[\d,]*(\.\d+)?", user_msg)
            order  = re.search(r"[Oo]rder\s*#?\s*(\w+)", user_msg)
            out = json.dumps({
                "amount":   amount.group(0) if amount else None,
                "order_id": order.group(1) if order else None,
            })
        elif "classify" in sys_msg and "sentiment" in sys_msg:
            out = self._classify_sentiment(user_msg)
        elif "classify" in sys_msg and "topic" in sys_msg:
            out = self._classify_topic(user_msg)
        elif "summarise" in sys_msg or "summary" in sys_msg:
            out = self._summarise(user_msg)
        elif "answer" in sys_msg or "qa" in sys_msg:
            out = ("Based on the provided context, here is a short answer. "
                   f"You asked: {self._summarise(user_msg, 80)}")
        else:
            out = "This is a mock response. Plug a real LLM in to get a real answer."

        tokens_in  = sum(self._count_tokens(m["content"]) for m in messages)
        tokens_out = self._count_tokens(out)
        return {"text": out, "model": model,
                "tokens_in": tokens_in, "tokens_out": tokens_out,
                "latency_s": time.perf_counter() - t0}


# =========================================================================
#  OpenAI
# =========================================================================
class OpenAILLM:
    """Wrapper around `openai.OpenAI`.

    pip install openai
    export OPENAI_API_KEY=sk-...
    """

    def __init__(self, model: str = "gpt-5.4-mini", api_key: str | None = None):
        try:
            from openai import OpenAI
        except ImportError as e:
            raise ImportError(
                "OpenAI provider requires `pip install openai`."
            ) from e
        self._client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model

    def chat(self, messages, *, temperature=0.0, max_tokens=512, **kwargs):
        t0 = time.perf_counter()
        resp = self._client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs,
        )
        return {
            "text":       resp.choices[0].message.content or "",
            "model":      resp.model,
            "tokens_in":  resp.usage.prompt_tokens,
            "tokens_out": resp.usage.completion_tokens,
            "latency_s":  time.perf_counter() - t0,
        }


# =========================================================================
#  Anthropic (Claude)
# =========================================================================
class AnthropicLLM:
    """Wrapper around `anthropic.Anthropic`.

    pip install anthropic
    export ANTHROPIC_API_KEY=sk-ant-...

    Note: Anthropic puts the system message in a separate `system=` parameter.
    """

    def __init__(self, model: str = "claude-haiku-4-5", api_key: str | None = None):
        try:
            import anthropic
        except ImportError as e:
            raise ImportError(
                "Anthropic provider requires `pip install anthropic`."
            ) from e
        self._client = anthropic.Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.model = model

    def chat(self, messages, *, temperature=0.0, max_tokens=512, **kwargs):
        t0 = time.perf_counter()
        system = next((m["content"] for m in messages if m["role"] == "system"), "")
        user_assistant = [m for m in messages if m["role"] != "system"]

        resp = self._client.messages.create(
            model=self.model,
            system=system,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=user_assistant,
            **kwargs,
        )
        return {
            "text":       resp.content[0].text if resp.content else "",
            "model":      resp.model,
            "tokens_in":  resp.usage.input_tokens,
            "tokens_out": resp.usage.output_tokens,
            "latency_s":  time.perf_counter() - t0,
        }


# =========================================================================
#  Google (Gemini)
# =========================================================================
class GoogleLLM:
    """Wrapper around the `google.generativeai` SDK.

    pip install google-generativeai
    export GOOGLE_API_KEY=...        # or GEMINI_API_KEY

    Gemini's API uses `generate_content(...)` with parts. We map the
    OpenAI-style chat messages into Gemini's format.
    """

    def __init__(self, model: str = "gemini-2.5-flash", api_key: str | None = None):
        try:
            import google.generativeai as genai
        except ImportError as e:
            raise ImportError(
                "Google provider requires `pip install google-generativeai`."
            ) from e
        key = api_key or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        if not key:
            raise RuntimeError("Set GOOGLE_API_KEY (or GEMINI_API_KEY) in your environment.")
        genai.configure(api_key=key)
        self._genai = genai
        self.model = model

    def chat(self, messages, *, temperature=0.0, max_tokens=512, **kwargs):
        t0 = time.perf_counter()
        # Gemini handles "system_instruction" separately
        system = next((m["content"] for m in messages if m["role"] == "system"), "")
        gemini_messages = [
            {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
            for m in messages if m["role"] in ("user", "assistant")
        ]
        model = self._genai.GenerativeModel(
            model_name=self.model,
            system_instruction=system or None,
            generation_config={"temperature": temperature, "max_output_tokens": max_tokens, **kwargs},
        )
        resp = model.generate_content(gemini_messages)
        text = resp.text or ""
        # Gemini gives input/output token counts via usage_metadata (recent SDK)
        usage = getattr(resp, "usage_metadata", None)
        tokens_in  = getattr(usage, "prompt_token_count", 0) if usage else 0
        tokens_out = getattr(usage, "candidates_token_count", 0) if usage else 0
        return {"text": text, "model": self.model,
                "tokens_in": tokens_in, "tokens_out": tokens_out,
                "latency_s": time.perf_counter() - t0}


# =========================================================================
#  Ollama (local LLMs)
# =========================================================================
class OllamaLLM:
    """Local LLM via an Ollama server.

    Install Ollama: https://ollama.com
        ollama pull llama3.2:3b
        ollama serve         # usually running already on port 11434

    pip install ollama

    No API key needed. Latency depends on your hardware. CPU-only is fine for
    small (1-3B) models; bigger models really want a GPU.
    """

    def __init__(self, model: str = "llama3.2:3b", host: str | None = None):
        try:
            import ollama
        except ImportError as e:
            raise ImportError(
                "Ollama provider requires `pip install ollama` and a running Ollama server."
            ) from e
        self._client = ollama.Client(host=host or os.getenv("OLLAMA_HOST"))
        self.model = model

    def chat(self, messages, *, temperature=0.0, max_tokens=512, **kwargs):
        t0 = time.perf_counter()
        resp = self._client.chat(
            model=self.model,
            messages=messages,
            options={"temperature": temperature, "num_predict": max_tokens, **kwargs},
        )
        msg  = resp.get("message", {})
        text = msg.get("content", "")
        # Ollama returns prompt_eval_count and eval_count for tokens
        tokens_in  = resp.get("prompt_eval_count", 0)
        tokens_out = resp.get("eval_count", 0)
        return {"text": text, "model": self.model,
                "tokens_in": tokens_in, "tokens_out": tokens_out,
                "latency_s": time.perf_counter() - t0}


# =========================================================================
#  EMBEDDERS — same idea, for vector retrieval (NB 19)
# =========================================================================
class MockEmbedder:
    """Deterministic offline embedder — same one used in NB 19.

    Uses a fast, sha256-keyed pseudo-random vector per token, averaged and
    L2-normalised. Replace with `OpenAIEmbedder` or `LocalEmbedder` for real
    semantic search.
    """

    def __init__(self, dim: int = 256, seed: int = 0):
        self.dim = dim
        self.seed = seed

    def _word_vec(self, word: str):
        import numpy as np
        h = hashlib.sha256(f"{self.seed}::{word}".encode()).digest()
        rng = np.random.default_rng(int.from_bytes(h[:8], "big"))
        return rng.standard_normal(self.dim).astype("float32")

    def embed(self, texts: list[str]):
        import numpy as np
        out = np.zeros((len(texts), self.dim), dtype="float32")
        for i, t in enumerate(texts):
            words = re.findall(r"[a-zA-Z']+", t.lower())
            if not words:
                continue
            vecs = np.array([self._word_vec(w) for w in words])
            out[i] = vecs.mean(axis=0)
        norms = (out ** 2).sum(axis=1, keepdims=True) ** 0.5
        norms[norms == 0] = 1.0
        return out / norms


class OpenAIEmbedder:
    """OpenAI hosted embeddings.

    pip install openai
    export OPENAI_API_KEY=sk-...
    """

    def __init__(self, model: str = "text-embedding-3-small", api_key: str | None = None):
        from openai import OpenAI
        self._client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model

    def embed(self, texts: list[str]):
        import numpy as np
        resp = self._client.embeddings.create(model=self.model, input=texts)
        return np.array([d.embedding for d in resp.data], dtype="float32")


class LocalEmbedder:
    """Local embedding model via `sentence-transformers` (no API needed).

    pip install sentence-transformers

    The first call downloads the model (~80 MB for `all-MiniLM-L6-v2`).
    Subsequent calls run on your CPU/GPU — no per-call cost.
    """

    def __init__(self, model: str = "all-MiniLM-L6-v2"):
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as e:
            raise ImportError(
                "LocalEmbedder requires `pip install sentence-transformers`."
            ) from e
        self._model = SentenceTransformer(model)
        self.model = model

    def embed(self, texts: list[str]):
        return self._model.encode(texts, normalize_embeddings=True)


# =========================================================================
#  Convenience factory — pick a provider from a string
# =========================================================================
PROVIDERS = {
    "mock":      MockLLM,
    "openai":    OpenAILLM,
    "anthropic": AnthropicLLM,
    "google":    GoogleLLM,
    "ollama":    OllamaLLM,
}


def get_llm(provider: str = "mock", **kwargs):
    """Create an LLM client by short name.

    >>> llm = get_llm("mock")
    >>> llm = get_llm("openai", model="gpt-5.4-mini")
    """
    provider = provider.lower()
    if provider not in PROVIDERS:
        raise ValueError(f"unknown provider {provider!r}; pick from {sorted(PROVIDERS)}")
    return PROVIDERS[provider](**kwargs)


EMBEDDERS = {
    "mock":   MockEmbedder,
    "openai": OpenAIEmbedder,
    "local":  LocalEmbedder,
}


def get_embedder(provider: str = "mock", **kwargs):
    provider = provider.lower()
    if provider not in EMBEDDERS:
        raise ValueError(f"unknown embedder {provider!r}; pick from {sorted(EMBEDDERS)}")
    return EMBEDDERS[provider](**kwargs)
