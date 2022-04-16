import glob
import json


def check_metadata(notebook, file, expected_kernel):
    metadata = notebook["metadata"]
    runtime = metadata["kernelspec"]["display_name"]

    assert runtime == expected_kernel
    assert metadata["language_info"]["version"].startswith("3.")

    if "colab" in metadata:
        colab_name = metadata["colab"]["name"]
        assert (
            colab_name == file
        ), f"Name in metadata doesn't match filename for {file}."


def check_file(file, expected_kernel="Python [conda env:python-public-policy] *"):
    print(f"Checking {file}...")
    notebook = json.load(open(file))
    check_metadata(notebook, file, expected_kernel)


def test_class_notebooks():
    for file in glob.glob("*.ipynb"):
        check_file(file)

def test_colab():
    # run in Google Colab
    check_file("extras/pandas_crash_course.ipynb", "Python 3")
