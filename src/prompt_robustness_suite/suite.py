from __future__ import annotations


def mock_model(prompt: str, case: str) -> str:
    if "cite evidence" in prompt.lower():
        return f"Answer for {case}. Evidence: retrieved context."
    return f"Answer for {case}."


def score(response: str) -> float:
    value = 0.5
    if "Evidence:" in response:
        value += 0.5
    return value


def compare_prompts(prompts: dict[str, str], cases: list[str]) -> dict[str, float]:
    return {
        name: sum(score(mock_model(prompt, case)) for case in cases) / len(cases)
        for name, prompt in prompts.items()
    }


def cluster_failures(responses: list[str]) -> dict[str, int]:
    clusters = {"missing_evidence": 0, "ok": 0}
    for response in responses:
        clusters["ok" if "Evidence:" in response else "missing_evidence"] += 1
    return clusters
