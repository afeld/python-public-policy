import glob
import pytest
from .nb_helper import read_notebook


def check_metadata(notebook, file, expected_kernel):
    metadata = notebook.metadata
    runtime = metadata.kernelspec.display_name

    assert runtime == expected_kernel
    assert metadata.language_info.version.startswith("3.")

    if "colab" in metadata:
        colab_name = metadata["colab"]["name"]
        assert (
            colab_name == file
        ), f"Name in metadata doesn't match filename for {file}."


def check_file(file, expected_kernel="Python [conda env:python-public-policy] *"):
    notebook = read_notebook(file)
    check_metadata(notebook, file, expected_kernel)


def is_h1(cell):
    return cell.cell_type == "markdown" and cell.source.startswith("# ")


notebooks = glob.glob("*.ipynb")


@pytest.mark.parametrize("notebook", notebooks)
def test_class_notebooks(notebook):
    check_file(notebook)


def test_colab():
    # run in Google Colab
    check_file("extras/pandas_crash_course.ipynb", "Python 3")


@pytest.mark.parametrize("file", notebooks)
def test_one_h1(file):
    notebook = read_notebook(file)
    num_h1s = sum(is_h1(cell) for cell in notebook.cells)
    assert num_h1s == 1
