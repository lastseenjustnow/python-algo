import unittest

from solutions import *


class TestDynamicProgramming(unittest.TestCase):

    # Largest Sum Subarray
    def test_find_max_sum_sub_array(self):
        arr = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
        self.assertEqual(12, find_max_sum_sub_array(arr))
        arr = [1, 10, -1, 11, 5, -30, -7, 20, 25, -35]
        self.assertEqual(45, find_max_sum_sub_array(arr))
        arr = [-15, -14, -10, -19, -5, -21, -10]
        self.assertEqual(-5, find_max_sum_sub_array(arr))

    # MaxSum Subsequence - Nonadjacent Elements
    def test_find_max_sum_nonadjacent(self):
        arr1 = [1, 6, 10, 14, -5, -1, 2, -1, 3]
        self.assertEqual(25, find_max_sum_nonadjacent(arr1))
        arr2 = [1, -1, 6, -4, 2, 2]
        self.assertEqual(9, find_max_sum_nonadjacent(arr2))
        arr3 = [1, 6, 10, 14, 50, -20, -5, -10]
        self.assertEqual(61, find_max_sum_nonadjacent(arr3))

    # Find Combinations for Game Scoring
    def test_scoring_options(self):
        inputs, expected_results = [3, 4, 5], [3, 6, 10]
        for x, y in zip(inputs, expected_results):
            self.assertEqual(scoring_options(x), y)

    # Equal Subset Sum Partition
    def test_can_partition(self):
        self.assertTrue(can_partition([1, 2, 3, 4]))
        self.assertTrue(can_partition([1, 1, 3, 4, 7]))
        self.assertFalse(can_partition([2, 3, 4, 6]))

    def test_can_partition_subset_sum(self):
        self.assertTrue(can_partition_subset_sum([1, 2, 3, 7], 6))
        self.assertTrue(can_partition_subset_sum([1, 2, 7, 1, 5], 10))
        self.assertFalse(can_partition_subset_sum([1, 3, 4, 8], 6))
