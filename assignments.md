# General assignment information

- [Due dates](syllabus.html#schedule)
- [Scoring](syllabus.html#assignment-scoring)

## Tips

- **All lecture slides and homework templates can be found under [`class_materials/`](https://padmgp-4506001-fall.rcnyu.org/user-redirect/notebooks/class_materials/).** The contents of this directory will be automatically updated from [the GitHub repository](https://github.com/afeld/python-public-policy), but should keep any changes you make.
- **Read the instructions carefully.** Like word problems from math class, they are very specific in what they are asking for.
- **Spot check your results.** If you are transforming data from a previous Step, compare the results, do a handful of the calculations manually, etc. to ensure that the results are correct.
- **[Don't repeat yourself (DRY).](https://dzone.com/articles/is-your-code-dry-or-wet)** If you find yourself copying and pasting code within a notebook, there's probably a better way to do it.
- **Avoid [hard-coding](https://www.quora.com/What-does-hard-coded-something-mean-in-computer-programming-context) values.** Don't rely on things like row numbers or column order being stable, in case the dataset were to be updated.

## Common issues

- **PDF export:**

  - **Plotly charts/maps not appearing:** Include the [boilerplate](https://whynameitthat.blogspot.com/2013/10/boiler-plate.html) codeL

    ```python
    import plotly.io as pio
    pio.renderers.default = "notebook_connected+pdf"
    ```

  - **500 error:** You may be outputting too much data. Try reducing your output (in the Jupyter sense) to smaller subsets.

- **`Disk is full` / `No space left on device`:** Your workspace in JupyterHub has a limit of 1GB (a.k.a 1,000 MB or 1,000,000 KB) across all your files. Jupyter shows the `File size` of each in the file browser. Try deleting some larger files that you don't need anymore.
  - If you do fill it up, your server may not be able to start again (`spawn failed`). You'll need to reach out to the instructor.
- **When using `choropleth_mapbox()`, nothing appears on the map:** Make sure:
  - Your `locations` corresponds to the DataFrame column name and `featureidkey` is set to `properties.<property name>` matching the GeoJSON
  - The column and the GeoJSON properties have values that match

### Kernel/memory issues

- Make sure `Python [conda env:python-public-policy]` is selected as the kernel.
  - Shows in the top right of the notebook interface
  - Change from `Kernel` menu → `Change kernel` → `Python [conda env:python-public-policy]`
- If your kernel is repeatedly crashing, you're probably running out of memory.
  - Make sure you aren't loading data sets you don't need.
  - Close kernels you aren't using from the [Running](https://padmgp-4506001-fall.rcnyu.org/user-redirect/tree#running) page.

## Turning in assignments

1. Ensure all the outputs are visible and the notebook is cleaned up.
   - This is a good time to run the notebook end-to-end with ⏩ (`Restart and run all`).
   - See [general scoring criteria](syllabus.html#assignment-scoring).
1. Leave your name off the notebook filename and the notebook itself, as assignments are graded anonymously.
1. Export the notebook as a PDF. From the Jupyter interface, go to:
   1. `File`
   1. `Download as`
   1. `PDF via LaTeX (PDF)`
1. Glance through the PDF to ensure everything is showing up as you intend.
   - What you see is what the instructors will see.
1. Upload the PDF to the {{lms_name}} Assignment.

After the resubmission deadline passes for each Assignment, the solutions will be posted in [`shared/solutions/`](https://padmgp-4506001-fall.rcnyu.org/user-redirect/tree/shared/solutions/).

Note: In-class exercises will not be graded.
