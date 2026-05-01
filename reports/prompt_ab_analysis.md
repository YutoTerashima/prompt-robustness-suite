# Prompt Robustness Analysis

Prompt variants are evaluated on stable cases rather than anecdotal examples.

| prompt | mean_score | failures | dominant_failure |
| --- | --- | --- | --- |
| v1 | 0.5 | 6 | missing_evidence |
| v2 | 1.0 | 0 | none |
| v3 | 0.88 | 1 | too_verbose |

## Interpretation

`v2` wins in this miniature suite because it consistently asks for evidence.
`v3` is more cautious but sometimes verbose. This mirrors real prompt tradeoffs:
quality, concision, grounding, and calibration often move independently.
