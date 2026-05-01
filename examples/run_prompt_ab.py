from prompt_robustness_suite.suite import compare_prompts


if __name__ == "__main__":
    scores = compare_prompts(
        {"v1": "Answer briefly.", "v2": "Answer briefly and cite evidence."},
        ["rag question", "agent question"],
    )
    print(scores)
