# General assignment information

- [Due dates](syllabus.md#schedule)
- [Scoring](syllabus.md#assignment-scoring)
- [Open-ended assignment info](assignments/open_ended.md)

## Getting started

To edit/execute a Homework/lecture notebook:

1. Open the page for the Homework/Lecture on this site.
   - For example: [Homework 0](hw_0.ipynb)
1. Click the launch button (🚀) at the top.
   - JupyterHub may take a few minutes to start up.
1. You should now see the notebook in JupyterHub.
That is now your own copy; make edits in there directly.

### [Open-ended assignments](assignments/open_ended.md)

You'll create your own notebook, using `Python [conda env:python-public-policy]` as the kernel.

## Tips

- **Read the instructions carefully.** Like word problems from math class, they are very specific in what they are asking for.
- **Ask for help.**
   - The assignments are meant to be challenging, not impossible.
   - Try and work through problems on your own to start. If you are stuck for more than a half hour, [step away](https://dankim.org/posts/cant-crack-that-programming-problem/). If you _still_ can't figure it out, ask for help.
      - [Ed](https://brightspace.nyu.edu/d2l/le/lessons/432695/topics/11040123)
      - [Office hours](https://python-public-policy.afeld.me/en/nyu/syllabus.html#instructor-information)

### Coding in general

- Make variable names descriptive.
   - Do as I say, not as I do!
- Only do one thing per line.
   - Makes troubleshooting easier
- **Spot check your results.** If you are transforming data from a previous Step, compare the results, do a handful of the calculations manually, etc. to ensure that the results are correct.
- **[Don't repeat yourself (DRY).](https://dzone.com/articles/is-your-code-dry-or-wet)** If you find yourself copying and pasting code within your file(s), there's probably a better way to do it.
- **Avoid [hard-coding](https://www.quora.com/What-does-hard-coded-something-mean-in-computer-programming-context) values.** Don't rely on things like row numbers or column order being stable, in case the dataset were to be updated.

### Jupyter / JupyterHub

- **All lecture slides and homework templates can be found under [`python-public-policy/`](https://padmgp-4506-spring.rcnyu.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fafeld%2Fpython-public-policy&urlpath=tree%2Fpython-public-policy%2F&branch=nyu).** The contents of this directory will be automatically updated from [the GitHub repository](https://github.com/afeld/python-public-policy/tree/nyu), but should keep any changes you make.
   - FYI that this uses [nbgitpuller](https://nbgitpuller.readthedocs.io/) under the hood.
- **Access [JupyterHub](https://padmgp-4506-spring.rcnyu.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fafeld%2Fpython-public-policy&urlpath=tree%2Fpython-public-policy%2F&branch=nyu) via the links on this site** rather than bookmarking JupyterHub, as that will pull down the latest changes.
- Keep each cell to only a few lines of code.
   - Allows/encourages you to output intermediate results, ensuring that everything is working as expected.
- You are always welcome to **add cells**. You probably don't want more than a few lines of code in each. This makes the spot checking of intermediate results easier.
- Make notebooks [idempotent](https://en.wikipedia.org/wiki/Idempotence)
   - Makes your work reproducible.
   - Use `Restart and run all` (⏩ button in toolbar).

## Submission

1. Ensure all the outputs are visible and the notebook is cleaned up.
   - This is a good time to run the notebook end-to-end with `Restart and run all` (⏩).
   - See [general scoring criteria](syllabus.md#assignment-scoring).
1. Ensure the notebook doesn't contain any sensitive information. (Only really applicable to [open-ended assignments](assignments/open_ended.md).)
   - API keys
   - Personally-identifiable information (PII)
1. Export the files.
   - `.ipynb`:
      1. `File`
      1. `Download`
   - `.py`:
      1. `File`
      1. `Save and Export Notebook As`
      1. `Executable Script`
         - You may need to [allow popups](https://support.google.com/chrome/answer/95472).
1. Submit.
   1. In [Brightspace](https://brightspace.nyu.edu/d2l/home/432695), go to `Content`.
      - Note that this is _not_ the `Assignments` tab of Brightspace.
   1. [Go to Gradescope.](https://brightspace.nyu.edu/d2l/le/lessons/432695/topics/11563092)
   1. [Upload both the `.ipynb` and `.py` files to the Assignment.](https://guides.gradescope.com/hc/en-us/articles/21865616724749-Submitting-a-Code-assignment)

Note [the Final Project submission](final_project.md#submission) is slightly different.

### Notes

- You can ignore Gradescope saying "Large file hidden". The grader can download the notebook to view.
- [Resubmissions](syllabus.md#resubmission) are done the same way.
- In-class exercises will not be submitted/graded.

## Common issues

- **`Error: Command '['git', 'diff', '..origin/nyu', '--name-status']' returned non-zero exit status 128` when trying to launch JupyterHub:** Something got corrupted in your copy of the files that come through [`nbgitpuller`](https://nbgitpuller.readthedocs.io/). Easiest thing is to move the existing ones and restart with a fresh copy.
   1. [Launch JupyterHub.](https://padmgp-4506-spring.rcnyu.org)
   1. There should be a `python-public-policy` folder. Rename it, something like `python-public-policy-old`.
      - If you've edited any of the template notebooks, you can find them in that `-old` folder.
   1. Repeat the [getting started](#getting-started) steps.
- **When using [`choropleth()`](https://plotly.com/python/choropleth-maps/)/[`choropleth_map()`](https://plotly.com/python/tile-county-choropleth/), nothing appears on the map:** Make sure:
   - Your `locations` corresponds to the DataFrame column name and `featureidkey` is set to `properties.<property name>` matching the GeoJSON
      - See [how we found the property name to use](lecture_3.ipynb#geospatial-data)
   - The column and the GeoJSON properties have values that match
- **`SettingWithCopyWarning`:** [How to fix](https://www.dataquest.io/blog/settingwithcopywarning/)
- **`input()` stuck:** Jupyter can be a bit buggy when dealing with interactive input. If it seems to get stuck or you aren't seeing a prompt when you'd expect one, try clicking the `Kernel` menu then `Restart Kernel`.
- **The values are out of order along the axis of a Plotly chart:** Make sure that:
   - The values are integers/floats/[timestamps](https://plotly.com/python/line-charts/#line-plots-on-date-axes), not strings, where applicable.
   - [Line charts: The column used for the X axis is sorted.](https://plotly.com/python/line-charts/#data-order-in-line-charts)
- **`AttributeError: partially initialized module 'orjson' has no attribute 'OPT_NON_STR_KEYS'`:** Add the following cell before your other Plotly code, then `Restart and run all` (⏩).

   ```python
   import plotly.io

   plotly.io.json.config.default_engine = 'json'
   ```

### Disk full

If you get an error of `Disk is full` / `No space left on device` / `Out of diskspace`: You've used all the [available disk space](assignments/open_ended.md#limits). If you do fill it up, your server may not be able to start again (`spawn failed`). You'll need to delete one or more large files that you don't need anymore:

1. If you server is started already (you're seeing notebooks), click `Control Panel` -> `Stop My Server`.
1. Go to [start your server again](https://padmgp-4506-spring.rcnyu.org).
1. Select `Troubleshooting Only - Clear Disk`.
1. Look at the `File size` Jupyter shows in the file browser.
1. Delete one or more large files.
1. If you're still using those datasets, [make them smaller](assignments/open_ended.md#reducing-data-size).

### `Error loading notebook`

This error can happen if you tried to output a lot of data in tables/charts. Steps to resolve:

1. Open the [JupyterHub](https://padmgp-4506-spring.rcnyu.org)) file browser
1. Click `New`, then `Terminal`
1. Run the following, changing the [path](https://www.codecademy.com/resources/docs/general/file-paths) at the end to match whatever notebook needs to be repaired:

   ```sh
   jupyter nbconvert --to notebook --clear-output ~/python-public-policy/hw_<NUMBER>.ipynb
   ```

If you're confused by these instrucions, download the notebook file and [email to the instructor](syllabus.md#instructor-information).

### Kernel and memory issues

The kernel is [the place where Python is installed and the code is actually executing](https://docs.jupyter.org/en/stable/projects/kernels.html#kernels), in the cloud somewhere.

- Make sure `Python [conda env:python-public-policy]` is selected as the kernel.
   - Shows in the top right of the notebook interface
   - To change:
      1. Open the `Kernel` menu.
      1. Click `Change kernel`.
      1. Click `Python [conda env:python-public-policy]`.
- If your kernel is repeatedly crashing, you're probably running out of memory.
   - Make sure you aren't loading data sets you don't need.
   - If loading a new dataset, [make it smaller](assignments/open_ended.md#reducing-data-size)
   
   - Close kernels you aren't using from the [Running](https://padmgp-4506-spring.rcnyu.org/user-redirect/tree#running) page.
