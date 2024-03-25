# General assignment information

- [Due dates](syllabus.md#schedule)
- [Scoring](syllabus.md#assignment-scoring)

## Getting started

To edit/execute a Homework/lecture notebook:

1. Open the page for the Homework/Lecture on this site.
   - For example: [Homework 0](hw_0.ipynb)
1. Click the launch button (🚀) at the top.
1. You should now see the notebook in {{coding_env_name}}.
{% if id == 'columbia' -%}
1. Make sure you're using your Columbia Google account. [How to switch.](https://support.google.com/accounts/answer/1721977)
1. Click `Copy to Drive`.
{% endif -%}

That is now your own copy; make edits in there directly.

## Tips

{% if id == 'nyu' -%}
- **All lecture slides and homework templates can be found under [`python-public-policy/`]({{coding_env_url}}).** The contents of this directory will be automatically updated from [the GitHub repository](https://github.com/afeld/python-public-policy/tree/{{school_slug}}), but should keep any changes you make.
- **Access [{{coding_env_name}}]({{coding_env_url}}) via the links on this site** rather than bookmarking {{coding_env_name}}, as that will pull down the latest changes.
{% endif -%}
- **Read the instructions carefully.** Like word problems from math class, they are very specific in what they are asking for.
- **Spot check your results.** If you are transforming data from a previous Step, compare the results, do a handful of the calculations manually, etc. to ensure that the results are correct.
- You are always welcome to **add cells**. You probably don't want more than a few lines of code in each. This makes the spot checking of intermediate results easier.
- **[Don't repeat yourself (DRY).](https://dzone.com/articles/is-your-code-dry-or-wet)** If you find yourself copying and pasting code within a notebook, there's probably a better way to do it.
- **Avoid [hard-coding](https://www.quora.com/What-does-hard-coded-something-mean-in-computer-programming-context) values.** Don't rely on things like row numbers or column order being stable, in case the dataset were to be updated.

### Storing data

{% if id == 'columbia' -%}
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
  - [Instructions for Socrata-based portals](https://support.socrata.com/hc/en-us/articles/202950808-Creating-a-Filtered-View)
- In a spreadsheet program
- For the [NYC Open Data Portal](https://opendata.cityofnewyork.us/), though [the shortener widget](shorten.md)

## Submission

1. Ensure all the outputs are visible and the notebook is cleaned up.
   - This is a good time to run the notebook end-to-end with `Restart and run all`{% if id == 'nyu' %} (⏩){% endif %}.
   - See [general scoring criteria](syllabus.md#assignment-scoring).
{% if id == 'columbia' -%}
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
   - What you see is what the instructors will see.
1. **If one of the Homeworks:** Upload the PDF to the {{lms_name}} Assignment.
1. **If the Final Project:**
   1. In [{{lms_name}}]({{lms_url}}), go to [`Content`, then `Final Project`](https://brightspace.nyu.edu/d2l/le/lessons/366164/topics/9977658). You should see an embedded TurnItIn/PeerMark dashboard.
   1. Follow [these instructions](https://help.turnitin.com/feedback-studio/d2l/LTI13/student/submitting-a-paper/submitting-a-paper.htm) to upload the PDF.

When you're ready to have it formally re-graded, please resubmit through the same Assignment in {{lms_name}}.

After the resubmission deadline passes for each Assignment, the solutions will be posted in [`shared/solutions/`](https://padm-4506-spring.rcnyu.org/user-redirect/tree/shared/solutions/).
{%- endif %}

Note: In-class exercises will not be graded.

## Common issues

{% if id == 'columbia' -%}
- **Mounting Google Drive is slow or fails:** See [the Google Colab help page](https://research.google.com/colaboratory/faq.html#drive-timeout).
- **Can't load a file from Drive with `requests.get()`:** Use [`open()`](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).
  - [How to read a JSON file](https://www.freecodecamp.org/news/python-parse-json-how-to-read-a-json-file/#how-to-parse-and-read-a-json-file-in-python)
{% else -%}
- **PDF export:**
  - **500 error:** You may be outputting too much data. Try reducing your output (in the Jupyter sense) to smaller subsets.
{% endif -%}
- **When using `choropleth_mapbox()`, nothing appears on the map:** Make sure:
  - Your `locations` corresponds to the DataFrame column name and `featureidkey` is set to `properties.<property name>` matching the GeoJSON
    - See [how we found the property name to use](lecture_3.ipynb#map-complaint-counts-by-cd)
  - The column and the GeoJSON properties have values that match
- **`SettingWithCopyWarning`:** [How to fix](https://www.dataquest.io/blog/settingwithcopywarning/)
- **`input()` stuck:** Jupyter can be a bit buggy when dealing with interactive input. If it seems to get stuck or you aren't seeing a prompt when you'd expect one, try clicking the `{{coding_env_kernel_name.title()}}` menu then `Restart Kernel`.

{% if id == 'nyu' -%}
### Disk full

If you get an error of `Disk is full` / `No space left on device` / `Out of diskspace`: You've used all the [available disk space](#limits). If you do fill it up, your server may not be able to start again (`spawn failed`). You'll need to delete one or more large files that you don't need anymore:

1. If you server is started already (you're seeing notebooks), click `Control Panel` -> `Stop My Server`.
1. Go to start your server again from [padm-4506-spring.rcnyu.org](https://padm-4506-spring.rcnyu.org).
1. Select `Troubleshooting Only - Clear Disk`.
1. Look at the `File size` Jupyter shows in the file browser.
1. Delete one or more large files.
1. If you're still using those datasets, [make them smaller](#reducing-data-size).

### `Error loading notebook`

This error can happen if you tried to output a lot of data in tables/charts. Steps to resolve:

1. Open the [{{coding_env_name}}]({{coding_env_url}})) file browser
1. Click `New`, then `Terminal`
1. Run the following, changing the [path](https://www.codecademy.com/resources/docs/general/file-paths) at the end to match whatever notebook needs to be repaired:

   ```sh
   jupyter nbconvert --to notebook --clear-output ~/python-public-policy/hw_<NUMBER>.ipynb
   ```

If you're confused by these instrucions, download the notebook file and [email to the instructor](syllabus.md#instructor-information).
{%- endif %}

### {{coding_env_kernel_name}}/memory issues

The {{coding_env_kernel_name}} is the place where Python is installed and the code is actually executing, in the cloud somewhere.

{% if id == 'nyu' -%}
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
  {% if id == 'nyu' %}- Close {{coding_env_kernel_name}}s you aren't using from the [Running](https://padm-4506-spring.rcnyu.org/user-redirect/tree#running) page.{% endif %}
