import nbconvert
import nbformat


def notebook_to_script(notebook):
    exporter = nbconvert.exporters.PythonExporter
    script, _ = nbconvert.exporters.export(exporter, notebook)
    return script


def read_notebook(notebook_path):
    return nbformat.read(notebook_path, as_version=4)
