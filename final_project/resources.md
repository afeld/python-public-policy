# [Final Project](../final_project.md) resources

Seee also: [open-ended assignment information](../assignments.md#open-ended-assignments)

## Counting lines of code

To count the number of lines of code in a notebook:

1. Download the notebook.
1. Upload the notebook to [Google Colab](https://colab.research.google.com/).
1. Download the notebook as a Python file.
    1. With the notebook open in JupyterHub, go to `File`->`Download`->`Download .py`.
1. Upload the Python file to Google Colab.
    1. Click the `Files` icon in the sidebar.
    1. Click the `Upload to session storage` button.
    1. Select the `.py` file.
1. Put the following in a code cell and run it.

    ```sh
    !apt-get install -y cloc > /dev/null
    !cloc --hide-rate --by-file *.py
    ```
