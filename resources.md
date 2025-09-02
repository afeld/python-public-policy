# Resources

There are countless blog posts, videos, books, etc. out there. There is no "best" resource, as individuals prefer different formats, come in with different experience, and learn at different speeds. Anything that comes up near the top of a Google search will likely be fine.

## Questions

- [Office hours](syllabus.md#instructor-information)
- [Stack Overflow](https://stackoverflow.com/)
- [Research Data Services](https://library.columbia.edu/services/research-data-services.html)


## Cheat sheets

- [Python Flash Cards](https://nostarch.com/pythonflashcards)
- pandas cheat sheets
   - [Official](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
   - [DataCamp](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python)
   - [DataQuest](https://www.dataquest.io/blog/pandas-cheat-sheet/)

## Tutorials

- [Crash Course Computer Science](https://thecrashcourse.com/topic/computerscience/)
- [FreeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/)
- [NYU's Quantitative Analysis Guide: Python](https://guides.nyu.edu/quant/python)
- [RealPython](https://realpython.com/tutorials/all/)

## Books

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Python for Data Analysis](https://wesmckinney.com/book/)
- [Python for MBAs](https://clio.columbia.edu/catalog/15536430) "and those in business roles that include coding or working with coding teams"

## Courses

- Related [Data Science for Policy (DSP) courses](https://www.sipa.columbia.edu/sipa-education/bulletin/dsp#dsp-requirements):
   - Applying Machine Learning — If interested, you should [take Computing in Context instead of Python for Public Policy](index.md#comparison-to-computing-in-context), as it's a prerequisite.
   - Intro to Text Analysis in Python
   - Introduction to Infographics and Data Visualization
   - Database Design, Management, and Security
   - Time Series Analysis

- [Free trials for online courses through the GitHub Student Developer Pack](https://education.github.com/pack?sort=popularity&tag=Learn#offers)

### Python fundamentals

- DataCamp's [Python Fundamentals](https://www.datacamp.com/tracks/python-fundamentals) or [Python Programmer](https://www.datacamp.com/tracks/python-programmer) tracks
- [Full Stack Python](https://www.fullstackpython.com/)
- [Python at Columbia Business School](https://academics.gsb.columbia.edu/python) self-paced course with videos, open to anyone at Columbia

### Data analysis/science


- [Data Analysis with Python for Excel Users](https://www.youtube.com/watch?v=WcDaZ67TVRo)
- freeCodeCamp's [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) class
- [IBM Data Analyst Course](https://www.youtube.com/watch?v=1PAy6d16ADQ) - can jump to specific parts

### Machine learning

- [Kaggle's Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
- [DataCamp's Natural Language Processing in Python track](https://www.datacamp.com/tracks/natural-language-processing-in-python)

## Workshops

- [Butler Studio](https://studio.cul.columbia.edu/)
- [Data Club](https://library.columbia.edu/services/research-data-services/data-club.html)
- [Foundations for Research Computing](https://rcfoundations.research.columbia.edu/)
- [Library Workshops](https://library.columbia.edu/using-libraries/workshops.html)
- [Research Data Services](https://library.columbia.edu/services/research-data-services.html)


## Learning more

Want to keep going with Python after this class? See [Developer Roadmaps](https://roadmap.sh/) for directions you can go. This course doesn't spend a lot of time on [Python fundamentals](#python-fundamentals), so it's recommended that you do that first.

Many "learn Python" resources will be web development-oriented — they will probably mention [Django](https://www.djangoproject.com/)/[Flask](https://flask.palletsprojects.com/). If you want to stay focused on data, you might want to look for ones that focus on [data science](#data-analysisscience) or [Python 3 generally](#python-fundamentals). See [Courses](#courses).

## Jupyter outside this course

We use [a cloud-based Jupyter environment (Google Colab)](lecture_0.ipynb#jupyter) for this course to avoid installation issues across student computers. This is the only environment that's supported for course work.



A non-exhaustive list of alternatives:

### Local

- [Anaconda Distribution](https://www.anaconda.com/download)
- [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

### Cloud-based

- [Anaconda Notebooks](https://www.anaconda.com/products/notebooks)
- [Google Cloud Vertex AI Notebooks](https://cloud.google.com/vertex-ai-notebooks)

- [Kaggle notebooks](https://www.kaggle.com/code)
- [Mode Notebooks](https://mode.com/help/articles/notebook)

### Matching the class environment

_Advanced_

Note these instructions won't work in Colab.

1. Install [Mamba](https://mamba.readthedocs.io/en/latest/index.html).
1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) [the repository](https://github.com/afeld/python-public-policy/tree/columbia).
1. Check out the `columbia` branch.
1. [Create the environment.](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) From this directory, run:

   ```sh
   mamba env create --file extras/environment.yml
   ```

1. Activate the environment:

   ```sh
   conda activate python-public-policy
   ```

1. Start the Jupyter server:

   ```sh
   make notebook
   ```

## See also

- [14 Principles of Open Government Data](https://opengovdata.io/2014/principles/)
- [Blog post about GitHub for non-developers](https://medium.com/nyc-planning-digital/git-what-extolling-githubs-virtues-to-non-coders-6cc11f1a5fd2)
- [Data Science Institute](https://datascience.columbia.edu/)
- [DataJournalism.com](https://datajournalism.com/)
- [GitHub Student Developer Pack](https://education.github.com/pack)
- [Generative AI offerings from the University](https://www.cuit.columbia.edu/content/ai-services)
