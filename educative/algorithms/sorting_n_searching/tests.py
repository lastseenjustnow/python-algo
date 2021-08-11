import unittest

from solutions import *


class TestArraySolution(unittest.TestCase):

    # Challenge 1: Find Two Numbers that Add up to "n"
    def test_find_sum(self):
        lst = [1, 21, 3, 14, 5, 60, 7, 6]
        n = 81

        self.assertEqual((21, 60), find_sum_brute_force(lst, n))
        self.assertEqual((21, 60), find_sum_sorting(lst, n))
        self.assertEqual((21, 60), find_sum_dictionary(lst, n))
        self.assertEqual((21, 60), find_sum_set(lst, n))

    def test_pivoted_binary_search(self):
        lst = [7, 8, 9, 0, 3, 5, 6]
        print(pivoted_binary_search(lst, 7, 3))