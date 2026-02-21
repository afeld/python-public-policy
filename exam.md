# Exam

The point of the exam is to ensure you were doing the following throughout the course:

- Paying attention
- Completing the assignments yourself (versus [copying-and-pasting from generative AI](syllabus.md#academic-integrity), etc.)

If both of those are the case, you will likely:

- Do well on the exam without a _huge_ amount of studying
- Finish before the time limit

## Format

- The exam will contain:
  - Fill-in-the-blank
  - Matching
  - Free response questions
    - Coding
      - The syntax isn't expected to be perfect.
    - High-level
- It will be done online (in-person, synchronously) through [{{exam_tool_name}}]({{exam_tool_docs}}).
  - To save time, installing this in advance is recommended.
- It will be "closed book", meaning no:
  - Web browsing
  - Apps
  - Cheat sheets
  - Phones
  - etc.

## Topics

The following is in scope for the exam:

- Python fundamentals
  - Types
  - Variables
  - Conditionals
  - Functions
- pandas data structures
- Jupyter concepts
- Markdown basics
- Data manipulation
  - Boolean indexing
  - Aggregation (count/sum/mean)
  - Grouping
  - Cleaning
  - Merging
- Troubleshooting
- Data visualization
  - Choosing chart types
  - Chart hygiene
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

- Why would you use an API?
- Suppose you have this JSON stored in a `candidates` variable. Write code to retrieve the name.

  ```json
  {
    "results": [{ "name": "Jimmy McMillan", "first_file_date": "2010-01-01" }]
  }
  ```
