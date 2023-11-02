# General assignment information

- [Due dates](syllabus.md#schedule)
- [Scoring](syllabus.md#assignment-scoring)

## Getting started

To edit/execute a Homework/lecture notebook:

1. Open the Homework page on this site.
1. Click the launch button (🚀) at the top.
1. You should now see the notebook in Google Colab.
1. Make sure you're using your Columbia Google account. [How to switch.](https://support.google.com/accounts/answer/1721977)
1. Save a copy to your Google Drive.
- [Google Colab walkthrough](https://columbiauniversity.zoom.us/rec/play/TfO3SbhRcAOSYoOc-HD7M_4d8cMQoAJCrcyJMIuUxfX1k7oX-txkCejsFLKxzrDn17aHDrlmWZumgS43.-J8dPQthf7yG1Iqx)
## Tips



- **Read the instructions carefully.** Like word problems from math class, they are very specific in what they are asking for.
- **Spot check your results.** If you are transforming data from a previous Step, compare the results, do a handful of the calculations manually, etc. to ensure that the results are correct.
- **[Don't repeat yourself (DRY).](https://dzone.com/articles/is-your-code-dry-or-wet)** If you find yourself copying and pasting code within a notebook, there's probably a better way to do it.
- **Avoid [hard-coding](https://www.quora.com/What-does-hard-coded-something-mean-in-computer-programming-context) values.** Don't rely on things like row numbers or column order being stable, in case the dataset were to be updated.

### Storing data

To keep data between sessions, you'll probably want to store it in Google Drive.

1. Upload the file(s) somewhere in Drive.
1. In the Colab sidebar, click the `Files` icon.
1. Click the `Mount Drive` icon.
1. Navigate to the file.
1. Next to the filename, click the three dots.
1. Click `Copy path`.
1. Use this path with `read_csv()`.


### Reducing data size

You can make data smaller _before_ uploading by filtering it through:

- The data portal, if it supports it
  - [Instructions for Socrata-based portals](https://support.socrata.com/hc/en-us/articles/202950808-Creating-a-Filtered-View)
- In a spreadsheet program
- For the [NYC Open Data Portal](https://opendata.cityofnewyork.us/), though [the shortener widget](shorten.md)

## Submission

1. Ensure all the outputs are visible and the notebook is cleaned up.
   - This is a good time to run the notebook end-to-end with `Restart and run all`.
   - See [general scoring criteria](syllabus.md#assignment-scoring).
1. Leave your name off the notebook filename and the notebook itself, as assignments are graded anonymously.
1. [Share your notebook](https://research.google.com/colaboratory/faq.html#notebook-storage) with [the instructor and Reader](syllabus.md#instructor-information) with `Commenter` permissions.
1. Drop the link to the Colab notebook in the CourseWorks Assignment.

Engaging with comments left in Google Colab is more than welcome. After [the late submission deadline](syllabus.md#schedule) for a given Homework passes, the solution will be shared.


Note: In-class exercises will not be graded.

## Common issues

- **Mounting Google Drive is slow or fails:** See [the Google Colab help page](https://research.google.com/colaboratory/faq.html#drive-timeout).
- **Can't load a file from Drive with `requests.get()`:** Use [`open()`](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).
  - [How to read a JSON file](https://www.freecodecamp.org/news/python-parse-json-how-to-read-a-json-file/#how-to-parse-and-read-a-json-file-in-python)
- **When using `choropleth_mapbox()`, nothing appears on the map:** Make sure:
  - Your `locations` corresponds to the DataFrame column name and `featureidkey` is set to `properties.<property name>` matching the GeoJSON
    - See [how we found the property name to use](lecture_3.ipynb#map-complaint-counts-by-cd)
  - The column and the GeoJSON properties have values that match
- **`SettingWithCopyWarning`:** Use `.loc[condition, "column name"] = …`. [More details.](https://www.dataquest.io/blog/settingwithcopywarning/)
- **`input()` stuck:** Jupyter can be a bit buggy when dealing with interactive input. If it seems to get stuck or you aren't seeing a prompt when you'd expect one, try clicking the `Runtime` menu then `Restart`.



### runtime/memory issues

The runtime is the place where Python is installed and the code is actually executing, in the cloud somewhere.


- If your runtime is repeatedly crashing, you're probably running out of memory.
  - Make sure you aren't loading data sets you don't need.
  - If loading a new dataset, [make it smaller](#reducing-data-size)
  
