# [Final Project](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project.html) proposal details

## Process

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
1. Submit the proposal to {% if id == "columbia" %}the `Final Project proposal` Assignment{% else %}a new Conversation under the `Final Project proposals` [Discussion]({{discussions_url}}){% endif %}, using the format below.

If the proposal shows effort and follows the format below, full credit will be given.

## Format

- **What dataset(s) are you going to use?**
  - Please include link(s). If multiple, how are you going to merge/join them?
- **What's the question you are trying to answer?**
  - It should be _specific, and objectively answerable_ through the data available.
- **What's your hypothesis?**

## Tips

- Your question/hypothesis doesn't need to be something novel; confirming something you read in the news is fine.
- You won't be graded on the scientific soundness of your work.
  - That said, please think through and note assumptions/caveats/unknowns of your approach.
- The sooner you post your proposal, the sooner you'll get feedback.

## Simplified example

- **Dataset:** [Recycling Diversion and Capture Rates](https://data.cityofnewyork.us/Environment/Recycling-Diversion-and-Capture-Rates/gaq9-z3hz)
- **Question:** From 2016 to 2019, what community district increased their diversion (recycling) rate the most?
- **Hypothesis:** [Bushwick](https://communityprofiles.planning.nyc.gov/brooklyn/4), because it's gentrified over that time, and hipsters love to recycle.

## Another example

- **Dataset:** data about people's trash
- **Question:** Is recycling better now than before?
- **Hypothesis:** probably

What's wrong with this proposal?

Even the question can bake in assumptions. For example:

> What ZIP code has the highest number of food poisoning cases?

assumes a relationship between food-borne illness and geography. What assumptions does your question make?
