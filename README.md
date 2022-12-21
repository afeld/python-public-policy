# Python Coding for Public Policy

[![Execute notebooks](https://github.com/afeld/python-public-policy/actions/workflows/main.yml/badge.svg)](https://github.com/afeld/python-public-policy/actions/workflows/main.yml?query=branch%3Amain) [![Documentation Status](https://readthedocs.org/projects/python-coding-for-public-policy/badge/?version=latest)](https://python-public-policy.afeld.me/en/latest/?badge=latest)

**Alternate course title:** _How to Use a Bit of Code to Do Things That Would Be Really Hard in Spreadsheets_

This repository contains content for [NYU Wagner's Python Coding for Public Policy](https://wagner.nyu.edu/education/courses/python-coding-for-public-policy) class (PADM-GP 4506).

The materials are also available for public consumption. If you are _not_ part of the class, see information about [running the notebooks locally](#jupyter-beyond-jupyterhub).

## Important links

- [Syllabus](syllabus.md)
- [Brightspace site](https://brightspace.nyu.edu/d2l/home/206261), which students will use for:
  - Viewing Announcements
  - Submitting Assignments
  - Viewing grades
- [JupyterHub](https://padmgp-4506001-fall.rcnyu.org/user-redirect/notebooks/class_materials/), where work will be completed

Produced and taught by Aidan Feldman. Largely based on [previous iteration by Hannah Kates](https://github.com/hannahkates/nyu-python-public-policy).

## Why this class?

There are countless resources out there to learn Python and pandas — books, videos, etc. — and many are free. Relative to other Python/pandas courses, this class:

- Doesn't expect any prior technical experience
- Puts the data/code in a public policy context
  - There's a specific emphasis on learning coding for data analysis rather than software engineering
- Teaches you how to work with open data
- Optimizes for minimal setup

All the lectures and assignment templates are in this repository, so you _could_ go through them on your own. The benefits of enrolling are:

- Additional content
  - You get access to lectures, which includes commentary that isn't in this repository
  - You get access to assignment solutions
- Support
  - There is an instructor to answer questions, both during and between lectures
  - You have peers you can work with
- You invest money and are expected to show up to class and turn in assignments on time, which [makes it far more likely you will complete it](https://mashable.com/2014/12/16/warning-college-may-be-a-waste-of-your-time-and-money/)

## Assignments

### Tips

- **All lecture slides and homework templates can be found under [`class_materials/`](https://padmgp-4506001-fall.rcnyu.org/user-redirect/notebooks/class_materials/).** The contents of this directory will be automatically updated from [the GitHub repository](https://github.com/afeld/python-public-policy), but should keep any changes you make.
- **Look at the Table of Contents** to get an overview. You can find the Table of Contents button in the sidebar.
- **Read the instructions carefully.** Like word problems from math class, they are very specific in what they are asking for.
- **Spot check your results.** If you are transforming data from a previous Step, compare the results, do a handful of the calculations manually, etc. to ensure that the results are correct.
- **[Don't repeat yourself (DRY).](https://dzone.com/articles/is-your-code-dry-or-wet)** If you find yourself copying and pasting code within a notebook, there's probably a better way to do it.
- **Avoid [hard-coding](https://www.quora.com/What-does-hard-coded-something-mean-in-computer-programming-context) values.** Don't rely on things like row numbers or column order being stable, in case the dataset were to be updated.

### Common issues

- **PDF export:**

  - **Plotly charts/maps not appearing:** Include the [boilerplate](https://whynameitthat.blogspot.com/2013/10/boiler-plate.html) codeL

    ```python
    import plotly.io as pio
    pio.renderers.default = "notebook_connected+pdf"
    ```

  - **500 error:** You may be outputting too much data. Try reducing your output (in the Jupyter sense) to smaller subsets.

- **`Disk is full` / `No space left on device`:** Your workspace in JupyterHub has a limit of 1GB (a.k.a 1,000 MB or 1,000,000 KB) across all your files. Jupyter shows the `File size` of each in the file browser. Try deleting some larger files that you don't need anymore.
- **Nothing appearing with `choropleth_mapbox()`:** See [troubleshooting suggestions](lecture_3.html#troubleshooting)

#### Kernel/memory issues

- Make sure `Python [conda env:python-public-policy]` is selected as the kernel.
  - Shows in the top right of the notebook interface
  - Change from `Kernel` menu → `Change kernel` → `Python [conda env:python-public-policy]`
- If your kernel is repeatedly crashing, you're probably running out of memory.
  - Make sure you aren't loading data sets you don't need.
  - Close kernels you aren't using from the [Running](https://padmgp-4506001-fall.rcnyu.org/user-redirect/tree#running) page.

### Turning in assignments

1. Ensure all the outputs are visible and the notebook is cleaned up.
   - What you see is what the instructors will see.
   - This is a good time to run the notebook end-to-end with ⏩ (`Restart and run all`).
   - See [general scoring criteria](syllabus.html#assignments).
1. Leave your name off the notebook filename and the notebook itself, as assignments are graded anonymously.
1. Export the notebook as a PDF. From the Jupyter interface, go to:
   1. `File`
   1. `Download as`
   1. `PDF via LaTeX (PDF)`
1. Glance through the PDF to ensure everything is showing up as you intend.
1. Upload the PDF to the Brightspace Assignment.

After the resubmission deadline passes for each Assignment, the solutions will be posted in [`shared/solutions/`](https://padmgp-4506001-fall.rcnyu.org/user-redirect/tree/shared/solutions/).

Note: In-class exercises will not be graded.

## Resources

- [Office hours](syllabus.html#instructor-information)
- [Wagner Quantitative Support](https://wagner.nyu.edu/portal/students/academics/advisement/quantitative)
  - Tutoring
  - Math Review
- [NYU Library Data Services](https://library.nyu.edu/departments/data-services/)
  - Consultation
  - Classes
- [Stack Overflow](https://stackoverflow.com/)
- [GitHub Student Developer Pack](https://education.github.com/pack)
  - Includes [learning resources](https://education.github.com/pack?sort=popularity&tag=Learn#offers) and various tools

### Pandas

- [Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- Cheat sheets
  - [Official](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
  - [DataCamp](https://datacamp-community-prod.s3.amazonaws.com/dbed353d-2757-4617-8206-8767ab379ab3)
  - [DataQuest](https://www.dataquest.io/blog/pandas-cheat-sheet/)
- [Python for Data Analysis book](https://bobcat.library.nyu.edu/permalink/f/ci13eu/nyu_aleph003900267)
- NYU's [Quantitative Analysis Guide: Python](https://guides.nyu.edu/quant/python)

There are countless other blog posts, videos, books, etc. out there. There is no "best" resource, as individuals prefer different formats, come in with different experience, and learn at different speeds. Anything that comes up near the top of a Google search will likely be fine.

## Learning more

Want to keep going after this class?

### Python fundamentals

Recommended focusing on fundamentals of Python 3. Many "learn Python" resources will be web development-oriented (they will probably mention [Django](https://www.djangoproject.com/)/[Flask](https://flask.palletsprojects.com/)), so you might want to look for ones that focus on data science or Python 3 on its own. Some that are data-oriented:

- DataCamp's [Python Fundamentals](https://www.datacamp.com/tracks/python-fundamentals) or [Python Programmer](https://www.datacamp.com/tracks/python-programmer) tracks
- [Kaggle's Learn Python tutorials](https://www.kaggle.com/learn/python)

Countless other "learn Python" resources/courses/videos/books out there; there isn't one right choice for everyone.

### Machine learning

- [Kaggle's Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
- [DataCamp's Natural Language Processing in Python track](https://www.datacamp.com/tracks/natural-language-processing-in-python)

### NYU

- [Wagner Data Science and Data Management](https://wagner.nyu.edu/focus/areas/data-science-data-management)
- [Center for Urban Science + Progress (CUSP)](https://cusp.nyu.edu/masters-degree/#curriculum)
  - Applied Data Science
  - Machine Learning for Cities

## See also

- [14 Principles of Open Government Data](https://opengovdata.io/2014/principles/)
- [Blog post about GitHub for non-developers](https://medium.com/nyc-planning-digital/git-what-extolling-githubs-virtues-to-non-coders-6cc11f1a5fd2)
- [DataJournalism.com](https://datajournalism.com/)

## Testimonials

> This class has been extremely helpful and my only regret is that I didn't take it sooner in my NYU career. … In fact, I've already put python to use for my final thesis. … In writing my thesis, I used python for descriptive statistics that would have otherwise taken much longer in excel … Writing code for these analysis probably saved me about a day or two of work.

---

> Thank you for an incredible semester. I truly took away a lot that I feel will help me dive deeper into a career in public service, while having unique skills that will help me deliver a much greater impact into the communities I'm serving.

---

> The in-class assignments and homework provided many opportunities to practice the Python concepts we learned in class. … Professor Feldman was able to present difficult concepts in a way that was easy to digest as someone who knew very little about Python prior to this course. This course achieved its goal of removing the uneasiness I felt towards Python and coding in general, and for a 7-week course, that is no easy feat!

---

> Everything controllable by the professor was fantastic. The objectives were straightforward and value-added. The professor helped make sure that we were coming away from assignments with real tangible understanding of the code rather than focusing on completion. I was challenged, but the professor was always around to answer questions.

---

From [Tess Edwards](https://www.linkedin.com/in/tess-edwards/):

> Though I've only been in Python class for less than a month, I've already learned so much that has empowered me beyond the classroom. Since I was an intern in 2017, the office of Congresswoman Kathleen Rice (formerly D4-NY) has contacted me annually to judge submissions for the "Congressional App Challenge". This challenge invites high school students to create apps and showcase their coding skills. Historically, I've graded these as an outsider with very little understanding for coding languages like Python (they knew that by the way!). However, this year is different. I am grading the submissions from a brand new perspective that is empowering and definitely making me a better judge. I'm so excited to be learning a skill that has already shown to be fruitful in such an unexpected way!

## Jupyter beyond JupyterHub

We use [a cloud-based JupyterHub environment](lecture_0.html#jupyter) for this course to avoid installation issues across student computers. This is the only environment that's supported by the instructor/grader for course work.

After this class, however, you'll no longer have access to the class JupyterHub. Some options for running Jupyter on your own:

- [Google Colab](https://colab.research.google.com/)
- [Anaconda](https://www.anaconda.com/)
- [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

### Matching the class environment

_Advanced_

Note these instructions won't work in Colab.

1. [Install Mamba.](https://mamba.readthedocs.io/en/latest/installation.html)
1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) [the repository](https://github.com/afeld/python-public-policy).
1. [Create the environment.](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) From this directory, run:

   ```sh
   mamba env create --file extras/environment.yml
   ```

1. Activate the environment:

   ```sh
   conda activate python-public-policy
   ```

1. Start the Jupyter server:

   ```sh
   jupyter notebook
   ```
