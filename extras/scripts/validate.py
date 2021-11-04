import glob
import json


def test_metadata(notebook, file, expected_kernel):
    metadata = notebook["metadata"]
    runtime = metadata["kernelspec"]["display_name"]

    assert (
        runtime == expected_kernel
    ), f"Runtime name incorrect for {file}: it's `{runtime}`, but should be `{expected_kernel}`."

    assert metadata["language_info"]["version"].startswith("3.")

    if "colab" in metadata:
        colab_name = metadata["colab"]["name"]
        assert (
            colab_name == file
        ), f"Name in metadata doesn't match filename for {file}."


def test_file(file, expected_kernel="Python [conda env:python-public-policy] *"):
    print(f"Checking {file}...")
    notebook = json.load(open(file))
    test_metadata(notebook, file, expected_kernel)


for file in glob.glob("*.ipynb"):
    test_file(file)

# run in Google Colab
test_file("extras/pandas_crash_course.ipynb", "Python 3")

print("Passed!")
