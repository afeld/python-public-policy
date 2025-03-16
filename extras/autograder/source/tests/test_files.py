"""https://github.com/gradescope/gradescope-utils/tree/master/gradescope_utils/autograder_utils#readme"""

import os
from glob import glob
from unittest import TestCase

from gradescope_utils.autograder_utils.decorators import number

from tests.helpers import check_plots


def get_ext(filename):
    return os.path.splitext(filename)[1]


class TestFiles(TestCase):
    @number("1.1")
    def test_notebook_and_py_file(self):
        """There should be exactly one notebook and one Python file submitted"""

        files = os.listdir("/autograder/submission")
        extensions = [get_ext(filename) for filename in files]
        extensions.sort()
        self.assertListEqual(
            extensions, [".ipynb", ".py"], f"Files submitted: {', '.join(files)}"
        )

    @number("1.2")
    def test_plots(self):
        """Plots should be well-formatted"""

        scripts = glob("/autograder/submission/*.py")
        for filename in scripts:
            with open(filename) as f:
                source = f.read()

            check_plots(source)
