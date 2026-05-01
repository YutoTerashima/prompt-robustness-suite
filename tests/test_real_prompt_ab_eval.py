import json
from pathlib import Path


def test_real_prompt_ab_eval_has_two_variants():
    result = json.loads(Path("reports/real_prompt_injection_ab_eval.json").read_text(encoding="utf-8"))
    assert result["rows"] >= 300
    assert "v1" in result and "v2" in result
    assert result["v2"]["recall"] >= result["v1"]["recall"]
