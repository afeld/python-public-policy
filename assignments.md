# General assignment information

- [Due dates](syllabus.md#schedule)
- [Scoring](syllabus.md#assignment-scoring)

## Getting started

To edit/execute a Homework/lecture notebook:

1. Open the Homework page on this site.
1. Click the launch button (🚀) at the top.
1. You should now see the notebook in JupyterHub.
1. Click `File`->`Save as...`
1. In the text box, delete `class_materials/` and replace with `<name>.ipynb`, so for example: `hw_1.ipynb`.
## Tips

- **All lecture slides and homework templates can be found under [`class_materials/`](https://padmgp-4506.rcnyu.org/user-redirect/notebooks/class_materials/).** The contents of this directory will be automatically updated from [the GitHub repository](https://github.com/afeld/python-public-policy/tree/nyu), but should keep any changes you make.

- **Read the instructions carefully.** Like word problems from math class, they are very specific in what they are asking for.
- **Spot check your results.** If you are transforming data from a previous Step, compare the results, do a handful of the calculations manually, etc. to ensure that the results are correct.
- **[Don't repeat yourself (DRY).](https://dzone.com/articles/is-your-code-dry-or-wet)** If you find yourself copying and pasting code within a notebook, there's probably a better way to do it.
- **Avoid [hard-coding](https://www.quora.com/What-does-hard-coded-something-mean-in-computer-programming-context) values.** Don't rely on things like row numbers or column order being stable, in case the dataset were to be updated.

### Storing data

1. Open the [JupyterHub file browser](https://padmgp-4506.rcnyu.org/user-redirect/notebooks/class_materials/).
1. Navigate to the folder your notebook is in.
1. [Upload the data.](https://tljh.jupyter.org/en/latest/howto/content/add-data.html#adding-data-from-your-local-machine)
1. From Python, use `read_csv("./<filename>.csv")`.

[More info about file paths](https://www.codecademy.com/resources/docs/general/file-paths)

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
1. Leave your name off the notebook filename and the notebook itself, as assignments are graded anonymously.
1. Export the notebook as a PDF. From the Jupyter interface, go to:
   1. `File`
   1. `Download as`
   1. `PDF via LaTeX (PDF)`
1. Glance through the PDF to ensure everything is showing up as you intend.
   - What you see is what the instructors will see.
1. **If one of the Homeworks:** Upload the PDF to the Brightspace Assignment.
1. **If the Final Project:**
   1. In [Brightspace](https://brightspace.nyu.edu/d2l/home/297088), go to [`Content`](https://brightspace.nyu.edu/d2l/le/lessons/297088) then `Final Project`. You should see an embedded TurnItIn/PeerMark dashboard.
   1. Follow [these instructions](https://help.turnitin.com/feedback-studio/d2l/LTI13/student/submitting-a-paper/submitting-a-paper.htm) to upload the PDF.

When you're ready to have it formally re-graded, please resubmit through the same Assignment in Brightspace.

After the resubmission deadline passes for each Assignment, the solutions will be posted in [`shared/solutions/`](https://padmgp-4506.rcnyu.org/user-redirect/tree/shared/solutions/).

Note: In-class exercises will not be graded.

## Common issues

- **PDF export:**

  - **Plotly charts/maps not appearing:** Include the [boilerplate](https://whynameitthat.blogspot.com/2013/10/boiler-plate.html) code.

    ```python
    import plotly.io as pio
    pio.renderers.default = "notebook_connected+pdf"
    ```

  - **500 error:** You may be outputting too much data. Try reducing your output (in the Jupyter sense) to smaller subsets.
- **When using `choropleth_mapbox()`, nothing appears on the map:** Make sure:
  - Your `locations` corresponds to the DataFrame column name and `featureidkey` is set to `properties.<property name>` matching the GeoJSON
    - See [how we found the property name to use](lecture_3.ipynb#map-complaint-counts-by-cd)
  - The column and the GeoJSON properties have values that match
- **`SettingWithCopyWarning`:** Use `.loc[condition, "column name"] = …`. [More details.](https://www.dataquest.io/blog/settingwithcopywarning/)
- **`input()` stuck:** Jupyter can be a bit buggy when dealing with interactive input. If it seems to get stuck or you aren't seeing a prompt when you'd expect one, try clicking the `Kernel` menu then `Restart`.

### Disk full

If you get an error of `Disk is full` / `No space left on device`: You've used all the [available disk space](#limits). If you do fill it up, your server may not be able to start again (`spawn failed`). You'll need to delete one or more large files that you don't need anymore:

1. If you server is started already (you're seeing notebooks), click `Control Panel` -> `Stop My Server`.
1. Go to start your server again (visit [JupyterHub](https://padmgp-4506.rcnyu.org/user-redirect/notebooks/class_materials/)).
1. Select `Troubleshooting Only - Clear Disk`.
1. Look at the `File size` Jupyter shows in the file browser.
1. Delete one or more large files.
1. If you're still using those datasets, [make them smaller](#reducing-data-size).

### `Error loading notebook`

This error can happen if you tried to output a lot of data in tables/charts. Steps to resolve:

1. Open the [JupyterHub](https://padmgp-4506.rcnyu.org/user-redirect/notebooks/class_materials/)) file browser
1. Click `New`, then `Terminal`
1. Run the following, changing the [path](https://www.codecademy.com/resources/docs/general/file-paths) at the end to match whatever notebook needs to be repaired:

   ```sh
   jupyter nbconvert --to notebook --clear-output ~/class_materials/hw_<NUMBER>.ipynb
   ```

If you're confused by these instrucions, download the notebook file and [email to the instructor](syllabus.md#instructor-information).

### kernel/memory issues

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
  - Close kernels you aren't using from the [Running](https://padmgp-4506.rcnyu.org/user-redirect/tree#running) page.
