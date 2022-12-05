# Resources

## General

- [Office hours](syllabus.html#instructor-information)
- [Stack Overflow](https://stackoverflow.com/)
- [GitHub Student Developer Pack](https://education.github.com/pack)
  - Includes [learning resources](https://education.github.com/pack?sort=popularity&tag=Learn#offers) and various tools

{% if id == "nyu" -%}

## NYU

- [Wagner Quantitative Support](https://wagner.nyu.edu/portal/students/academics/advisement/quantitative)
  - Tutoring
  - Math Review
- [NYU Library Data Services](https://library.nyu.edu/departments/data-services/)
  - Consultation
  - Classes

{% endif -%}

## Pandas

- [Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- Cheat sheets
  - [Official](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
  - [DataCamp](https://datacamp-community-prod.s3.amazonaws.com/dbed353d-2757-4617-8206-8767ab379ab3)
  - [DataQuest](https://www.dataquest.io/blog/pandas-cheat-sheet/)
- [Python for Data Analysis book](https://wesmckinney.com/book/)
- [NYU's Quantitative Analysis Guide: Python](https://guides.nyu.edu/quant/python)

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

{% if school_slug == "columbia" -%}

### Columbia

- [Other Data Analytics & Quantitative Analysis (DAQA) courses](https://bulletin.columbia.edu/sipa/specializations/daqa/#coursestext)

{% else -%}

### NYU

- [Wagner Data Science and Data Management](https://wagner.nyu.edu/focus/areas/data-science-data-management)
- [Center for Urban Science + Progress (CUSP)](https://cusp.nyu.edu/masters-degree/#curriculum)
  - Applied Data Science
  - Machine Learning for Cities

{% endif -%}

## Jupyter beyond JupyterHub

We use [a cloud-based JupyterHub environment](lecture_0.html#jupyter) for this course to avoid installation issues across student computers. This is the only environment that's supported for course work.

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

1. Install Python dependencies used in notebooks:

   ```sh
   pip install -r extras/requirements.txt
   ```

1. Start the Jupyter server:

   ```sh
   jupyter notebook
   ```

## See also

- [14 Principles of Open Government Data](https://opengovdata.io/2014/principles/)
- [Blog post about GitHub for non-developers](https://medium.com/nyc-planning-digital/git-what-extolling-githubs-virtues-to-non-coders-6cc11f1a5fd2)
- [DataJournalism.com](https://datajournalism.com/)
