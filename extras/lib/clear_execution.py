# adapted from
# https://github.com/jupyter/nbconvert/blob/main/nbconvert/preprocessors/clearmetadata.py

from nbconvert.preprocessors import Preprocessor


class ClearExecutionPreprocessor(Preprocessor):
    """Removes the execution metadata from all code cells in a notebook."""

    def preprocess_cell(self, cell, resources, cell_index):
        if cell.cell_type == "code" and "metadata" in cell:
            metadata = cell.metadata
            if "execution" in metadata:
                metadata["execution"] = {}
        return cell, resources
