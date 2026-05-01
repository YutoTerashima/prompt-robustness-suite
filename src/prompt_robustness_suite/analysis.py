from __future__ import annotations

from .suite import compare_prompts, mock_model


def run_ab_analysis(prompts: dict[str, str], cases: list[str]) -> dict[str, object]:
    scores = compare_prompts(prompts, cases)
    best = max(scores, key=scores.get)
    responses = {
        name: [mock_model(prompt, case) for case in cases]
        for name, prompt in prompts.items()
    }
    return {"scores": scores, "best": best, "responses": responses}
