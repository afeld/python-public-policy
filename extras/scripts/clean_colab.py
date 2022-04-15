# jupyter nbconvert --to notebook --Exporter.preprocessors=extras.scripts.clean_colab.CleanColab --inplace <file>.ipynb

from nbconvert.preprocessors import Preprocessor


def remove_key(obj, key):
    if key in obj:
        del obj[key]


# based off of
# https://github.com/jupyter/nbconvert/blob/master/nbconvert/preprocessors/tagremove.py
class CleanColab(Preprocessor):
    def preprocess(self, nb, resources):
        nb, resources = super().preprocess(nb, resources)
        remove_key(nb.metadata, "colab")
        return nb, resources

    def preprocess_cell(self, cell, resources, cell_index):
        remove_key(cell.metadata, "colab")
        remove_key(cell.metadata, "colab_type")
        return cell, resources
