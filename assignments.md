# General assignment information

- [Due dates](syllabus.md#schedule)
- [Scoring](syllabus.md#assignment-scoring)

## Getting started

To edit/execute a Homework/lecture notebook:

1. Open the page for the Homework/Lecture on this site.
   - For example: [Homework 0](hw_0.ipynb)
1. Click the launch button (🚀) at the top.
   - JupyterHub may take a few minutes to start up.
1. You should now see the notebook in JupyterHub.
That is now your own copy; make edits in there directly.

## Tips

- **All lecture slides and homework templates can be found under [`python-public-policy/`](https://padmgp-4506-fall.rcnyu.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fafeld%2Fpython-public-policy&urlpath=tree%2Fpython-public-policy%2F&branch=nyu).** The contents of this directory will be automatically updated from [the GitHub repository](https://github.com/afeld/python-public-policy/tree/nyu), but should keep any changes you make.
- **Access [JupyterHub](https://padmgp-4506-fall.rcnyu.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fafeld%2Fpython-public-policy&urlpath=tree%2Fpython-public-policy%2F&branch=nyu) via the links on this site** rather than bookmarking JupyterHub, as that will pull down the latest changes.
- **Read the instructions carefully.** Like word problems from math class, they are very specific in what they are asking for.
- **Spot check your results.** If you are transforming data from a previous Step, compare the results, do a handful of the calculations manually, etc. to ensure that the results are correct.
- You are always welcome to **add cells**. You probably don't want more than a few lines of code in each. This makes the spot checking of intermediate results easier.
- **[Don't repeat yourself (DRY).](https://dzone.com/articles/is-your-code-dry-or-wet)** If you find yourself copying and pasting code within a notebook, there's probably a better way to do it.
- **Avoid [hard-coding](https://www.quora.com/What-does-hard-coded-something-mean-in-computer-programming-context) values.** Don't rely on things like row numbers or column order being stable, in case the dataset were to be updated.

### Generative AI

_See also: [course generative AI policy](syllabus.md#generative-ai)._

We will be using the AI "magic" (command). Documentation:

- [NYU-specific](https://sites.google.com/nyu.edu/rit-genai/use-build/rit-jupyterhub#h.r3bhgpidqt5o)
- [General](https://jupyter-ai.readthedocs.io/en/latest/index.html)

#### Usage

1. Open [JupyterHub](https://padmgp-4506-fall.rcnyu.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fafeld%2Fpython-public-policy&urlpath=tree%2Fpython-public-policy%2F&branch=nyu).
1. Create a new notebook using the `Python [conda env:base]` kernel.
   - We will only use this kernel for AI; [all other notebooks should use `Python [conda env:python-public-policy]`](#kernel-and-memory-issues).
1. Load the models by running the following in a `Code` cell:

   ```
   %load_ext rit_jupyter_ai_magics
   ```

1. In another cell, run:

   ```
   %%ai gpt-4.0-32k
   how are you?
   ```

1. Replace `how are you?` with your prompt. You can repeat that cell as many times as you need.

### Storing data

1. Open the [JupyterHub file browser](https://padmgp-4506-fall.rcnyu.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fafeld%2Fpython-public-policy&urlpath=tree%2Fpython-public-policy%2F&branch=nyu).
1. Navigate to the folder your notebook is in.
1. [Upload the data.](https://tljh.jupyter.org/en/latest/howto/content/add-data.html#adding-data-from-your-local-machine)
1. From Python, use `read_csv("./<filename>.csv")`.

Note that that file path should be to relative to the notebook within JupyterHub — `./` means "in the same directory". JupyterHub cannot access the file on your local machine; in other words, the path shouldn't start with `C:\\` or anything like that. [More info about file paths](https://www.codecademy.com/resources/docs/general/file-paths)

### Limits

JupyterHub has a disk storage limit of 1GB (a.k.a. 1,024 MB or 1,048,576 KB) across all your files, and a memory limit of 3GB.

### Reducing data size

You can make data smaller _before_ uploading by filtering it through:

- The data portal, if it supports it
  - [Instructions for Socrata-based portals](https://support.socrata.com/hc/en-us/articles/202950808-Creating-a-Filtered-View)
- In a spreadsheet program
- For the [NYC Open Data Portal](https://opendata.cityofnewyork.us/), though [the shortener widget](shorten.md)

## Submission

1. Ensure all the outputs are visible and the notebook is cleaned up.
   - This is a good time to run the notebook end-to-end with `Restart and run all` (⏩).
   - See [general scoring criteria](syllabus.md#assignment-scoring).
1. Export the notebook as a PDF. From the Jupyter interface, go to:
   1. `File`
   1. `Save and Export Notebook As…`
   1. `PDF`
   1. You may need to [allow popups](https://support.google.com/chrome/answer/95472)
1. Glance through the PDF to ensure everything is showing up as you intend.
   - In particular, check your visualizations.
   - What you see is what the instructors will see.
1. **If one of the Homeworks:** Upload the PDF to the Brightspace Assignment.
1. **If the Final Project:**
   1. In [Brightspace](https://brightspace.nyu.edu/d2l/home/384630), go to `Content`, then `Final Project`. You should see the TurnItIn/PeerMark dashboard.
   1. Follow [these instructions](https://help.turnitin.com/feedback-studio/d2l/LTI13/student/submitting-a-paper/submitting-a-paper.htm) to upload the PDF.
1. **If you [used generative AI](#generative-ai):** Repeat the previous steps to also turn in the notebook with your interactions.

When you're ready to have it formally re-graded, please resubmit through the same Assignment in Brightspace.

Note: In-class exercises will not be graded.

## Common issues

- **`Error: Command '['git', 'diff', '..origin/nyu', '--name-status']' returned non-zero exit status 128` when trying to launch JupyterHub:** Something got corrupted in your copy of the files that come through [`nbgitpuller`](https://nbgitpuller.readthedocs.io/). Easiest thing is to move the existing ones and restart with a fresh copy.
  1. [Launch JupyterHub.](https://padmgp-4506-fall.rcnyu.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fafeld%2Fpython-public-policy&urlpath=tree%2Fpython-public-policy%2F&branch=nyu)
  1. There should be a `python-public-policy` folder. Rename it, something like `python-public-policy-old`.
    - If you've edited any of the template notebooks, you can find them in that `-old` folder.
  1. Repeat the [getting started](#getting-started) steps.
- **PDF export:**
  - **500 error:** You may be outputting too much data. Try reducing your output (in the Jupyter sense) to smaller subsets. This can include:
    - Not displaying so many rows/values
    - Reducing the number of points that are plotted
- **When using `choropleth_mapbox()`, nothing appears on the map:** Make sure:
  - Your `locations` corresponds to the DataFrame column name and `featureidkey` is set to `properties.<property name>` matching the GeoJSON
    - See [how we found the property name to use](lecture_3.ipynb#map-complaint-counts-by-cd)
  - The column and the GeoJSON properties have values that match
- **`SettingWithCopyWarning`:** [How to fix](https://www.dataquest.io/blog/settingwithcopywarning/)
- **`input()` stuck:** Jupyter can be a bit buggy when dealing with interactive input. If it seems to get stuck or you aren't seeing a prompt when you'd expect one, try clicking the `Kernel` menu then `Restart Kernel`.

### Disk full

If you get an error of `Disk is full` / `No space left on device` / `Out of diskspace`: You've used all the [available disk space](#limits). If you do fill it up, your server may not be able to start again (`spawn failed`). You'll need to delete one or more large files that you don't need anymore:

1. If you server is started already (you're seeing notebooks), click `Control Panel` -> `Stop My Server`.
1. Go to start your server again from [padmgp-4506-fall.rcnyu.org](https://padmgp-4506-fall.rcnyu.org).
1. Select `Troubleshooting Only - Clear Disk`.
1. Look at the `File size` Jupyter shows in the file browser.
1. Delete one or more large files.
1. If you're still using those datasets, [make them smaller](#reducing-data-size).

### `Error loading notebook`

This error can happen if you tried to output a lot of data in tables/charts. Steps to resolve:

1. Open the [JupyterHub](https://padmgp-4506-fall.rcnyu.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fafeld%2Fpython-public-policy&urlpath=tree%2Fpython-public-policy%2F&branch=nyu)) file browser
1. Click `New`, then `Terminal`
1. Run the following, changing the [path](https://www.codecademy.com/resources/docs/general/file-paths) at the end to match whatever notebook needs to be repaired:

   ```sh
   jupyter nbconvert --to notebook --clear-output ~/python-public-policy/hw_<NUMBER>.ipynb
   ```

If you're confused by these instrucions, download the notebook file and [email to the instructor](syllabus.md#instructor-information).

### kernel and memory issues

The kernel is the place where Python is installed and the code is actually executing, in the cloud somewhere.

- Make sure `Python [conda env:python-public-policy]` is selected as the kernel.
  - Shows in the top right of the notebook interface
  - To change:
    1. Open the `Kernel` menu
    1. Click `Change kernel`
    1. Click `Python [conda env:python-public-policy]`
- If your kernel is repeatedly crashing, you're probably running out of memory.
  - Make sure you aren't loading data sets you don't need.
  - If loading a new dataset, [make it smaller](#reducing-data-size)
  - Close kernels you aren't using from the [Running](https://padmgp-4506-fall.rcnyu.org/user-redirect/tree#running) page.
