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

    # Subset Sum
    def test_can_partition_subset_sum(self):
        self.assertTrue(can_partition_subset_sum([1, 2, 3, 7], 6))
        self.assertTrue(can_partition_subset_sum([1, 2, 7, 1, 5], 10))
        self.assertFalse(can_partition_subset_sum([1, 3, 4, 8], 6))

    # Minimum Subset Sum Difference
    # Brute force
    def test_can_partition_minumum_subset_sum_difference_brute_force(self):
        arr1 = [1, 2, 3, 9]
        expected_result1 = ([1, 2, 3], [9])
        self.assertEqual(expected_result1, can_partition_minumum_subset_sum_difference(arr1))

        arr2 = [1, 2, 7, 1, 5]
        expected_result2 = ([1, 2, 5], [7, 1])
        self.assertEqual(expected_result2, can_partition_minumum_subset_sum_difference(arr2))

        arr3 = [1, 3, 100, 4]
        expected_result3 = ([1, 3, 4], [100])
        self.assertEqual(expected_result3, can_partition_minumum_subset_sum_difference(arr3))

    def test_can_partition_minumum_subset_sum_difference_memoization(self):
        arr1 = [1, 2, 3, 9]
        expected_result1 = 3
        self.assertEqual(expected_result1, can_partition_minumum_subset_sum_difference(arr1))

        arr2 = [1, 2, 7, 1, 5]
        expected_result2 = 0
        self.assertEqual(expected_result2, can_partition_minumum_subset_sum_difference(arr2))

        arr3 = [1, 3, 100, 4]
        expected_result3 = 92
        self.assertEqual(expected_result3, can_partition_minumum_subset_sum_difference(arr3))

    def test_length_of_longest_substring(self):
        arr1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
        self.assertEqual(6, length_of_longest_substring_naive(arr1, 2))

        arr2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
        self.assertEqual(9, length_of_longest_substring_naive(arr2, 3))