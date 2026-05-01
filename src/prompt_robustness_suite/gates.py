from __future__ import annotations


def regression_gate(current: dict[str, float], baseline: dict[str, float], tolerance: float = 0.05) -> list[str]:
    failures = []
    for metric, base_value in baseline.items():
        current_value = current.get(metric, 0.0)
        if current_value + tolerance < base_value:
            failures.append(f"{metric}: {current_value:.3f} < {base_value:.3f} - {tolerance:.3f}")
    return failures
