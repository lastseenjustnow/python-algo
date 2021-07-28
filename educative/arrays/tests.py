import unittest

from solutions import *


class TestArraySolution(unittest.TestCase):
    def test_find_max_sliding_window(self):
        arr = [-4, 2, -5, 3, 6]
        self.assertTrue([2, 3, 6], find_max_sliding_window(arr, 3))

        arr = [-4, 2, -5, 1, -1, 6]
        self.assertTrue([2, 2, 1, 6], find_max_sliding_window(arr, 3))
