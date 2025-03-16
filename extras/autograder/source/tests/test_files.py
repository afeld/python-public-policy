"""https://github.com/gradescope/gradescope-utils/tree/master/gradescope_utils/autograder_utils#readme"""

from unittest import TestCase
import os
from gradescope_utils.autograder_utils.decorators import number


class TestFiles(TestCase):
    @number("1.1")
    def test_notebook_and_py_file(self):
        """There should be exactly one notebook and one Python file submitted"""

        files = os.listdir("/autograder/submission")
        extensions = [os.path.splitext(filename)[1] for filename in files]
        extensions.sort()
        self.assertListEqual(
            extensions, [".ipynb", ".py"], f"Files submitted: {', '.join(files)}"
        )
