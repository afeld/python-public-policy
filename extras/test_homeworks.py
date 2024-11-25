from glob import glob

import pytest

from .lib.nb_helper import is_markdown, read_notebook


hw_notebooks = glob("hw_*.ipynb")
hw_notebooks.sort()


@pytest.mark.parametrize("file", hw_notebooks)
def test_reminders(file):
    notebook = read_notebook(file)

    assert any(
        "assignments.html" in cell.source for cell in notebook.cells
    ), "Missing assignment submission instructions"

    assert any(
        "participation" in cell.source for cell in notebook.cells
    ), "Missing participation reminder"


@pytest.mark.parametrize("file", hw_notebooks)
def test_no_markdown_images(file):
    """https://edstem.org/us/courses/68651/discussion/5782405?answer=13400397"""

    notebook = read_notebook(file)

    assert not any("![" in cell.source for cell in notebook.cells if is_markdown(cell))
