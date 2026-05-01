# Full Prompt Robustness Analysis

        This suite contains 32 prompt-evaluation rows across four prompt variants.

        ## Summary by Prompt

        | prompt | cases | mean_grounding | pass_rate |
| --- | --- | --- | --- |
| baseline | 8 | 0.55 | 0.0 |
| calibrated | 8 | 0.84 | 1.0 |
| concise | 8 | 0.61 | 0.0 |
| evidence | 8 | 0.82 | 1.0 |

        ## Sample Cases

        | case_id | prompt | grounding | brevity | passed |
| --- | --- | --- | --- | --- |
| PR-001 | baseline | 0.55 | 0.72 | False |
| PR-002 | evidence | 0.82 | 0.72 | True |
| PR-003 | calibrated | 0.84 | 0.72 | True |
| PR-004 | concise | 0.61 | 0.9 | False |
| PR-005 | baseline | 0.55 | 0.72 | False |
| PR-006 | evidence | 0.82 | 0.72 | True |
| PR-007 | calibrated | 0.84 | 0.72 | True |
| PR-008 | concise | 0.61 | 0.9 | False |
| PR-009 | baseline | 0.55 | 0.72 | False |
| PR-010 | evidence | 0.82 | 0.72 | True |
| PR-011 | calibrated | 0.84 | 0.72 | True |
| PR-012 | concise | 0.61 | 0.9 | False |
