# Final Project

The goal of the Final Project is to **prove or disprove a hypothesis using skills learned in this class, and demonstrate understanding of those techniques through explaining them to others**. It's open-ended — you decide what you're investigating. We're looking for you to be creative, and _just the right amount_ of ambitious.

## Proposal

[Details](final_project/proposal.md)

## Once you start

- [General assignment information](assignments.md)
- Create a new notebook to do the actual analysis; that is what you'll [turn in](#submission).
- Go back and find any information that's available _around_ the data, to get a better understanding of what it contains and means.
  - Might include a data dictionary
  - Might involve poking around a government agency's web site to understand their processes
  - Understand what all the different columns and values represent
- If you end up answering your initial research question easily (haven't met the requirements below), ask and answer follow-up question(s).

## Analysis requirements

In addition to the applicable [general assignment requirements](syllabus.md#assignment-scoring), your submission should:

<!-- make sure edits here are reflected in extras/scripts/final_project_check.py -->

- [**Read like a blog post**](assignments/open_ended.md#read-like-a-blog-post), and do the following - 35 points
  - Re-state the [question, hypothesis, and data source(s) with link(s)](final_project/proposal.md#format)
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

Note this is different than [submission for other assignments](assignments.md#submission).

1. Remove the following from the notebook, filename, file paths, etc:
   - Name
   - NetID
   - Sensitive information
      - API keys
      - Personally-identifiable information (PII)
1. [Share the notebook.](https://research.google.com/colaboratory/faq.html#notebook-storage) Under `General Access`, select:
   1. {% if id == "columbia" %}`LionMail`{% else %}`Anyone with the link`{% endif %}, then
   1. `Viewer`
1. Submit.
   {% if id == "columbia" -%}
   1. Go to [the `Final Project` Assignment in {{lms_name}}.]({{lms_url}}/assignments)
   {% else -%}
   1. Go to [`Content` -> `Final Project`](https://brightspace.nyu.edu/d2l/le/lessons/477758/topics/12556022).
   {%- endif %}
   1. Submit the URL to your notebook (`https://colab.research.google.com/drive/...`).

### Notes

- **DO NOT WAIT UNTIL THE LAST MINUTE TO [SUBMIT](assignments.md#submission).** Leave yourself time to fix any [issues that come up](assignments.md#common-issues) in doing so, computer crashing, etc.
- Because it's the end of the course and [your peers are doing the reviews](final_project/peer_grading.md), **there will be no extensions**.
- Hold off on responding to comments on your notebook before you get your Project grade.

### Confirming you meet the requirements

The instructor {% if id == "columbia" %}and {{assistant_name}} don't{% else %}doesn't{% endif %} have bandwidth to review everyone's full notebooks. Therefore, to be fair to everyone, any requests to have notebooks reviewed end to end will be denied — aside from [appeals to the peer grade](final_project/peer_grading.md). In other words, please don't ask "I think I'm done — can you make sure my Final Project is ok?" That said, more than happy to answer specific questions and help troubleshoot specific sections.

To confirm you meet [the requirements](#analysis-requirements) prior to submitting, you can:

- Take a pass through your own notebook, pretending you are grading someone else
- Ask someone else in the class to do so

## Peer grading

[Details](final_project/peer_grading.md)
