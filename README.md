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
