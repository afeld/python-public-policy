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

| Option       | Tool                             | Autograder support | Plagiarism detection | Inline annotation                    | Notebooks are interactive                          | Other pros                                                                                                                                   | Other cons                                                                                   |
| ------------ | -------------------------------- | ------------------ | -------------------- | ------------------------------------ | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **PDF**      | **{{lms_name}}**                 | N                  | [Y][lms-similarity]  | [Y][annotation]                      | N                                                  | Students are comfortable with {{lms_name}}; avoids "works on my machine"                                                                     | [Plotly needs extra packages][kaleido] and is [fragile][fragile]; long/wide outputs look bad |
| **HTML**     | **{{lms_name}}**                 | N                  | [Y][lms-similarity]  | [N][annotation]                      | Kinda - need to be downloaded                      | Students are comfortable with {{lms_name}}; outputs support scrolling, though that must be done by the student; avoids "works on my machine" | [Plotly rendering broken in v6.0.0][html-render]                                             |
| **Notebook** | **{{lms_name}}**                 | N                  | [N][lms-similarity]  | [N][annotation]                      | Kinda - need to be downloaded                      | Students are comfortable with {{lms_name}}; long outputs are collapsable/scrollable by the {{assistant_name}}                                | Need to be downloaded to be viewed                                                           |
| **Notebook** | [**Gradescope**][gradescope]     | [Y][gs-autograder] | [N][gs-similarity]   | N                                    | [Kinda][gs-interactive] - need to be downloaded    | Supported by both schools                                                                                                                    |                                                                                              |
| **Notebook** | [**Nbgrader**][nbgrader]         | Y                  | N                    | Y                                    | Y                                                  | Pre-installed in NYU {{coding_env_name}}                                                                                                     | Workflow is totally disconnected from {{lms_name}}                                           |
| **Notebook** | [**Otter Grader**][otter-grader] | Y                  | N                    | [Kinda - through PDFs][otter-manual] | N - [manual grading is through PDFs][otter-manual] | Built by Jupyter experts                                                                                                                     | Optimized for autograding over manual feedback                                               |

[lms-similarity]: https://guides.turnitin.com/hc/en-us/articles/23929463501965-File-requirements
[kaleido]: https://plotly.com/python/static-image-export/
[annotation]: https://community.d2l.com/brightspace/kb/articles/3529-evaluate-assignments-using-the-assignments-tool#supported-file-types-for-annotating-submissions
[html-render]: https://github.com/plotly/plotly.py/issues/5012
[gradescope]: https://support.nyu.edu/esc?id=kb_article&sysparm_article=KB0011989
[gs-autograder]: https://gradescope-autograders.readthedocs.io/
[gs-similarity]: https://portal.productboard.com/sz44uvlbbmnviv939g6lvnkd/c/500-code-similarity-support-for-jupyter-notebooks-ipynb-files-
[gs-interactive]: https://portal.productboard.com/sz44uvlbbmnviv939g6lvnkd/c/711-support-html-in-jupyter-notebooks
[nbgrader]: https://nbgrader.readthedocs.io/
[otter-grader]: https://otter-grader.readthedocs.io/
[otter-manual]: https://otter-grader.readthedocs.io/en/latest/pdfs.html

### PDF export

If sticking with PDFs, they can be exported from {{coding_env_name}}:

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
