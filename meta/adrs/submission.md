# Submission [Architecture Decision Record (ADR)](https://18f.gsa.gov/2021/07/06/architecture_decision_records_helpful_now_invaluable_later/)

Status: **DRAFT**

12/1/24

## Context

Students are currently [directed to export PDFs and submit via {{lms_name}}](../../assignments.md#submission).

TODO

## Options

### Format

| Option       | Pros                                                                                          | Cons                                                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **PDF**      | Avoids "works on my machine"                                                                  | No support for interactive plots; [Plotly needs extra packages][kaleido] and is [fragile][fragile]; long outputs look bad |
| **HTML**     | Supports interactive plots; outputs support scrolling                                         | TODO                                                                                                                      |
| **Notebook** | Supports interactive plots; long outputs are collapsable/scrollable by the {{assistant_name}} | Can hide long outputs; can interact with interactive plots; TODO                                                          |

[kaleido]: https://plotly.com/python/static-image-export/
[fragile]: ../instructor_guide.md#jupyterhub-troubleshooting

### Tool

| Option           | Pros | Cons                                    |
| ---------------- | ---- | --------------------------------------- |
| **{{lms_name}}** | TODO | TODO                                    |
| **Gradescope**   | TODO | Notebook submissions aren't interactive |

## Decision

TODO

## Consequences

TODO
