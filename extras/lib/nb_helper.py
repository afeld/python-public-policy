import nbconvert
import nbformat
from nbformat import NotebookNode
from .diffable import is_system_command


def notebook_to_script(notebook: NotebookNode):
    exporter = nbconvert.exporters.PythonExporter
    script, _ = nbconvert.exporters.export(exporter, notebook)
    return script


def read_notebook(notebook_path: str) -> NotebookNode:
    return nbformat.read(notebook_path, as_version=4)


def is_markdown(cell: NotebookNode):
    return cell.cell_type == "markdown"


def is_h1(cell: NotebookNode):
    return is_markdown(cell) and cell.source.startswith("# ")


def is_magic(source: str):
    """https://ipython.readthedocs.io/en/stable/interactive/tutorial.html#magic-functions"""
    return source.startswith("%%")


def is_code_cell(cell: NotebookNode):
    return cell.cell_type == "code"


def is_python(cell: NotebookNode):
    source = cell.source
    return cell.cell_type == "code" and not (
        is_magic(source) or is_system_command(source)
    )


def get_tags(cell: NotebookNode):
    return cell.metadata.get("tags", [])
