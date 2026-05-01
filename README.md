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
