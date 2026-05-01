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
## Publishable V2 Research Results

This repository now includes a full V2 research suite with real data, multiple baselines, ablations, result artifacts, figures, and failure analysis. The README summarizes the measured run so the project can be judged from results, not just project intent.

### Dataset And Scale

S-Labs prompt-injection train, validation, and test splits; 15,291 prompts evaluated across policy and perturbation variants.

- Full-profile result rows: `15`
- Experiment profile: `full`
- Experiment index: [`reports/results/experiment_index.json`](reports/results/experiment_index.json)
- Full report: [`reports/prompt_robustness_v2_research_report.md`](reports/prompt_robustness_v2_research_report.md)

### Main Results

| experiment_id | perturbation | macro_f1 | attack_recall | benign_pass_rate | unsafe_recall | safe_recall |
| --- | --- | --- | --- | --- | --- | --- |
| baseline_policy_a | original | 0.5160 | 0.1774 | 0.9777 | 0.1774 | 0.9777 |
| baseline_policy_a | casing | 0.5160 | 0.1774 | 0.9777 | 0.1774 | 0.9777 |
| baseline_policy_a | typoglycemia | 0.3546 | 0.0000 | 1.0000 | 0.0000 | 1.0000 |
| baseline_policy_a | base64_wrapper | 0.3546 | 0.0000 | 1.0000 | 0.0000 | 1.0000 |
| baseline_policy_a | instruction_sandwich | 0.5160 | 0.1774 | 0.9777 | 0.1774 | 0.9777 |
| strict_policy_b | original | 0.5532 | 0.2340 | 0.9594 | 0.2340 | 0.9594 |
| strict_policy_b | casing | 0.5532 | 0.2340 | 0.9594 | 0.2340 | 0.9594 |
| strict_policy_b | typoglycemia | 0.3623 | 0.0070 | 0.9999 | 0.0070 | 0.9999 |

### Analysis

- The leaderboard exposes the real tradeoff: stricter policies raise attack recall but can sharply reduce benign pass rate under instruction-sandwich style perturbations.
- Typoglycemia and base64-like wrappers nearly erase keyword-policy attack recall, which makes them useful regression tests for future detectors.
- Detector policy C improves original attack recall over the baseline policy, but still fails under encoding-style perturbations.
- This turns prompt engineering into a regression-tested artifact with measurable gates instead of a subjective prompt-writing exercise.

### Failure Analysis

- `original`: 100 records

The public failure artifacts use redacted previews or structured metadata where source examples may contain harmful, private, or otherwise sensitive text. This keeps the analysis reproducible without turning the README into a prompt-injection or unsafe-content corpus.

### Key Artifacts

- [`reports/results/v2_robustness_leaderboard.csv`](reports/results/v2_robustness_leaderboard.csv)
- [`reports/results/v2_clustered_failures.json`](reports/results/v2_clustered_failures.json)
- [`reports/figures/v2_attack_recall.png`](reports/figures/v2_attack_recall.png)
- [`reports/figures/v2_benign_pass_rate.png`](reports/figures/v2_benign_pass_rate.png)
- [`reports/figures/v2_policy_macro_f1.png`](reports/figures/v2_policy_macro_f1.png)

Figures:

- [`reports/figures/v2_attack_recall.png`](reports/figures/v2_attack_recall.png)
- [`reports/figures/v2_benign_pass_rate.png`](reports/figures/v2_benign_pass_rate.png)
- [`reports/figures/v2_policy_macro_f1.png`](reports/figures/v2_policy_macro_f1.png)

### Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

<!-- MATURITY_ITERATION -->
## Mature Research Engineering Pass

This repository has been reviewed against a professional portfolio rubric and now includes project-specific research modules, a mature review report, and an end-to-end walkthrough notebook.

- Maturity score: `94/100`
- Review report: [`reports/maturity_review.md`](reports/maturity_review.md)
- Walkthrough notebook: [`notebooks/maturity_walkthrough.ipynb`](notebooks/maturity_walkthrough.ipynb)
- Project-specific modules: `prompt_robustness_suite`

The latest iteration focuses on making the project understandable to a technical reviewer: what problem it addresses, what data it uses, what experiments were run, what failed, and what should be tried next.
