import os
import pytest

from .nb_helper import notebook_to_script, read_notebook


@pytest.fixture()
def notebook():
    nb_full_path = os.path.join(os.getcwd(), "hw_6.ipynb")
    return read_notebook(nb_full_path)


@pytest.fixture()
def script(notebook):
    return notebook_to_script(notebook)
