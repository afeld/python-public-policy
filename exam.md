# Exam

The exam will contain fill-in-the-blank, matching, and free response questions, coding and high-level. It will be done on paper, closed-book (no cheat sheets, phones, laptops, etc).

## Topics

The exam will cover the following:

- Python fundamentals
  - Types
  - Variables
  - Conditionals
  - Functions
- pandas data structures
- Jupyter concepts
- Data manipulation
  - Boolean indexing
  - Grouping
  - Cleaning
  - Merging
- Troubleshooting
- Data visualization
- Time series
  - Resampling
- APIs, conceptually

## Example questions

Recommendation: Try completing them without using a search engine, generative AI, the course materials, etc.

- What is the value of `y` after the following code is executed?

  ```python
  x = 5
  y = 2 * x
  x = 50
  ```

- What will the following code print?

  ```python
  x = 0
  numbers = [1, 3, 5, 9]
  for i in numbers:
      if i > 2:
          x = x + 1
  print(x)
  ```

- What types can a pandas column be? Come up with at least three.
- What are some scenarios where you'd need to deal with types in pandas? Come up with at least three.
- How do you make a link in Markdown?
- How does `groupby()` work?
- What is resampling used for? Include an example.
- Why would you use an API?
- What's a choropleth map? Try explaining to someone who's never seen one before.
- What are the different kinds of merges? Can describe through text and/or visuals.
- How would you merge the following Dataframes? Write the code as best you can.

**`intros`**

| Name         | Year introduced |
| ------------ | --------------- |
| Mickey Mouse | 1928            |
| Big Bird     | 1969            |
| Lisa Simpson | 1987            |

**`shows`**

| First  | Last    | Series        |
| ------ | ------- | ------------- |
| Lisa   | Simpson | The Simpsons  |
| Mickey | Mouse   | multiple      |
| Big    | Bird    | Sesame Street |
