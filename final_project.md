# Final Project

The goal of the Final Project is to **prove or disprove a hypothesis using skills learned in this class, and demonstrate understanding of those techniques through explaining them to others**. It's open-ended — you decide what you're investigating. We're looking for you to be creative, and _just the right amount_ of ambitious.

## Proposal

[Details](final_project/proposal.md)

## Once you start

- [General assignment information](assignments.md)
- Create a new notebook to do the actual analysis; that is what you'll [turn in](#submission). To create, click:
  1. `File`
  1. `New notebook`
  1. `Python [conda env:python-public-policy]`
- Go back and find any information that's available _around_ the data, to get a better understanding of what it contains and means.
  - Might include a data dictionary
  - Might involve poking around a government agency's web site to understand their processes
  - Understand what all the different columns and values represent
- If you end up answering your initial research question easily (haven't met the requirements below), ask and answer follow-up question(s).

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
    - You may need to tweak your research question as you go. Show and explain why.
  - Have a conclusion that speaks to your question and hypothesis.
- **Use pandas** - 15 points
- **Not be trivial** - 35 points - requiring:
  - Transforming of DataFrames through [grouping](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html), [merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging), and/or [reshaping](https://pandas.pydata.org/docs/user_guide/reshaping.html)
  - Operations that aren't easily done in a spreadsheet
- **Have a visualization** (chart or map) of some kind - 15 points
  - Follow [best practices](https://xdgov.github.io/data-design-standards/)

If you answer the first question easily, that's fine; dig into / build off of it. Go deep, not broad.

```{dropdown} Is the subjectivity of "trivial" stressing you out?
If you insist: Make sure you use at least 40 lines of code to come to a conclusion.

- That code should be relevant to answering your question. In other words, having 40 lines of `print("hello world")` wouldn't count.
- If you meet all the requirements above, you will likely be well over this number.
- [How to count them automaticaly](final_project/resources.md#counting-lines-of-code)
```

## Examples

[Details](final_project/examples.md)

## Submission

1. Remove the following from the notebook, filename, file paths, etc:
   - Name
   - NetID
   - Sensitive information
      - API keys
      - Personally-identifiable information (PII)
1. Export the notebook as HTML by clicking:
   1. `File`
   1. `Save and Export Notebook As`
   1. `HTML`
      - You may need to [allow popups](https://support.google.com/chrome/answer/95472).
1. Submit.
   1. In [Brightspace](https://brightspace.nyu.edu/d2l/home/477758), go to `Content`.
      - Note that this is _not_ the `Assignments` tab of Brightspace.
   1. Click `Final Project`. You should see the TurnItIn/PeerMark dashboard.
   1. Follow [these instructions](https://guides.turnitin.com/hc/en-us/articles/21851026380813-Submitting-to-a-Feedback-Studio-assignment-using-D2L-LTI-1-3) to upload the `.html` file as-is.

### Notes

- **DO NOT WAIT UNTIL THE LAST MINUTE TO [SUBMIT](assignments.md#submission).** Leave yourself time to fix any [issues that come up](assignments.md#common-issues) in doing so, computer crashing, etc.
- Because it's the end of the course and [your peers are doing the reviews](final_project/peer_grading.md), **there will be no extensions or resubmissions**.


### Confirming you meet the requirements

The instructor doesn't have bandwidth to review everyone's full notebooks. Therefore, to be fair to everyone, any requests to have notebooks reviewed end to end will be denied — aside from [appeals to the peer grade](final_project/peer_grading.md). In other words, please don't ask "I think I'm done — can you make sure my Final Project is ok?" That said, more than happy to answer specific questions and help troubleshoot specific sections.

To confirm you meet [the requirements](#analysis-requirements) prior to submitting, you can:

- Take a pass through your own notebook, pretending you are grading someone else
- Ask someone else in the class to do so



## Peer grading

[Details](final_project/peer_grading.md)
