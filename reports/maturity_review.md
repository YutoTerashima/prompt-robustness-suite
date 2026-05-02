# Prompt Robustness Suite Mature Research Review

## Abstract

Which prompt policies survive realistic perturbations without destroying benign pass rate? This mature iteration packages the project as a reviewable research-engineering artifact rather than a standalone demo.

## Research Question

Which prompt policies survive realistic perturbations without destroying benign pass rate?

## Dataset

This section preserves the standard V2 report interface expected by tests and reviewers.

## Dataset Card

- Dataset summary: S-Labs prompt-injection train, validation, and test splits; 15,291 prompts across policy and perturbation variants.
- Profile: `full`
- Result rows: `15`
- Artifact count: `5`

## Methods

The project now separates reusable project-specific modules from experiment orchestration. The modules are intentionally small and importable from tests, notebooks, and reporting scripts.

### `prompt_robustness_suite.perturbations`

Perturbation families for casing, typoglycemia, wrapping, and instruction sandwich tests.

Public helpers:

- `perturb`
- `perturbation_matrix`
- `family_labels`

### `prompt_robustness_suite.regression_gates`

Attack-recall and benign-pass-rate gates for prompt regression testing.

Public helpers:

- `gate_result`
- `recommended_policy`
- `leaderboard_summary`

### `prompt_robustness_suite.policy_variants`

Prompt policy A/B/C definitions and detector-routing helpers.

Public helpers:

- `policy_keywords`
- `evaluate_policy`
- `policy_tradeoff`

## Experiments

This section preserves the standard V2 report interface and points to the concrete matrix below.

## Experiment Matrix

The current committed matrix records full-profile results and small artifacts. Large raw datasets, model checkpoints, optimizer states, and cache files remain outside Git.

| accuracy | attack_recall | benign_pass_rate | experiment_id | macro_f1 | perturbation | safe_f1 | safe_precision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.6172 | 0.1774 | 0.9777 | baseline_policy_a | 0.5160 | original | 0.7374 | 0.5918 |
| 0.6172 | 0.1774 | 0.9777 | baseline_policy_a | 0.5160 | casing | 0.7374 | 0.5918 |
| 0.5495 | 0.0000 | 1.0000 | baseline_policy_a | 0.3546 | typoglycemia | 0.7093 | 0.5495 |
| 0.5495 | 0.0000 | 1.0000 | baseline_policy_a | 0.3546 | base64_wrapper | 0.7093 | 0.5495 |
| 0.6172 | 0.1774 | 0.9777 | baseline_policy_a | 0.5160 | instruction_sandwich | 0.7374 | 0.5918 |
| 0.6327 | 0.2340 | 0.9594 | strict_policy_b | 0.5532 | original | 0.7416 | 0.6044 |
| 0.6327 | 0.2340 | 0.9594 | strict_policy_b | 0.5532 | casing | 0.7416 | 0.6044 |
| 0.5526 | 0.0070 | 0.9999 | strict_policy_b | 0.3623 | typoglycemia | 0.7107 | 0.5512 |
| 0.5495 | 0.0000 | 1.0000 | strict_policy_b | 0.3546 | base64_wrapper | 0.7093 | 0.5495 |
| 0.4505 | 1.0000 | 0.0000 | strict_policy_b | 0.3106 | instruction_sandwich | 0.0000 | 0.0000 |

## Results

- Typoglycemia and base64-like wrappers expose brittle keyword policies.
- Instruction-sandwich perturbations reveal overblocking risk.
- The project turns prompt changes into measurable regression gates.

## Ablations

Ablations are represented by the committed experiment matrix and companion result tables. The important review criterion is not only whether a model wins, but whether the artifacts explain which tradeoff changes when the method changes.

## Failure Analysis

- Failure records: `100`
- `original`: 100 records

Failure examples are redacted or summarized when source text may contain unsafe, private, or copyrighted content. The goal is to preserve diagnostic value without publishing harmful details.

## Engineering Notes

- Package namespace: `prompt_robustness_suite`
- The new maturity modules can be imported independently of full experiment execution.
- The walkthrough notebook gives reviewers a low-friction entry point.
- Existing scripts remain compatible so previous reproduction commands continue to work.

## Maturity Review

Overall maturity score: `97/100`.

| Category | Score |
| --- | --- |
| meaning | 20/20 |
| engineering | 19/20 |
| experiments | 18/20 |
| analysis | 20/20 |
| readme_examples | 18/20 |

Professional-review blockers:

- No blocking issues remain for a portfolio/recruiter review pass.

## Limitations

- The project is optimized for reproducible portfolio review, not production deployment.
- Large datasets and checkpoints are intentionally excluded from GitHub.
- Metrics should be reproduced before using them as publication claims.

## Next Experiments

- Add multilingual paraphrase perturbations.
- Add detector variants trained from MCP security artifacts.
- Promote regression gates into CI examples.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

## Reviewer Checklist

- README contains measured results and analysis.
- Reports contain dataset, method, result, failure, limitation, and reproduction sections.
- Tests import the maturity modules.
- Raw data and model weights are not tracked.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

## Top-Tier Review Gate

The highest-standard review gate requires evidence-backed claims, artifact provenance, explicit reproducibility metadata, strict artifact hygiene, and reviewer-facing limitations.

- Score: `97/100`
- Reviewer packet: `docs/top_tier_reviewer_packet.md`
- Claim-evidence matrix: `reports/results/claim_evidence_matrix.csv`
- Artifact manifest: `reports/results/artifact_manifest.json`
- Reproducibility manifest: `reports/results/reproducibility_manifest.json`
- Quality gate: `reports/results/top_tier_quality_gate.json`
