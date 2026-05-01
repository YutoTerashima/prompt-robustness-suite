from prompt_robustness_suite.analysis import run_ab_analysis


def test_ab_analysis_selects_best_prompt():
    data = run_ab_analysis({"a": "Answer.", "b": "Answer and cite evidence."}, ["case"])
    assert data["best"] == "b"
