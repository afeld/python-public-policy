# General assignment information

- [Due dates](syllabus.md#schedule)
- [Scoring](syllabus.md#assignment-scoring)

## Getting started

To edit/execute a Homework/lecture notebook:

1. Open the page for the Homework/Lecture on this site.
   - For example: [Homework 0](hw_0.ipynb)
1. Click the launch button (🚀) at the top.
   {% if id == "nyu" -%}
   - {{coding_env_name}} may take a few minutes to start up.
   {%- endif %}
1. You should now see the notebook in {{coding_env_name}}.
{% if id == "columbia" -%}
1. Make sure you're using your Columbia Google account. [How to switch.](https://support.google.com/accounts/answer/1721977)
1. Click `Copy to Drive`.
{% endif -%}

That is now your own copy; make edits in there directly.

## Tips

{% if id == "nyu" -%}
- **All lecture slides and homework templates can be found under [`python-public-policy/`]({{coding_env_url}}).** The contents of this directory will be automatically updated from [the GitHub repository](https://github.com/afeld/python-public-policy/tree/{{school_slug}}), but should keep any changes you make.
   - FYI that this uses [nbgitpuller](https://nbgitpuller.readthedocs.io/) under the hood.
- **Access [{{coding_env_name}}]({{coding_env_url}}) via the links on this site** rather than bookmarking {{coding_env_name}}, as that will pull down the latest changes.
{% endif -%}
- **Read the instructions carefully.** Like word problems from math class, they are very specific in what they are asking for.
- **Spot check your results.** If you are transforming data from a previous Step, compare the results, do a handful of the calculations manually, etc. to ensure that the results are correct.
- You are always welcome to **add cells**. You probably don't want more than a few lines of code in each. This makes the spot checking of intermediate results easier.
- **[Don't repeat yourself (DRY).](https://dzone.com/articles/is-your-code-dry-or-wet)** If you find yourself copying and pasting code within a notebook, there's probably a better way to do it.
- **Avoid [hard-coding](https://www.quora.com/What-does-hard-coded-something-mean-in-computer-programming-context) values.** Don't rely on things like row numbers or column order being stable, in case the dataset were to be updated.
- **Ask for help.**
   - The assignments are meant to be challenging, not impossible.
   - Try and work through problems on your own to start. If you are stuck for more than a half hour, [step away](https://dankim.org/posts/cant-crack-that-programming-problem/). If you _still_ can't figure it out, ask for help.
      - [Ed]({{discussions_url}})
      - [Office hours](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#instructor-information)

## Open-ended assignments

_[Homework 1](hw_1.md) and the [Final Project](final_project.md)_

### Open data portals

There are countless places to get data, notably:

- Local:
   - [NYC Open Data](https://opendata.cityofnewyork.us/)
      - [Scout](https://scout.tsdataclinic.com/explore/NYC) can be used to find datasets with certain columns
   - [BetaNYC](https://data.beta.nyc/)
- U.S. Federal:
   - [data.gov](https://www.data.gov/)
   - [Census Bureau](https://data.census.gov/)
   - [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/)
- [United Nations](https://data.un.org/)
- [World Bank](https://data.worldbank.org/)
- [World Health Organization (WHO)](https://www.who.int/data)
- [Economic Policy Institute](https://www.epi.org/data/)
- [Kaggle](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Black Wealth Data](https://blackwealthdata.org/)
- Lists of open data portals:
   - [DataPortals](https://dataportals.org/)
   - [Open Data Network](https://www.opendatanetwork.com/)

### Inspiration

For starters, see the [Final Project examples from past semesters](final_project/examples.md).

Probably not realistic to make visualizations that are as fancy as these ones made by professionals, but they may give you ideas. Some also include links/downloads of the source data.

- [FiveThirtyEight Interactives](https://projects.fivethirtyeight.com/)
- [The Guardian Visual Journalism](https://www.theguardian.com/interactive)
- [New York Times Graphics](https://www.nytimes.com/spotlight/graphics)
- [Our World in Data](https://ourworldindata.org/)
- [ProPublica News Apps](https://www.propublica.org/newsapps/)
- [Visual Capitalist](https://www.visualcapitalist.com/)

### Storing data

{% if id == "columbia" -%}
To keep data between sessions, you'll probably want to store it in Google Drive.

1. Upload the file(s) somewhere in Drive.
1. In the Colab sidebar, click the `Files` icon.
1. Click the `Mount Drive` icon.
   - Think of this as attaching your Drive to your Colab instance, as if you were plugging in a USB flash drive.
1. Navigate to the file.
1. Next to the filename, click the three dots.
1. Click `Copy path`.
   - The value should be something like `/content/drive/My Drive/...`.
1. Use this path with `read_csv()`.
{% else -%}
1. Open the [{{coding_env_name}} file browser]({{coding_env_url}}).
1. Navigate to the folder your notebook is in.
1. [Upload the data.](https://tljh.jupyter.org/en/latest/howto/content/add-data.html#adding-data-from-your-local-machine)
1. From Python, use `read_csv("./<filename>.csv")`.

Note that that file path should be to relative to the notebook within {{coding_env_name}} — `./` means "in the same directory". {{coding_env_name}} cannot access the file on your local machine; in other words, the path shouldn't start with `C:\\` or anything like that. [More info about file paths](https://www.codecademy.com/resources/docs/general/file-paths)

### Limits

{{coding_env_name}} has a disk storage limit of 1GB (a.k.a. 1,024 MB or 1,048,576 KB) across all your files, and a memory limit of 3GB.
{%- endif %}

### Reducing data size

You can make data smaller _before_ uploading by filtering it through:

- The data portal, if it supports it
  - This makes the download faster, including only the data you need.
  - [Instructions for Socrata-based portals](https://support.socrata.com/hc/en-us/articles/202950808-Creating-a-Filtered-View)
- In a spreadsheet program

{% if id == "nyu" -%}
## Generative AI

_See also: [course generative AI policy](syllabus.md#generative-ai)._

We will be using the AI [magic](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html#magic-functions).

### Documentation

- [NYU-specific](https://sites.google.com/nyu.edu/rit-genai/use-build/rit-jupyterhub#h.r3bhgpidqt5o)
- [General](https://jupyter-ai.readthedocs.io/en/latest/index.html)

Note that we only have the `gpt-4.0-32k` model enabled.

### Usage

1. **One-time setup:** Visit [projects.rit.nyu.edu](https://projects.rit.nyu.edu/) and accept the Terms of Use.
   - This site is only accessible from [the NYU network](https://www.nyu.edu/life/information-technology/infrastructure/network-services/nyu-net.html).
      - If you're off campus, you can connect via [the VPN](https://www.nyu.edu/life/information-technology/infrastructure/network-services/vpn.html).
1. Open [{{coding_env_name}}]({{coding_env_url}}).
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
{%- endif %}

## Submission

1. Ensure all the outputs are visible and the notebook is cleaned up.
   - This is a good time to run the notebook end-to-end with `Restart and run all`{% if id == "nyu" %} (⏩){% endif %}.
   - See [general scoring criteria](syllabus.md#assignment-scoring).
{% if id == "columbia" -%}
1. Confirm that the notebook is [shared](https://research.google.com/colaboratory/faq.html#notebook-storage) with [the instructor and {{assistant_name}}](syllabus.md#instructor-information) with `Commenter` permissions. If it isn't, [share the parent folder](hw_0.ipynb#one-time-setup) and re-confirm.
1. Copy the URL of your notebook.
   - The URL should be of the format `https://colab.research.google.com/drive/<long identifier>`. If it's `https://colab.research.google.com/github/...`, click `Copy to Drive`.
1. Paste your notebook URL in the {{lms_name}} Assignment.

Engaging with comments left in {{coding_env_name}} is more than welcome. After [the late submission deadline](syllabus.md#schedule) for a given Homework passes, the solution will be shared.
{% else -%}
1. Export the notebook as a PDF. From the Jupyter interface, go to:
   1. `File`
   1. `Save and Export Notebook As…`
   1. `PDF`
   1. You may need to [allow popups](https://support.google.com/chrome/answer/95472)
1. Glance through the PDF to ensure everything is showing up as you intend.
   - In particular, check your visualizations.
   - What you see is what the instructors will see.
   - [Troubleshooting tips](#pdf-export)
1. **If one of the Homeworks:** Upload the PDF to the {{lms_name}} Assignment.
1. **If the Final Project:**
   1. In [{{lms_name}}]({{lms_url}}), go to `Content`, then `Final Project`. You should see the TurnItIn/PeerMark dashboard.
   1. Follow [these instructions](https://help.turnitin.com/feedback-studio/d2l/LTI13/student/submitting-a-paper/submitting-a-paper.htm) to upload the PDF.

When you're ready to have it formally re-graded, please resubmit through the same Assignment in {{lms_name}}.
{%- endif %}

Note: In-class exercises will not be graded.

## Common issues

{% if id == "columbia" -%}
- **Mounting Google Drive is slow or fails:** See [the Google Colab help page](https://research.google.com/colaboratory/faq.html#drive-timeout).
- **Can't load a file from Drive with `requests.get()`:** Use [`open()`](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).
  - [How to read a JSON file](https://www.freecodecamp.org/news/python-parse-json-how-to-read-a-json-file/#how-to-parse-and-read-a-json-file-in-python)
{% else -%}
- **`Error: Command '['git', 'diff', '..origin/nyu', '--name-status']' returned non-zero exit status 128` when trying to launch {{coding_env_name}}:** Something got corrupted in your copy of the files that come through [`nbgitpuller`](https://nbgitpuller.readthedocs.io/). Easiest thing is to move the existing ones and restart with a fresh copy.
  1. [Launch {{coding_env_name}}.]({{coding_env_origin}})
  1. There should be a `python-public-policy` folder. Rename it, something like `python-public-policy-old`.
    - If you've edited any of the template notebooks, you can find them in that `-old` folder.
  1. Repeat the [getting started](#getting-started) steps.
{% endif -%}
- **When using `choropleth_map()`, nothing appears on the map:** Make sure:
  - Your `locations` corresponds to the DataFrame column name and `featureidkey` is set to `properties.<property name>` matching the GeoJSON
    - See [how we found the property name to use](lecture_3.ipynb#map-complaint-counts-by-cd)
  - The column and the GeoJSON properties have values that match
- **`SettingWithCopyWarning`:** [How to fix](https://www.dataquest.io/blog/settingwithcopywarning/)
- **`input()` stuck:** Jupyter can be a bit buggy when dealing with interactive input. If it seems to get stuck or you aren't seeing a prompt when you'd expect one, try clicking the `{{coding_env_kernel_name.title()}}` menu then `Restart Kernel`.
- **The values are out of order along the axis of a Plotly chart:** Make sure that:
   - The values are integers/floats/[timestamps](https://plotly.com/python/line-charts/#line-plots-on-date-axes), not strings, where applicable.
   - [Line charts: The column used for the X axis is sorted.](https://plotly.com/python/line-charts/#data-order-in-line-charts)
- **`AttributeError: partially initialized module 'orjson' has no attribute 'OPT_NON_STR_KEYS'`:** Add the following cell before your other Plotly code, then `Restart and run all`{% if id == "nyu" %} (⏩){% endif %}.

   ```python
   import plotly.io

   plotly.io.json.config.default_engine = 'json'
   ```

{% if id == "nyu" -%}
### Disk full

If you get an error of `Disk is full` / `No space left on device` / `Out of diskspace`: You've used all the [available disk space](#limits). If you do fill it up, your server may not be able to start again (`spawn failed`). You'll need to delete one or more large files that you don't need anymore:

1. If you server is started already (you're seeing notebooks), click `Control Panel` -> `Stop My Server`.
1. Go to [start your server again]({{coding_env_origin}}).
1. Select `Troubleshooting Only - Clear Disk`.
1. Look at the `File size` Jupyter shows in the file browser.
1. Delete one or more large files.
1. If you're still using those datasets, [make them smaller](#reducing-data-size).

### `Error loading notebook`

This error can happen if you tried to output a lot of data in tables/charts. Steps to resolve:

1. Open the [{{coding_env_name}}]({{coding_env_origin}})) file browser
1. Click `New`, then `Terminal`
1. Run the following, changing the [path](https://www.codecademy.com/resources/docs/general/file-paths) at the end to match whatever notebook needs to be repaired:

   ```sh
   jupyter nbconvert --to notebook --clear-output ~/python-public-policy/hw_<NUMBER>.ipynb
   ```

If you're confused by these instrucions, download the notebook file and [email to the instructor](syllabus.md#instructor-information).
{%- endif %}

### {{coding_env_kernel_name}} and memory issues

The {{coding_env_kernel_name}} is [the place where Python is installed and the code is actually executing](https://docs.jupyter.org/en/stable/projects/kernels.html#kernels), in the cloud somewhere.

{% if id == "nyu" -%}
- Make sure `Python [conda env:python-public-policy]` is selected as the {{coding_env_kernel_name}}.
  - Shows in the top right of the notebook interface
  - To change:
    1. Open the `{{coding_env_kernel_name.title()}}` menu
    1. Click `Change {{coding_env_kernel_name}}`
    1. Click `Python [conda env:python-public-policy]`
{%- endif %}
- If your {{coding_env_kernel_name}} is repeatedly crashing, you're probably running out of memory.
  - Make sure you aren't loading data sets you don't need.
  - If loading a new dataset, [make it smaller](#reducing-data-size)
  {% if id == "nyu" %}- Close {{coding_env_kernel_name}}s you aren't using from the [Running]({{coding_env_origin}}/user-redirect/tree#running) page.{% endif %}

{% if id == "nyu" -%}
### PDF export

[Jupyter notebook export to PDF is _fragile_, especially with interactive charts through Plotly.](meta/instructor_guide.md#jupyterhub-troubleshooting)

If you get a **500 error**, it could be happening for a handful of reasons. Scroll to the bottom and read the message.

- If it mentions `Undefined control sequence` and `\pandocbounded`, it's [an issue with the exporter](https://github.com/jupyter/nbconvert/issues/2173). Jump to the [Alternatives](#alternatives).
- If it mentions a package being missing, ask on [Ed]({{discussions_url}}).
- Otherwise, it may be crashing due to not being handle the complexity of the render. Try reducing your output (in the Jupyter sense) to smaller subsets. This can include:
   - Not displaying so many rows/values
   - Reducing the number of points that are plotted

#### Alternatives

If you are unable to get the direct-to-PDF export working, try:

- Going through HTML:
   1. [Export the notebook as HTML.](https://jupyterlab.readthedocs.io/en/stable/user/export.html)
   1. Open the HTML file in your browser.
   1. `File`->`Print…`
   1. `Save as PDF`
   1. If any of the visualizations are cut off:
      1. Cancel the Print to PDF.
      1. Viewing the HTML file, make the browser window narrower.
         - This forces the visualizations to re-draw.
      1. Try from `File`->`Print…` again.
- An online converter, such as [Ploomer](https://www.convert.ploomber.io/)
{%- endif %}
