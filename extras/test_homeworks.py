from glob import glob

import pytest

from .lib.nb_helper import read_notebook


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
