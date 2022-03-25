import ast
import os
import pytest
from .nb_helper import *


class InputChecker(ast.NodeVisitor):
    def __init__(self):
        self.num_inputs = 0

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == "input":
            self.num_inputs += 1


@pytest.fixture()
def notebook():
    nb_full_path = os.path.join(os.getcwd(), "hw_0.ipynb")
    return read_notebook(nb_full_path)


@pytest.fixture()
def script(notebook):
    return notebook_to_script(notebook)


@pytest.fixture()
def tree(script):
    return ast.parse(script)
