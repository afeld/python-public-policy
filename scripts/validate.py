import glob
import json


def test_colab_metadata(notebook, file):
    metadata = notebook["metadata"]
    runtime = metadata["kernelspec"]["display_name"]
    expected = "Python 3"

    assert (
        runtime == expected
    ), f"Runtime name incorrect for {file}: it's `{runtime}`, but should be `{expected}`."

    assert metadata["language_info"]["version"].startswith("3.")

    if "colab" in metadata:
        colab_name = metadata["colab"]["name"]
        assert (
            colab_name == file
        ), f"Name in metadata doesn't match filename for {file}."


def test_badge(notebook, file):
    cell = notebook["cells"][0]
    source = cell["source"][0]
    nb_url = f"https://colab.research.google.com/github/afeld/python-public-policy/blob/main/{file}"
    assert nb_url in source, f"'Open in Colab' badge missing/incorrect for {file}."


for file in glob.glob("*.ipynb"):
    print(f"Checking {file}...")
    notebook = json.load(open(file))
    test_colab_metadata(notebook, file)
    test_badge(notebook, file)

print("Passed!")
