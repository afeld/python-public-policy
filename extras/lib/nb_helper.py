import nbconvert
import nbformat
from .diffable import is_system_command


def notebook_to_script(notebook):
    exporter = nbconvert.exporters.PythonExporter
    script, _ = nbconvert.exporters.export(exporter, notebook)
    return script


def read_notebook(notebook_path):
    return nbformat.read(notebook_path, as_version=4)


def is_markdown(cell):
    return cell.cell_type == "markdown"


def is_h1(cell):
    return is_markdown(cell) and cell.source.startswith("# ")


def is_magic(source):
    return source.startswith("%%")


def is_python(cell):
    source = cell.source
    return cell.cell_type == "code" and not (is_magic(source) or is_system_command(source))
