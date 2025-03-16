"""https://github.com/gradescope/gradescope-utils/tree/master/gradescope_utils/autograder_utils#readme"""

from unittest import TestCase
import os
from gradescope_utils.autograder_utils.decorators import number


class TestFiles(TestCase):
    @number("1.1")
    def test_notebook_and_py_file(self):
        """There should be exactly one notebook and one Python file submitted"""

        files = os.listdir("/autograder/submission")

        self.assertEqual(len(files), 2, "There should be exactly two files submitted.")

        for ext in [".ipynb", ".py"]:
            ext_files = [f for f in files if f.endswith(ext)]
            self.assertEqual(
                len(ext_files), 1, f"There should be exactly one {ext} file."
            )
