# Submission [Architecture Decision Record (ADR)](https://18f.gsa.gov/2021/07/06/architecture_decision_records_helpful_now_invaluable_later/)

Status: **DRAFT**

12/1/24

## Context

Students are currently [directed to export PDFs and submit via {{lms_name}}](../../assignments.md#submission). This has various tradeoffs — see the comparison below. I think there might be a better way.

### Considerations

- The assignments are largely/increasingly open-ended.
- There's more need for manual line-by-line feedback.

### Nice-to-haves

- Auto-grading
- Minimal/foolproof [submission steps](../../assignments.md#submission)

## Options

### Format

| Option       | Pros                                                                                                                         | Cons                                                                                                                           |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **PDF**      | Avoids "works on my machine"                                                                                                 | No support for interactive plots; [Plotly needs extra packages][kaleido] and is [fragile][fragile]; long/wide outputs look bad |
| **HTML**     | Supports interactive plots; outputs support scrolling, though that must be done by the student; avoids "works on my machine" | [Plotly rendering broken in v6.0.0][html-render]                                                                               |
| **Notebook** | Supports interactive plots; long outputs are collapsable/scrollable by the {{assistant_name}}                                |                                                                                                                                |

[kaleido]: https://plotly.com/python/static-image-export/
[html-render]: https://github.com/plotly/plotly.py/issues/5012

### PDF export

If sticking with PDFs, they can be exported from {{coding_env_name}}:

| Option                                   | Pros                        | Cons                                                                                                       |
| ---------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Directly, via [nbconvert][nbconvert]** | Single click, in theory     | [Fragile][fragile]                                                                                         |
| **As HTML, then Save as PDF**            | [Higher fidelity][fidelity] | Extra steps; Plotly doesn't re-draw on print, so need to resize window or set dimensions to ensure it fits |

[nbconvert]: https://nbconvert.readthedocs.io/
[fidelity]: https://github.com/jupyterlab/jupyterlab/issues/12113
[fragile]: ../instructor_guide.md#jupyterhub-troubleshooting

### Tool

| Option                           | [Format](#format) | Pros                                                                        | Cons                                                                           |
| -------------------------------- | ----------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **{{lms_name}}**                 | PDF               | Students are comfortable with it                                            |                                                                                |
| **{{lms_name}}**                 | HTML              | Students are comfortable with it                                            | [Doesn't support annotation][annotation]                                       |
| **{{lms_name}}**                 | notebook          | Students are comfortable with it                                            | [Doesn't support annotation][annotation]; need to be downloaded to be viewed   |
| [**Gradescope**][gradescope]     | notebook          | Supported by both schools; [autograder support (for notebooks)][autograder] | Notebook submissions aren't interactive; doesn't support plagiarism detection? |
| [**Nbgrader**][nbgrader]         | notebook          | Pre-installed in NYU {{coding_env_name}}                                    | Workflow is totally disconnected from {{lms_name}}                             |
| [**Otter Grader**][otter-grader] | notebook          | TODO                                                                        | Optimized for autograding over manual feedback                                 |

[annotation]: https://community.d2l.com/brightspace/kb/articles/3529-evaluate-assignments-using-the-assignments-tool#supported-file-types-for-annotating-submissions
[gradescope]: https://support.nyu.edu/esc?id=kb_article&sysparm_article=KB0011989
[autograder]: https://gradescope-autograders.readthedocs.io/
[nbgrader]: https://nbgrader.readthedocs.io/
[otter-grader]: https://otter-grader.readthedocs.io/

## Decision

TODO

## Consequences

TODO
