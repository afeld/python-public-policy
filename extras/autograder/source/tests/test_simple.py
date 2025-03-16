import unittest
from gradescope_utils.autograder_utils.decorators import weight, number


class TestSimpleArithmetic(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_eval_add(self):
        """Evaluate 1 + 1"""
        self.assertEqual(1+1, 2)
