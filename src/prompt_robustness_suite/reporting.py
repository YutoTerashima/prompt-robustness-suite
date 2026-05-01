from __future__ import annotations


def prompt_leaderboard(rows: list[dict]) -> list[dict[str, object]]:
    groups: dict[str, list[dict]] = {}
    for row in rows:
        groups.setdefault(row["prompt"], []).append(row)
    board = []
    for prompt, items in groups.items():
        board.append(
            {
                "prompt": prompt,
                "mean_grounding": round(sum(float(item["grounding"]) for item in items) / len(items), 3),
                "mean_brevity": round(sum(float(item["brevity"]) for item in items) / len(items), 3),
                "pass_rate": round(sum(str(item["passed"]).lower() == "true" for item in items) / len(items), 3),
            }
        )
    return sorted(board, key=lambda row: (row["pass_rate"], row["mean_grounding"]), reverse=True)
