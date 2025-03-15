from glob import glob

import pytest

from .lib.nb_helper import read_notebook


hw_notebooks = glob("hw_*.ipynb")
hw_notebooks.sort()

hw_markdown = glob("hw_*.md")
hw_markdown.sort()


@pytest.mark.parametrize("file", hw_notebooks)
def test_notebook_reminders(file):
    notebook = read_notebook(file)

    assert any(
        "assignments.html" in cell.source for cell in notebook.cells
    ), "Missing assignment submission instructions"

    assert any(
        "participation" in cell.source for cell in notebook.cells
    ), "Missing participation reminder"


@pytest.mark.parametrize("file", hw_markdown)
def test_markdown_reminders(file):
    with open(file) as f:
        homework = f.read()

    assert "assignments.md" in homework, "Missing assignment submission instructions"
    assert "participation" in homework, "Missing participation reminder"
