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
    def test_can_partition_minimum_subset_sum_difference_brute_force(self):
        arr1 = [1, 2, 3, 9]
        expected_result1 = ([1, 2, 3], [9])
        self.assertEqual(expected_result1, can_partition_minimum_subset_sum_difference(arr1))

        arr2 = [1, 2, 7, 1, 5]
        expected_result2 = ([1, 2, 5], [7, 1])
        self.assertEqual(expected_result2, can_partition_minimum_subset_sum_difference(arr2))

        arr3 = [1, 3, 100, 4]
        expected_result3 = ([1, 3, 4], [100])
        self.assertEqual(expected_result3, can_partition_minimum_subset_sum_difference(arr3))

    def test_can_partition_minimum_subset_sum_difference_memoization(self):
        arr1 = [1, 2, 3, 9]
        expected_result1 = 3
        self.assertEqual(expected_result1, can_partition_minimum_subset_sum_difference(arr1))

        arr2 = [1, 2, 7, 1, 5]
        expected_result2 = 0
        self.assertEqual(expected_result2, can_partition_minimum_subset_sum_difference(arr2))

        arr3 = [1, 3, 100, 4]
        expected_result3 = 92
        self.assertEqual(expected_result3, can_partition_minimum_subset_sum_difference(arr3))

    def test_length_of_longest_substring_naive(self):
        arr1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
        self.assertEqual(6, length_of_longest_substring_naive(arr1, 2))

        arr2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
        self.assertEqual(9, length_of_longest_substring_naive(arr2, 3))

    def test_length_of_longest_substring(self):
        arr1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
        self.assertEqual(6, length_of_longest_substring(arr1, 2))

        arr2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
        self.assertEqual(9, length_of_longest_substring(arr2, 3))

    def test_solve_knapsack(self):
        profits1 = [15, 20, 50]
        weights1 = [1, 2, 3]
        capacity1 = 5

        self.assertEqual(80, solve_knapsack(profits1, weights1, capacity1))
        profits2 = profits3 = [15, 50, 60, 90]
        weights2 = weights3 = [1, 3, 4, 5]

        self.assertEqual(140, solve_knapsack(profits2, weights2, 8))
        self.assertEqual(105, solve_knapsack(profits3, weights3, 6))

    def test_count_ribbon_pieces(self):
        arrs = [
            [2, 3, 5],
            [2, 3],
            [3, 5, 7],
            [7, 3, 5],
            [6, 3, 9, 3],
            [3, 5]
        ]
        targets = [5, 7, 13, 13, 9, 7]
        ress = [2, 3, 3, 3, 3, -1]

        for i in range(len(arrs)):
            self.assertEqual(ress[i], count_ribbon_pieces(arrs[i], targets[i]))

    def test_find_max_steal(self):
        arr1 = [2, 5, 1, 3, 6, 2, 4]
        self.assertEqual(15, find_max_steal(arr1))

        arr2 = [2, 10, 14, 8, 1]
        self.assertEqual(18, find_max_steal(arr2))

    def test_find_minimum_deletions(self):
        arrs = [
            [4, 2, 3, 6, 10, 1, 12],
            [-4, 10, 3, 7, 15],
            [3, 2, 1, 0],
            [-4, 6, 7, 8, -2, -1, 0, 1, -6, -5],
            [-4, 6, -2, 10, -1, 12, 0],
            [-4, 6, -2, 10, -1, 12, 0, 1],
            [-4, 6, -2, 10, -1, 12, 0, 1, 13]
        ]
        results = [2, 1, 3, 5, 3, 3, 3]
        for i, arr in enumerate(arrs, 0):
            self.assertEqual(results[i], find_minimum_deletions(arr))

    def test_palindromic_partitioning(self):
        ss = ['abdbca', 'cddpd', 'pqr', 'pp']
        ress = [3, 2, 2, 0]
        for s, res in zip(ss, ress):
            self.assertEqual(res, palindromic_partitioning(s))

    def test_find_LBS_length(self):
        arrs = [
            [4, 2, 3, 6, 10, 1, 12],
            [4, 2, 5, 9, 7, 6, 10, 3, 1]
        ]
        results = [5, 7]
        for i, arr in enumerate(arrs, 0):
            self.assertEqual(results[i], find_LBS_length(arr))

    def test_find_min_operations(self):
        self.assertEqual(1, find_min_operations('bat', 'but'))
        self.assertEqual(2, find_min_operations('abdca', 'cbda'))
        self.assertEqual(3, find_min_operations('passpot', 'ppsspqrt'))

    def test_find_SI(self):
        m, n, p = "abd", "cef", "abcdef"
        self.assertTrue(find_SI(m, n, p))

        m, n, p = "abd", "cef", "adcbef"
        self.assertFalse(find_SI(m, n, p))

        m, n, p = "abc", "def", "abdccf"
        self.assertFalse(find_SI(m, n, p))

        m, n, p = "abcdef", "mnop", "mnaobcdepf"
        self.assertTrue(find_SI(m, n, p))
