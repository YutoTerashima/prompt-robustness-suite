from prompt_robustness_suite.gates import regression_gate


def test_regression_gate_detects_drop():
    failures = regression_gate({"grounding": 0.7}, {"grounding": 0.9}, tolerance=0.05)
    assert failures
