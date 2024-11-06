from nbformat import NotebookNode
from .diffable import should_clear_output


def test_ignore_empty():
    cell = NotebookNode({"source": "", "outputs": ""})
    assert should_clear_output(cell) is False


def test_ignore_random():
    cell = NotebookNode({"source": "foo = 6", "outputs": ""})
    assert should_clear_output(cell) is False


def test_ignore_system():
    cell = NotebookNode({"source": "!pip install", "outputs": ""})
    assert should_clear_output(cell)


def test_ignore_image():
    cell = NotebookNode(
        {
            "source": "import qrcode\nqrcode.make('hello')",
            "outputs": [
                {
                    "data": {
                        "image/png": "…",
                    }
                }
            ],
        }
    )
    assert should_clear_output(cell)


def test_ignore_memory():
    cell = NotebookNode(
        {
            "source": "import qrcode\nqrcode.make('hello')",
            "outputs": [
                {
                    "data": {
                        "text/plain": "<qrcode.image.pil.PilImage at 0x1060e5850>",
                    }
                }
            ],
        }
    )
    assert should_clear_output(cell)
