# **NYU Wagner - Python Coding for Public Policy**

# Class 0: Intro to coding

## Welcome!

![Elmo waving](https://media.giphy.com/media/LPgFwCQg4HQBvPihcn/source.gif)

### Introductions

In the Zoom meeting chat, share the following:

- Name (what you go by)
- What you're studying
- Go-to quarantine snack

### A bit more about me

- Coding since 2005 🖥
- Government since 2014 🦅
- Also a modern dancer 💃 cyclist 🚲 and baker 🍞
- Passionate about open source
- Run a meetup called [Hacker Hours](https://hackerhours.org/) for people learning to code

### Day jobs

- **Current:** Technology Director at [TTS](https://www.gsa.gov/about-us/organization/federal-acquisition-service/technology-transformation-services)
- **Past** include:
  - [Census xD](https://www.xd.gov/)
  - [NYC Planning Labs](https://labs.planning.nyc.gov/)
  - GitHub
  - [18F](https://18f.gsa.gov)

### Repository walkthrough

- [Homepage](https://github.com/afeld/nyu-python-public-policy)
- [Syllabus](https://github.com/afeld/nyu-python-public-policy/blob/master/syllabus.md#readme)

### Disclaimers

- You are not going to be good at coding by the end of this class
- I am here to teach you to:
  - Understand the power of code
  - Not be afraid of code
  - Troubleshoot
  - Google stuff
- Not a statistician
- This class came together in two weeks
  - Rough around the edges
  - Subject to change
  - Ask for your patience

## Spreadsheets vs. programming languages

### Why spreadsheets

- The easy stuff is easy
- Lots of people know how to use them
- Mostly just have to point, click, and scroll
- Data and logic live together as one

### Why programming languages

- Data and logic _don't_ live together
  - Why might this matter?
- More powerful, flexible, and expressive than spreadsheet formulas

  - Don't have to cram into a single line

    ```
    =SUM(INDEX(C3:E9,MATCH(B13,C3:C9,0),MATCH(B14,C3:E3,0)))
    ```

  - Can have more descriptive data references than `Sheet1!A:A`

- Better at working with large data
  - Google Sheets and Excel have hard limits at 1-5 million rows, but get slow long before that
- Reusable code (packages)
- Automation

### Side-by-side\*

|                       Task |  Spreadsheets  | Programming languages |
| -------------------------: | :------------: | :-------------------: |
|           **Loading data** |      Easy      |        Medium         |
|           **Viewing data** |      Easy      |        Medium         |
|         **Filtering data** |      Easy      |        Medium         |
|      **Manipulating data** |     Medium     |        Medium         |
|           **Joining data** |      Hard      |        Medium         |
| **Complicated transforms** | Impossible\*\* |        Medium         |
|             **Automation** | Impossible\*\* |        Medium         |
|        **Making reusable** | Impossible\*\* |        Medium         |
|         **Large datasets** |   Impossible   |         Hard          |

_\*Ratings are obviously somewhat subjective._

_\*\*Not including scripting._

## Python vs. other languages

- Good for general-purpose _and_ data stuff
- Widely used in both industry and academia
- Relatively easy to learn
- Open source

![Python logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/110px-Python-logo-notext.svg.png)
