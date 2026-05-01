# Prompt Robustness Suite V2 Research Report

## Abstract

This V2 upgrade turns the repository into a reproducible project-level experiment suite. The run records the dataset, device, experiment matrix, metrics, figures, failure analysis, and reproduction commands in committed small artifacts.

## Dataset

- Source path: `data/processed/classification_examples.jsonl`
- Profile: `full`
- Runtime: `5.929` seconds
- Device: `cuda` / `NVIDIA GeForce RTX 5090 Laptop GPU`

## Methods

Experiments declared in `configs/experiment_matrix.yaml`:

- `baseline_policy_a`: `policy_a`
- `strict_policy_b`: `policy_b`
- `detector_policy_c`: `policy_c`
- `threshold_sweep`: `threshold`

## Experiments

The matrix produced `15` result rows. Best observed `macro_f1`: `0.5976` from `detector_policy_c`.

## Results

Key artifacts:

- `reports\results\v2_robustness_leaderboard.csv`
- `reports\results\v2_clustered_failures.json`
- `reports\figures\v2_attack_recall.png`
- `reports\figures\v2_benign_pass_rate.png`
- `reports\figures\v2_policy_macro_f1.png`

## Ablations

Configured ablations: casing, typoglycemia, base64_wrapper, instruction_sandwich. The generated ablation files quantify threshold, perturbation, architecture, retrieval, or metric sensitivity depending on the project.

## Failure Analysis

Failure records: `100`.

Top clusters:

- `original`: 100

## Discussion

Prompt robustness is regression testing. V2 measures attack recall and benign pass rate under perturbations, then promotes the best policy variant only if it clears both safety and usefulness gates.

## Limitations

- Full raw caches, model weights, and optimizer states are intentionally excluded from GitHub.
- Results are designed for reproducible portfolio research; they are not production safety, medical, or compliance guarantees.
- Some V2 experiments use compact local artifacts to keep the repository lightweight.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```
