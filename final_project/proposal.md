# [Final Project](../final_project.md) proposal details

## Process

1. [Find a dataset](resources.md#open-data-portals) that seems interesting.
   - Use at least one dataset that you aren't familiar with.
     - Using data from a primary source is preferred.
   - Finding a dataset available in CSV or JSON is recommended, though [pandas can read other formats](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html).
1. If necessary, [upload the data](../assignments.md#storing-data).
1. Load the data into a DataFrame.
1. Inspect the data a bit.
1. Come up with a question that the data is capable of answering and _isn't trivial to answer_.
   - If you aren't sure, ask.
1. Come up with a hypothesis (a.k.a. a guess of the answer to the question).
1. Submit the proposal to [the `Final Project proposal` thread on Ed](https://edstem.org), using the format below.

If the proposal shows effort and follows the format below, full credit will be given.

## Format

- **What dataset(s) are you going to use?**
  - Please include link(s).
- **What's the question you are trying to answer?**
  - It should be _specific, and objectively answerable_ through the data available.
- **What columns of the DataFrame(s) are you going to use to answer that?**
- If you're using multiple datasets: **What columns are you going to merge/join them on?**
- **What's your hypothesis?**

Feel free to include any questions/concerns/uncertainties that the Reader can help with.

## Tips

- Don't overthink it; [the process above](#process) shouldn't take more than a few hours.
- Your question/hypothesis doesn't need to be something novel; confirming something you read / heard about is fine.
- You won't be graded on the scientific soundness of your work.
  - That said, please think through and note assumptions/caveats/unknowns of your approach.
- The sooner you post your proposal, the sooner you'll get feedback.
- The point of the proposal is to ensure you've dug into the data and that your project scope is reasonable. Think of it as a head start rather than something you're locked into.

## Simplified example

- **Dataset:** [Recycling Diversion and Capture Rates](https://data.cityofnewyork.us/Environment/Recycling-Diversion-and-Capture-Rates/gaq9-z3hz)
- **Question:** From 2016 to 2019, what community district increased their diversion (recycling) rate the most?
- **Columns:** `District`, `Fiscal Year`, `Diversion Rate-Total (Total Recycling / Total Waste)`
- **Hypothesis:** [Bushwick](https://communityprofiles.planning.nyc.gov/brooklyn/4), because it's gentrified over that time, and hipsters love to recycle.

## Another example

- **Dataset:** data about people's trash
- **Question:** Is recycling better now than before?
- **Hypothesis:** probably

What's wrong with this proposal?

## Question your question

Even the question can bake in assumptions. For example:

> What ZIP code has the highest number of food poisoning cases?

assumes a relationship between food-borne illness and geography. What assumptions does your question make?

## Changing your proposal

You may change your dataset/question after your proposal was submitted, but unless directed to do so, it's not recommended. [The purpose of the Final Project](../final_project.md) is to get practice doing data analysis through code … the dataset and research question are a means to that end. The hope is that you're getting into the analysis sooner than later, rather than being stuck picking the perfect dataset/question.

If you do decide to change them, be very sure they meet the requirements/tips above.
