# Submission [Architecture Decision Record (ADR)](https://blog.18f.org/2021/07/06/architecture_decision_records_helpful_now_invaluable_later/)

Status: **DRAFT**

12/1/24

## Context

Students are currently [directed to export PDFs and submit via Brightspace](../../assignments.md#submission). This has various tradeoffs — see the comparison below. I think there might be a better way.

### Considerations

- The assignments are largely/increasingly open-ended.
- There's more need for manual line-by-line feedback than auto-grading.

### Nice-to-haves

- Auto-grading
- Plagiarism detection
- Minimal/foolproof workflows for:
  - [Submission](../../assignments.md#submission)
  - [Grading](../assistant_guide.md#grading)

## [Options](https://docs.google.com/spreadsheets/d/181B2YeSahgSkTMyoo7QbfLC4pm6sEQyj_N78XtsfFWo/edit?gid=0#gid=0)

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSzltT-noD1xOhsmqzkW20Vx8BMVBydlAyWPZrml046nVZPPeC1KeBeInLhEXmdGV_FRe8uCGUA07x7/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false" height="500"></iframe>

### PDF export

If sticking with PDFs, they can be exported from Google Colab:

| Option                                   | Pros                        | Cons                                                                                                       |
| ---------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Directly, via [nbconvert][nbconvert]** | Single click, in theory     | [Fragile][fragile]                                                                                         |
| **As HTML, then Save as PDF**            | [Higher fidelity][fidelity] | Extra steps; Plotly doesn't re-draw on print, so need to resize window or set dimensions to ensure it fits |

[nbconvert]: https://nbconvert.readthedocs.io/
[fidelity]: https://github.com/jupyterlab/jupyterlab/issues/12113
[fragile]: https://web.archive.org/web/20251015160329/https://python-public-policy.afeld.me/en/nyu/meta/instructor_guide.html#jupyterhub-troubleshooting

## Decision

Notebook + Python files through Gradescope

## Consequences

TODO
