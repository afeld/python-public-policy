from nbformat import NotebookNode
from scripts.diffable import should_clear_output


def test_ignore_empty():
    cell = NotebookNode({"source": ""})
    assert should_clear_output(cell) == False

def test_ignore_random():
    cell = NotebookNode({"source": "foo = 6"})
    assert should_clear_output(cell) == False

def test_ignore_system():
    cell = NotebookNode({"source": "!pip install"})
    assert should_clear_output(cell)

def test_ignore_ipytest():
    cell = NotebookNode({"source": "%%ipytest -qq"})
    assert should_clear_output(cell)
