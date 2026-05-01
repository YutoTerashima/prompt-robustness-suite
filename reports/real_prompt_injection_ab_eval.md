# Real Dataset A/B Prompt Robustness Evaluation

Source: [S-Labs/prompt-injection-dataset](https://huggingface.co/datasets/S-Labs/prompt-injection-dataset)

The suite evaluates two deterministic prompt-injection detectors on 320 public rows.

- v1: {'precision': 0.778, 'recall': 0.107, 'f1': 0.188}
- v2: {'precision': 0.635, 'recall': 0.252, 'f1': 0.361}

Interpretation: this is a real regression target. A production prompt classifier should improve
recall without simply overfitting to obvious keywords.
