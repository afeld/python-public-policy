import glob
import pytest
import re
from .lib.nb_helper import read_notebook


def check_metadata(notebook, file, expected_kernel):
    metadata = notebook.metadata
    runtime = metadata.kernelspec.display_name

    assert runtime == expected_kernel
    assert metadata.language_info.version.startswith("3.")

    if "colab" in metadata:
        colab_name = metadata["colab"]["name"]
        assert colab_name == file, f"Name in metadata doesn't match filename for {file}."


def check_file(file, expected_kernel="Python [conda env:python-public-policy] *"):
    notebook = read_notebook(file)
    check_metadata(notebook, file, expected_kernel)


def is_markdown(cell):
    return cell.cell_type == "markdown"


def is_h1(cell):
    return is_markdown(cell) and cell.source.startswith("# ")


notebooks = glob.glob("*.ipynb")
notebooks.sort()
crash_course = "extras/pandas_crash_course.ipynb"
all_notebooks = notebooks + [crash_course]


@pytest.mark.parametrize("notebook", notebooks)
def test_class_notebooks(notebook):
    check_file(notebook)


def test_colab():
    # run in Google Colab
    check_file(crash_course, "Python 3")


@pytest.mark.parametrize("file", all_notebooks)
def test_one_h1(file):
    notebook = read_notebook(file)
    num_h1s = sum(is_h1(cell) for cell in notebook.cells)
    assert num_h1s == 1


@pytest.mark.parametrize("file", all_notebooks)
def test_heading_levels(file):
    notebook = read_notebook(file)
    for cell in notebook.cells:
        meta = cell.metadata
        source = cell.source
        if is_markdown(cell) and "slideshow" in meta and source.startswith("#"):
            # slide with a heading
            slide_type = meta["slideshow"]["slide_type"]
            if slide_type == "slide":
                assert source.startswith(("# ", "## ")), "should be an H1 or H2"
            elif slide_type == "subslide":
                assert source.startswith("###"), "should be H3+"


@pytest.mark.parametrize("file", notebooks)
def test_nested_lists(file):
    """JupyterBook's markdown parser doesn't support nested lists with two spaces."""

    notebook = read_notebook(file)
    for cell in notebook.cells:
        source = cell.source
        if is_markdown(cell):
            for line in source.splitlines():
                match = re.match(r"^( +)(-|\d\.)", line)
                if match:
                    num_spaces = len(match[1])
                    assert (
                        num_spaces % 3 == 0 or num_spaces % 4 == 0
                    ), f"Lists should be indented in multiples of three or four spaces. Text:\n\n{source}\n"


hw_notebooks = glob.glob("hw_*.ipynb")


@pytest.mark.parametrize("file", hw_notebooks)
def test_reminders(file):
    notebook = read_notebook(file)

    assert any(
        "assignments.html" in cell.source for cell in notebook.cells
    ), "Missing assignment submission instructions"

    assert any(
        "participation" in cell.source for cell in notebook.cells
    ), "Missing participation reminder"
