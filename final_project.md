# Final Project

- Open-ended
  - Be creative, and just the right amount of ambitious
- **Goal:** Prove or disprove a hypothesis using skills learned in this class

## Proposal

1. [Find a dataset](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/resources.html#open-data-portals) that seems interesting.
   - Use at least one dataset that you aren't familiar with.
     - Using data from a primary source is preferred.
   - Finding a dataset available in CSV or JSON is recommended, though [pandas can read other formats](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html).
   {%- if id == "nyu" %}
   - Note that {{coding_env_name}} has a storage limit of 1GB.
   {%- endif %}
1. Inspect the data a bit.
1. Come up with a question that the data is capable of answering and _isn't trivial to answer_.
   - If you aren't sure, ask.
1. Come up with a hypothesis (a.k.a. a guess of the answer to the question).
1. Submit the proposal.

If the proposal shows effort and follows the format below, full credit will be given.

### Format

{% if id == "columbia" -%}
Submit responses to the following in the `Final Project proposal` Assignment:
{% else -%}
Post responses to the following as a new Conversation under the `Final Project proposals` [Discussion]({{discussions_url}}) by the start of class on 2/21:
{%- endif %}

- **What dataset are you going to use?**
  - Please include a link. If multiple, how are you going to merge/join them?
- **What's the question you are trying to answer?**
  - It should be _specific, and objectively answerable_ through the data available.
- **What's your hypothesis?**

### Tips

- Your question/hypothesis doesn't need to be something novel; confirming something you read in the news is fine.
- You won't be graded on the scientific soundness of your work.
  - That said, please think through and note assumptions/caveats/unknowns of your approach.
- The sooner you post your proposal, the sooner you'll get feedback.

### Simplified example

- **Dataset:** [Recycling Diversion and Capture Rates](https://data.cityofnewyork.us/Environment/Recycling-Diversion-and-Capture-Rates/gaq9-z3hz)
- **Question:** From 2016 to 2019, what community district increased their diversion (recycling) rate the most?
- **Hypothesis:** [Bushwick](https://communityprofiles.planning.nyc.gov/brooklyn/4), because it's gentrified over that time, and hipsters love to recycle.

### Another example

- **Dataset:** data about people's trash
- **Question:** Is recycling better now than before?
- **Hypothesis:** probably

What's wrong with this proposal?

Even the question can bake in assumptions. For example:

> What ZIP code has the highest number of food poisoning cases?

assumes a relationship between food-borne illness and geography. What assumptions does your question make?

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
  - Re-state the question, hypothesis, and data source(s) with link(s)
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

Your Final Project will be reviewed and graded by three of your peers, and you will grade three others'. Your score will be the average of the peer grades. If you disagree with the grade, you can appeal by [emailing the instructor and {{assisstant_name}}](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#instructor-information).

### How to review

1. Open [{{lms_name}}]({{lms_url}}).
1. Open the Assignment.
1. Check against [the requirements above](#analysis-requirements), factoring in the applicable [general assignment scoring](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#assignment-scoring).
   - Explain what points are being deducted for what.
1. Leave substantive feedback, directly in the notebook or in the overall comment area.
   - This should include what they did well, as well as what they could do more clearly/simply/etc.

You are _not_ expected to run any of their code. The notebook should be graded as-is.

{% if school_slug == "columbia" -%}
While there are ways to find who owns a notebook on Colab, please avoid doing so.
{% endif -%}
