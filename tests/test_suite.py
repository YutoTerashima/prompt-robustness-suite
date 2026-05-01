from prompt_robustness_suite.suite import cluster_failures, compare_prompts


def test_prompt_comparison_prefers_evidence():
    scores = compare_prompts({"v1": "Answer.", "v2": "Answer and cite evidence."}, ["case"])
    assert scores["v2"] > scores["v1"]
    assert cluster_failures(["No evidence", "Evidence: x"])["ok"] == 1
