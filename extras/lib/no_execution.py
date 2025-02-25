from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode


class NoExecution(Preprocessor):
    """A more minimal version of https://github.com/jupyter/nbconvert/blob/main/nbconvert/preprocessors/clearmetadata.py. Useful because nbconvert adds `execution` information to the cell metadata, while JupyterLab doesn't. This makes the two consistent."""

    def preprocess_cell(self, cell: NotebookNode, resources, cell_index):
        if "execution" in cell.metadata:
            del cell.metadata["execution"]

        return cell, resources
