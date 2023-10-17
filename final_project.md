# Final Project

- Open-ended
  - Be creative, and just the right amount of ambitious
- **Goal:** Prove or disprove a hypothesis using skills learned in this class

## Proposal

[Details](final_project/proposal.md)

## Once you start

- [General assignment information](assignments.md)
- Create a new notebook to do the actual analysis; that is what you'll [turn in](#submission).{% if id == 'nyu' %} To create, click:
  1. `File`
  1. `New notebook`
  1. `Python [conda env:python-public-policy]`{% endif %}
- Go back and find any information that's available _around_ the data, to get a better understanding of what it contains and means.
  - Might include a data dictionary
  - Might involve poking around a government agency's web site to understand their processes
  - Understand what all the different columns and values represent

## Analysis requirements

In addition to the applicable [general assignment requirements](syllabus.md#assignment-scoring), your submission should:

<!-- make sure edits here are reflected in extras/scripts/final_project_check.py -->

- **Read like a blog post** - 35 points
  - Pretend you're explaining to a peer who hasn't taken this class. You don't need to teach them to code, but they should be able to follow what's going on.
  - Re-state the [question, hypothesis, and data source(s) with link(s)](final_project/proposal.md#format)
  - Walk the reader through what you're doing in every step and what they should be taking away from it.
    - You are more than welcome to inject personality in there; doesn't need to be dry.
  - Use text cells with [Markdown](https://www.markdownguide.org/basic-syntax/) for formatting.
    - You'll need to [change the cell type to Markdown](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html#Markdown-Cells).
  - If you hit any dead ends in your analysis, leave them in.
    - For example, include charts that you generate that may not show anything interesting and explain what you are choosing to look at instead.
    - You should still be cleaning up unused/broken code to make your notebook readable.
  - Have a conclusion that speaks to your question and hypothesis.
- **Use pandas** - 15 points
- **Not be trivial** - 35 points - requiring:
  - At least 40 lines of code to come to a conclusion
    - [How to count them automaticaly](final_project/resources.md#counting-lines-of-code)
  - Transforming data through [grouping](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html), [merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging), and/or [reshaping](https://pandas.pydata.org/docs/user_guide/reshaping.html) of DataFrames
  - Operations that aren't easily done in a spreadsheet.
- **Have a visualization** (chart or map) of some kind - 15 points
  - Follow [best practices](https://xdgov.github.io/data-design-standards/)

If you answer the first question easily, that's fine; dig into / build off of it. Go deep, not broad.

## Examples

[Details](final_project/examples.md)

## Submission

- **DO NOT WAIT UNTIL THE LAST MINUTE TO [SUBMIT](assignments.md).** Leave yourself time to fix any [issues that come up](assignments.md#common-issues) in doing so, computer crashing, etc.
- Please try to preserve anonymity.
  - Keep your name/username out of the notebook title, text cells, file paths, etc.
  - Hold off on responding to comments on your notebook before you get your Project grade.
- Don't leave any sensitive information in the notebook, such as:
  - API keys
  - Personally-identifiable information (PII)

Because it's the end of the course and [your peers are doing the reviews](final_project/peer_grading.md), **there will be no extensions{% if id == 'nyu' %} or resubmissions{% endif %}**.

### Confirming you meet the requirements

The instructor and {{assistant_name}} don't have bandwidth to review everyone's full notebooks. Therefore, to be fair to everyone, we will deny any requests to have notebooks reviewed end to end, aside from the appeals mentioned below. In other words, please don't ask us "I think I'm done — can you make sure my Final Project is ok?" That said, we are more than happy to answer specific questions and help troubleshoot specific sections.

To confirm you meet [the requirements](#analysis-requirements) prior to submitting, you can:

- Take a pass through your own notebook, pretending you are grading someone else
- Ask someone else in the class to do so

## Peer grading

[Details](final_project/peer_grading.md)
