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