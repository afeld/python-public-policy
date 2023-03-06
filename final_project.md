# Final Project

- Open-ended
  - Be creative, and just the right amount of ambitious
- **Goal:** Prove or disprove a hypothesis using skills learned in this class

## Proposal

[Details](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/proposal.html)

## Once you start

- [General assignment information](https://python-public-policy.afeld.me/en/{{school_slug}}/assignments.html)
- Create a new notebook to do the actual analysis; that is what you'll [turn in](#submission).{% if id == 'nyu' %} To create, click:
  1. `File`
  1. `New notebook`
  1. `Python [conda env:python-public-policy]`{% endif %}
- Go back and find any information that's available _around_ the data, to get a better understanding of what it contains and means.
  - Might include a data dictionary
  - Might involve poking around a government agency's web site to understand their processes
  - Understand what all the different columns and values represent

## Analysis requirements

In addition to the applicable [general assignment requirements](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#assignment-scoring), your submission should:

<!-- make sure edits here are reflected in extras/scripts/final_project_check.py -->

- **Read like a blog post** - 35 points
  - Pretend you're explaining to a peer who hasn't taken this class. You don't need to teach them to code, but they should be able to follow what's going on.
  - Re-state the [question, hypothesis, and data source(s) with link(s)](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/proposal.html#format)
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
    - [How to count them automaticaly](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/resources.html#counting-lines-of-code)
  - Transforming data through [grouping](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html), [merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging), and/or [reshaping](https://pandas.pydata.org/docs/user_guide/reshaping.html) of DataFrames
  - Operations that aren't easily done in a spreadsheet.
- **Have a visualization** (chart or map) of some kind - 15 points
  - Follow [best practices](https://xdgov.github.io/data-design-standards/)

If you answer the first question easily, that's fine; dig into / build off of it. Go deep, not broad.

## Examples

Sample projects from past semesters:

- [NYC Restaurant Inspections, Creepy Crawly Edition](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/creepy_crawly.html)
- [Investigating Elevated Blood Lead Level Rates in Children in NYC](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/lead.html)
- [U.S. Universities - Regional Performance](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/universities.html)

Note these won't be runnable without downloading the source data.

## Submission

- **DO NOT WAIT UNTIL THE LAST MINUTE TO [SUBMIT](https://python-public-policy.afeld.me/en/{{school_slug}}/assignments.html).** Leave yourself time to fix any [issues that come up](https://python-public-policy.afeld.me/en/{{school_slug}}/assignments.html#common-issues) in doing so, computer crashing, etc.
- Please try to preserve anonymity.
  - Keep your name/username out of the notebook title, text cells, file paths, etc.
  - Hold off on responding to comments on your notebook before you get your Project grade.
- Don't leave any sensitive information in the notebook, such as:
  - API keys
  - Personally-identifiable information (PII)
{% if school_slug == "nyu" -%}
- You are encouraged to post your PDF in your Proposal Discussion thread so other folks from the class can see.
{% endif -%}

Because it's the end of the course and your peers are doing the reviews, **there will be no extensions or resubmissions**.

### Confirming you meet the requirements

The instructor and {{assisstant_name}} don't have bandwidth to review everyone's full notebooks. Therefore, to be fair to everyone, we will deny any requests to have notebooks reviewed end to end, aside from the appeals mentioned below. In other words, please don't ask us "I think I'm done — can you make sure my Final Project is ok?" That said, we are more than happy to answer specific questions and help troubleshoot specific sections.

To confirm you meet [the requirements](#analysis-requirements) prior to submitting, you can:

- Take a pass through your own notebook, pretending you are grading someone else
- Ask someone else in the class to do so

## Peer grading

Your Final Project will be reviewed and graded by three of your peers, and you will grade three others'. The person being graded will be anonymous, but the reviewers won't be. Your score will be the average of the peer grades. If you disagree with the grade, you can appeal by [emailing the instructor and {{assisstant_name}}](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#instructor-information).

### How to review

1. Open [{{lms_name}}]({{lms_url}}).
1. Go to Assignments, then `Final Project`.
{% if school_slug == "columbia" -%}
   - Each submission should appear as a link to `https://colab.research.google.com/drive/...`.
   - If you're unable to access the notebooks, make sure you're signed into Google with your Columbia account, and using that to try and access them. See [these instructions](https://support.google.com/docs/answer/6211862).
{%- endif %}
1. Leave substantive feedback, directly in the notebook and/or as a comment/attachment on the {{lms_name}} Assignment peer review area.
1. Check against [the requirements above](#analysis-requirements), factoring in the applicable [general assignment scoring](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#assignment-scoring).
   - Explain what points are being deducted for what.
   - State the final score in the comment area of the {{lms_name}} Assignment.

### Notes for reviewers

- Your feedback should include what they did well, as well as what they could do more clearly/simply/etc.
- Points should only be deducted based on the [requirements](#analysis-requirements). A "this could be done better/differently" comment doesn't _necessarily_ need to have a corresponding point deduction.
- You are _not_ expected to run any of their code. The notebook should be graded as-is.
{% if school_slug == "columbia" -%}
- While there are ways to find who owns a notebook on Colab, please avoid doing so.
- "Changes cannot be saved" doesn't apply to comments.
- [Canvas peer review documentation](https://community.canvaslms.com/t5/Student-Guide/How-do-I-submit-a-peer-review-to-an-assignment/ta-p/293)
{% endif -%}
- Reviews are expected to be in-depth, and thus take 15+ minutes each.
- As long as the feedback is thoughtful, you'll receive full points.
