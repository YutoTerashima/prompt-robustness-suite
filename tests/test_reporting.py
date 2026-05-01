from prompt_robustness_suite.reporting import prompt_leaderboard


def test_prompt_leaderboard_sorts():
    rows = [{"prompt": "a", "grounding": 0.5, "brevity": 1, "passed": False}, {"prompt": "b", "grounding": 1, "brevity": 1, "passed": True}]
    assert prompt_leaderboard(rows)[0]["prompt"] == "b"
