# Quizzes

_This course used to have an exam. They have been replaced by multiple quizzes._

[There are several quizzes througout the course.](syllabus.md#schedule) They are in place to ensure you are doing the following throughout the course:

- Paying attention
- Completing the assignments yourself (versus [copying-and-pasting from generative AI, etc.](syllabus.md#academic-integrity))

If both of those are the case, you will likely do well on the quizzes without additional studying. The quizzes are intended to be completed in under 15 minutes.

## Format

- Each quiz will contain some combination of:
  - Fill-in-the-blank
  - Matching
  - Free response questions
    - Coding
      - The syntax isn't expected to be perfect.
    - High-level
- They will be "closed book", meaning no:
  - Web browsing
  - Apps
  - Cheat sheets
  - Phones
  - etc.
- They will be done online (in-person, synchronously) through [Respondus LockDown Browser](https://support.nyu.edu/esc?id=kb_article&sysparm_article=KB0011343).
  - This is being used to prevent access to other tabs/apps.
  - While the tool _can_ be used to collect location, video, etc., this is disabled.
  - You only need this during the quizzes; it can be uninstalled outside of that time.

## Topics

The quizzes cover everything from the lectures and assignments due prior to that quiz. In other words, they have the following scopes.

### Quiz 0

- Python fundamentals
  - Types
  - Variables
  - Conditionals
  - Loops
- Jupyter concepts

#### Example questions

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

### Quiz 1

Everything above, plus:

- Functions
- pandas data structures
- Data manipulation
  - Boolean indexing
  - Aggregation (count/sum/mean)
  - Grouping
  - Cleaning
  - Merging
- Troubleshooting
- Markdown basics

#### Example questions

- What types can a pandas column be? Come up with at least three.
- What are some scenarios where you'd need to deal with types in pandas? Come up with at least three.
- How do you make a link in Markdown?
- How does `groupby()` work?
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

### Quiz 2

Everything above, plus:

- Reshaping
- Data visualization
  - Choosing chart types
  - Chart hygiene
- Time series
  - Resampling
  <!-- - APIs, conceptually -->

#### Example questions

- What is resampling used for? Include an example.
- What's a choropleth map? Try explaining to someone who's never seen one before.
<!-- - Why would you use an API?
- Suppose you have this JSON stored in a `candidates` variable. Write code to retrieve the name.

  ```json
  {
    "results": [{ "name": "Jimmy McMillan", "first_file_date": "2010-01-01" }]
  }
  ``` -->
