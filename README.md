# Prompt Robustness Suite

A small framework for treating prompts like testable artifacts: variants, test
cases, A/B comparisons, and failure clustering.

## Quick Start

```bash
pip install -e ".[dev]"
python examples/run_prompt_ab.py
pytest
```

## Research Brief

See [`docs/research_brief.md`](docs/research_brief.md) for why prompt changes
should be tested like behavior-defining code.

## Portfolio Notes

This project frames prompt engineering as versioned, tested behavior rather than intuition.

## Experiment Artifacts

- Prompt variants: [`examples/prompt_variants.json`](examples/prompt_variants.json)
- Results: [`reports/prompt_ab_results.csv`](reports/prompt_ab_results.csv)
- Analysis: [`reports/prompt_ab_analysis.md`](reports/prompt_ab_analysis.md)

## Regression Gates

The suite includes metric regression gates so prompt variants can fail CI when
grounding, format validity, or task quality drops beyond tolerance.

## Full Prompt Suite

The project includes 32 prompt-evaluation rows in
[`reports/full_prompt_results.csv`](reports/full_prompt_results.csv) and a report
in [`reports/full_prompt_analysis.md`](reports/full_prompt_analysis.md).

## Prompt Leaderboard

The suite can summarize prompt variants into a small leaderboard using pass rate,
grounding, and brevity metrics.
## Real Public Dataset Experiment

`reports/real_prompt_injection_ab_eval.md` evaluates two prompt-injection detection variants on a
real 320-row sample from
[S-Labs/prompt-injection-dataset](https://huggingface.co/datasets/S-Labs/prompt-injection-dataset),
turning prompt robustness into a measurable regression test.

## GPU-Backed Real Experiment

This repository now includes a reproducible GPU-backed experiment using `S-Labs/prompt-injection-dataset`.
The smoke path runs on the local RTX 5090 Laptop GPU through the `Transformers` conda
environment and writes metrics, figures, and a markdown report.

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

Main report: `reports/prompt_robustness_real_benchmark.md`.

<!-- V2_RESEARCH_UPGRADE -->
## Publishable V2 Research Upgrade

This repository now includes a project-level V2 experiment suite:

- Reproducible matrix: `configs/experiment_matrix.yaml`
- Main runner: `scripts/run_matrix.py --device cuda --profile full`
- Failure analysis: `scripts/analyze_failures.py`
- Research report: `reports/prompt_robustness_v2_research_report.md`
- Experiment index: `reports/results/experiment_index.json`

The V2 artifacts include multiple experiments, ablations, figures, failure cases, and a discussion section while keeping raw caches and large checkpoints out of Git.

