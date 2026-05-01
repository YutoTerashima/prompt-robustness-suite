from __future__ import annotations

"""Report metadata for the mature portfolio iteration."""

PROJECT_TITLE = 'Prompt Robustness Suite'
RESEARCH_PROBLEM = 'Which prompt policies survive realistic perturbations without destroying benign pass rate?'
DATASET_SUMMARY = 'S-Labs prompt-injection train, validation, and test splits; 15,291 prompts across policy and perturbation variants.'
TAKEAWAYS = ['Typoglycemia and base64-like wrappers expose brittle keyword policies.', 'Instruction-sandwich perturbations reveal overblocking risk.', 'The project turns prompt changes into measurable regression gates.']
NEXT_EXPERIMENTS = ['Add multilingual paraphrase perturbations.', 'Add detector variants trained from MCP security artifacts.', 'Promote regression gates into CI examples.']


def report_outline() -> list[str]:
    return [
        "Abstract",
        "Research question",
        "Dataset card",
        "Methods",
        "Experiment matrix",
        "Results",
        "Ablations",
        "Failure analysis",
        "Engineering notes",
        "Limitations",
        "Reproduction",
    ]


def maturity_claims() -> dict[str, object]:
    return {
        "title": PROJECT_TITLE,
        "problem": RESEARCH_PROBLEM,
        "dataset": DATASET_SUMMARY,
        "takeaways": TAKEAWAYS,
        "next_experiments": NEXT_EXPERIMENTS,
    }
