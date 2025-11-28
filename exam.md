# Exam

The exam will contain fill-in-the-blank, matching, and free response questions, coding and high-level. It will be done on paper, closed-book (no cheat sheets, phones, laptops, etc).

## Topics

The exam will cover the following:

- Working with data using only the Python standard library ("pure Python")
- Python/pandas data types/structures
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

- What types can a pandas column be? Come up with at least three.
- What are some scenarios where you'd need to convert between Python/pandas types? Come up with at least three.
- How do you make a link in Markdown?
- How does `groupby()` work?
- What is resampling used for? Include an example.
- What's a kernel, in the context of this course?
- Write the equivalent of the following in pandas.

  ```python
  import csv

  lowest_gdp = None
  lowest_country = None

  with open("gdp.csv") as f:
     reader = csv.DictReader(f)
     for row in reader:
        gdp = float(row["GDP"])
        if lowest_gdp is None or gdp < lowest_gdp:
              lowest_gdp = gdp
              lowest_country = row["Country"]

  print(lowest_country)
  ```

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
