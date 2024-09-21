# Resources

## General

- [Office hours](syllabus.md#instructor-information)
- [Stack Overflow](https://stackoverflow.com/)
- [RealPython](https://realpython.com/tutorials/all/)
- [FreeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/)
- [Crash Course Computer Science](https://thecrashcourse.com/topic/computerscience/)
- [Data Analysis with Python for Excel Users](https://www.youtube.com/watch?v=WcDaZ67TVRo)
- [Python for MBAs]({{python_for_mbas}}) "and those in business roles that include coding or working with coding teams"
- [IBM Data Analyst Course](https://www.youtube.com/watch?v=1PAy6d16ADQ) - can jump to specific parts
- [Full Stack Python](https://www.fullstackpython.com/)
- [GitHub Student Developer Pack](https://education.github.com/pack)
  - Includes [learning resources](https://education.github.com/pack?sort=popularity&tag=Learn#offers) and various tools

{% if id == "columbia" -%}

## Columbia

- [Python at Columbia Business School](https://academics.gsb.columbia.edu/python) self-paced course with videos, open to anyone at Columbia
- [Foundations for Research Computing](https://rcfoundations.research.columbia.edu/)
- [Data Science Institute](https://datascience.columbia.edu/)
- Library
  - [Data Club](https://library.columbia.edu/services/research-data-services/data-club.html)
  - [Research Data Services](https://library.columbia.edu/services/research-data-services.html)
  - [Studio](https://studio.cul.columbia.edu/)

{% else -%}

## NYU

- [Wagner Quantitative Support](https://wagner.nyu.edu/portal/students/academics/advisement/quantitative)
  - Tutoring
  - Math Review
- [NYU Library Data Services](https://library.nyu.edu/departments/data-services/)
  - Consultation
  - Classes
- [The Coding Lab](https://codinglab.itp.io/)

{% endif -%}

## Pandas

- [Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- Cheat sheets
  - [Official](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
  - [DataCamp](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python)
  - [DataQuest](https://www.dataquest.io/blog/pandas-cheat-sheet/)
- [Python for Data Analysis book](https://wesmckinney.com/book/)
- [NYU's Quantitative Analysis Guide: Python](https://guides.nyu.edu/quant/python)

There are countless other blog posts, videos, books, etc. out there. There is no "best" resource, as individuals prefer different formats, come in with different experience, and learn at different speeds. Anything that comes up near the top of a Google search will likely be fine.

## Learning more

Want to keep going after this class?

### Python fundamentals

Recommended focusing on fundamentals of Python 3. Many "learn Python" resources will be web development-oriented (they will probably mention [Django](https://www.djangoproject.com/)/[Flask](https://flask.palletsprojects.com/)), so you might want to look for ones that focus on data science or Python 3 on its own. Some that are data-oriented:

- freeCodeCamp's [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) class
- DataCamp's [Python Fundamentals](https://www.datacamp.com/tracks/python-fundamentals) or [Python Programmer](https://www.datacamp.com/tracks/python-programmer) tracks

Countless other "learn Python" resources/courses/videos/books out there; there isn't one right choice for everyone.

### Machine learning

- [Kaggle's Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
- [DataCamp's Natural Language Processing in Python track](https://www.datacamp.com/tracks/natural-language-processing-in-python)

{% if school_slug == "columbia" -%}

### Columbia

- [Other Data Analytics & Quantitative Analysis (DAQA) courses](https://bulletin.columbia.edu/sipa/specializations/daqa/#coursestext)
- [Library Workshops](https://library.columbia.edu/using-libraries/workshops.html)

{% else -%}

### NYU

- Wagner
  - [Data Science and Data Management](https://wagner.nyu.edu/focus/areas/data-science-data-management)
  - [Pre-approved courses outside of Wagner (for Wagner students)](https://wagner.nyu.edu/portal/students/academics/courses/non-wagner-courses)
- [Center for Data Science](https://cds.nyu.edu/masters-curriculum/)
- [Center for Urban Science + Progress (CUSP)](https://cusp.nyu.edu/masters-degree/#curriculum)
  - Applied Data Science
  - Machine Learning for Cities

{% endif -%}

## Jupyter outside this course

We use [a cloud-based Jupyter environment ({{coding_env_name}})](lecture_0.ipynb#jupyter) for this course to avoid installation issues across student computers. This is the only environment that's supported for course work.

{% if id == "columbia" -%}
Some additional options for running Jupyter:
{% else -%}
After this class, however, you'll no longer have access. To download the files:

1. Open a notebook
1. In a code cell, run `!tar -czvf ~/python_files.tar.gz ~`
1. From [the file browser](https://padmgp-4506-fall.rcnyu.org/user-redirect/tree), check the box next to `python_files.tar.gz`, then click `Download`
1. On your computer, unzip the file.
   - On Windows, you may need to install [7-Zip](https://www.7-zip.org/) to do so.

Some options for running Jupyter on your own:

- [Google Colab](https://colab.research.google.com/)
{% endif -%}
- [Anaconda](https://www.anaconda.com/)
- [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

### Matching the class environment

_Advanced_

Note these instructions won't work in Colab.

1. Install [Mamba](https://mamba.readthedocs.io/en/latest/index.html).
1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) [the repository](https://github.com/afeld/python-public-policy/tree/{{school_slug}}).
1. Add the following to your `.git/config` file:

    ```
    # based on https://stackoverflow.com/a/73218382/358804
    [filter "strip-notebook-execution"]
    	clean = "jupyter nbconvert --Exporter.preprocessors=extras.lib.clear_execution.ClearExecutionPreprocessor --to=notebook --stdin --stdout --log-level=ERROR"
    ```

1. Check out the `{{school_slug}}` branch.
1. [Create the environment.](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) From this directory, run:

   ```sh
   mamba env create --file extras/environment.lock.yml
   ```

1. Activate the environment:

   ```sh
   conda activate python-public-policy
   ```

1. Start the Jupyter server:

   ```sh
   ./extras/scripts/start.sh
   ```

## See also

- [14 Principles of Open Government Data](https://opengovdata.io/2014/principles/)
- [Blog post about GitHub for non-developers](https://medium.com/nyc-planning-digital/git-what-extolling-githubs-virtues-to-non-coders-6cc11f1a5fd2)
- [DataJournalism.com](https://datajournalism.com/)
