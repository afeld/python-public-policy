from nbformat import NotebookNode
from .diffable import should_clear_output


def test_ignore_empty():
    cell = NotebookNode({"source": "", "outputs": ""})
    assert should_clear_output(cell) == False


def test_ignore_random():
    cell = NotebookNode({"source": "foo = 6", "outputs": ""})
    assert should_clear_output(cell) == False


def test_ignore_system():
    cell = NotebookNode({"source": "!pip install", "outputs": ""})
    assert should_clear_output(cell)


def test_ignore_ipytest():
    cell = NotebookNode({"source": "%%ipytest -qq", "outputs": ""})
    assert should_clear_output(cell)