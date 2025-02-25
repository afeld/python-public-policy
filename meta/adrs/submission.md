# Submission [Architecture Decision Record (ADR)](https://18f.gsa.gov/2021/07/06/architecture_decision_records_helpful_now_invaluable_later/)

Status: **DRAFT**

12/1/24

## Context

Students are currently [directed to export PDFs and submit via Brightspace](../../assignments.md#submission). This has various tradeoffs — see the comparison below. I think there might be a better way.

### Considerations

- The assignments are largely/increasingly open-ended.
- There's more need for manual line-by-line feedback.

### Nice-to-haves

- Auto-grading
- Minimal/foolproof [submission steps](../../assignments.md#submission)

## Options

| Option       | Tool                             | Pros                                                                                                                                         | Cons                                                                                                                                                       |
| ------------ | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PDF**      | **Brightspace**                 | Students are comfortable with Brightspace; avoids "works on my machine"                                                                     | No support for interactive plots; [Plotly needs extra packages][kaleido] and is [fragile][fragile]; long/wide outputs look bad                             |
| **HTML**     | **Brightspace**                 | Students are comfortable with Brightspace; outputs support scrolling, though that must be done by the student; avoids "works on my machine" | [Doesn't support annotation][annotation]; not rendered with scripts or styles, so needs to be downloaded; [Plotly rendering broken in v6.0.0][html-render] |
| **Notebook** | **Brightspace**                 | Students are comfortable with Brightspace; supports interactive plots; long outputs are collapsable/scrollable by the grader    | [Doesn't support annotation][annotation]; need to be downloaded to be viewed                                                                               |
| **Notebook** | [**Gradescope**][gradescope]     | Supported by both schools; [autograder support][gs-autograder]                                                                               | Notebook submissions aren't interactive; doesn't support plagiarism detection?                                                                             |
| **Notebook** | [**Nbgrader**][nbgrader]         | Pre-installed in NYU JupyterHub; autograder support                                                                                 | Workflow is totally disconnected from Brightspace                                                                                                         |
| **Notebook** | [**Otter Grader**][otter-grader] | Built by Jupyter experts; autograder support                                                                                                 | Optimized for autograding over manual feedback                                                                                                             |

[kaleido]: https://plotly.com/python/static-image-export/
[annotation]: https://community.d2l.com/brightspace/kb/articles/3529-evaluate-assignments-using-the-assignments-tool#supported-file-types-for-annotating-submissions
[html-render]: https://github.com/plotly/plotly.py/issues/5012
[gradescope]: https://support.nyu.edu/esc?id=kb_article&sysparm_article=KB0011989
[gs-autograder]: https://gradescope-autograders.readthedocs.io/
[nbgrader]: https://nbgrader.readthedocs.io/
[otter-grader]: https://otter-grader.readthedocs.io/

### PDF export

If sticking with PDFs, they can be exported from JupyterHub:

| Option                                   | Pros                        | Cons                                                                                                       |
| ---------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Directly, via [nbconvert][nbconvert]** | Single click, in theory     | [Fragile][fragile]                                                                                         |
| **As HTML, then Save as PDF**            | [Higher fidelity][fidelity] | Extra steps; Plotly doesn't re-draw on print, so need to resize window or set dimensions to ensure it fits |

[nbconvert]: https://nbconvert.readthedocs.io/
[fidelity]: https://github.com/jupyterlab/jupyterlab/issues/12113
[fragile]: ../instructor_guide.md#jupyterhub-troubleshooting

## Decision

TODO

## Consequences

TODO
