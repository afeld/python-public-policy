# Submission [Architecture Decision Record (ADR)](https://18f.gsa.gov/2021/07/06/architecture_decision_records_helpful_now_invaluable_later/)

Status: **DRAFT**

12/1/24

## Context

Students are currently [directed to export PDFs and submit via Brightspace](../../assignments.md#submission). This has various tradeoffs — see the comparison below — and I think there might be a better way.

## Options

### Format

| Option       | Pros                                                                                           | Cons                                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **PDF**      | Avoids "works on my machine"                                                                   | No support for interactive plots; [Plotly needs extra packages][kaleido] and is [fragile][fragile]; long outputs look bad |
| **HTML**     | Supports interactive plots; outputs support scrolling, though that must be done by the student | TODO                                                                                                                      |
| **Notebook** | Supports interactive plots; long outputs are collapsable/scrollable by the grader  | Can hide long outputs; can interact with interactive plots; TODO                                                          |

[kaleido]: https://plotly.com/python/static-image-export/

### PDF export

If sticking with PDFs, they can be exported from JupyterHub:

| Option                                   | Pros                        | Cons                                                                                          |
| ---------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------- |
| **Directly, via [nbconvert][nbconvert]** | Single click, in theory     | [Fragile][fragile]                                                                            |
| **As HTML, then Save as PDF**            | [Higher fidelity][fidelity] | Plotly doesn't re-draw on print, so need to resize window or set dimensions to ensure it fits |

[nbconvert]: https://nbconvert.readthedocs.io/
[fidelity]: https://github.com/jupyterlab/jupyterlab/issues/12113
[fragile]: ../instructor_guide.md#jupyterhub-troubleshooting

### Tool

| Option                       | Supports      | Pros                                          | Cons                                    |
| ---------------------------- | ------------- | --------------------------------------------- | --------------------------------------- |
| **Brightspace**             | PDF, HTML     | Students are comfortable with it              | TODO                                    |
| **[Gradescope][gradescope]** | PDF, notebook | Supported by both schools; autograder support | Notebook submissions aren't interactive |

[gradescope]: https://nyu.service-now.com/sp?id=kb_article&sysparm_article=KB0018576&sys_kb_id=408338081bbf5c50a54ffdd51a4bcb0c&spa=1

## Decision

TODO

## Consequences

TODO
