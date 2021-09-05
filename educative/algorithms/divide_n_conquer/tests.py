import unittest

from solutions import *


class TestDivideNConquerAlgorithmsSolution(unittest.TestCase):

    # Challenge 2: Find the Peak Element
    def test_find_peak(self):
        lst = [18, 34, 40, 37, 94, 8]
        self.assertTrue(find_peak(lst) in [40, 94])
        lst = [47, 85, 85, 35, 49, 49]
        self.assertTrue(find_peak(lst) in [85, 49])
        lst = [77, 54, 101, 40, 27, 62]
        self.assertTrue(find_peak(lst) in [101, 77])

    # Challenge 3: Maximum Sum Sublist of Size K
    def test_max_sub_list_of_size_k(self):
        self.assertEqual(9, max_sub_list_of_size_k([2, 1, 5, 1, 3, 2], 3))
        self.assertEqual(7, max_sub_list_of_size_k([2, 3, 4, 1, 5], 2))

    # Challenge 4: Collect Coins in Minimum Steps
    def test_minimum_steps(self):
        lst = [2, 5, 1, 2, 3, 1]
        self.assertEqual(5, minimum_steps(lst))
        lst = [2, 1, 2, 5, 1]
        self.assertEqual(4, minimum_steps(lst))

    # Challenge 5: Find the Floor and Ceil of a Number in a Sorted List
    def test_find_floor_ceiling(self):
        lst = [1, 2, 3, 5, 7]
        self.assertEqual((2, 5), find_floor_ceiling(lst, 3))
        lst = [0, 1, 2, 5]
        self.assertEqual((5, -1), find_floor_ceiling(lst, 6))
        lst = [1, 2, 3, 5, 7]
        self.assertEqual((3, 5), find_floor_ceiling(lst, 4))

    # Challenge 7: Find the Closest Number
    def test_find_closest(self):
        lst = [-9, -4, -2, 0, 1, 3, 4, 10]
        self.assertEqual(4, find_closest(lst, 5))
        lst = [1, 2, 5, 10, 23, 25, 30, 50]
        find_closest(lst, 100)
