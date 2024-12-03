# Plotting [Architecture Decision Record (ADR)](https://18f.gsa.gov/2021/07/06/architecture_decision_records_helpful_now_invaluable_later/)

Status: **DRAFT**

12/1/24

## Context

[Shared this with students:](https://edstem.org/us/courses/68651/discussion/5805993?comment=13444671)

> every time I've tried to fix something in JupyterHub recently, it seems to get worse, not better 😒 Remember when I said ["you will want to throw your computer out a window at one or many points in the class"](../../lecture_0.ipynb#you)? That's me with JupyterHub, Plotly, and [nbconvert](https://nbconvert.readthedocs.io/) (the PDF exporting engine) this past week. [Here's the running list of walls we've run into.][problems]
>
> A lot of the complication revolves around Plotly charts being interactive by default.

This is tied up with [how assignments are submitted](submission.md), as [support for interactive plots (in notebooks/HTML) in those tools varies](submission.md#tool).

## Options

| Option                                     | Pros                                                                                                          | Cons                                                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Plotly (interactive)**                   | No change required to course materials; interactive is cool                                                   | [Various problems][problems]                                                                          |
| **Plotly ([static][static])**              | Minimal change required to course materials; safer for PDF export; easy to switch between interactive and non | Students need to remember to switch; static isn't as cool as interactive                              |
| **[pandas native][pandas]**                | Less code; fewer packages; more native                                                                        | Requires changes throughout the materials; learning curve for me; static isn't as cool as interactive |
| **[seaborn](https://seaborn.pydata.org/)** | More powerful charts take less code than pandas                                                               | Learning curve for me; static isn't as cool as interactive                                            |

[problems]: ../instructor_guide.md#jupyterhub-troubleshooting
[static]: https://plotly.com/python/renderers/#static-image-renderers
[pandas]: https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html

[pandas can use Plotly as the plotting backend](https://plotly.com/python/pandas-backend/), which may be a way to split the difference between the options.

## Decision

TODO

## Consequences

TODO
