import unittest

from solutions import *

profit_1 = [60, 100, 120]
profits_length_1 = 3
weight_1 = [10, 20, 30]
capacity_1 = 50

profit_2 = [1, 2, 2, 4, 10]
profits_length_2 = 5
weight_2 = [1, 1, 2, 12, 4]
capacity_2 = 15


class TestGraphAlgorithmsSolution(unittest.TestCase):

    # Challenge 1: The 0/1 Knapsack Problem
    def test_knap_sack_brute_force_iterative(self):
        self.assertEqual(220, knap_sack_brute_force_iterative(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_brute_force_iterative(profit_2, profits_length_2, weight_2, capacity_2))

    def test_knap_sack_brute_force_recursive(self):
        self.assertEqual(220, knap_sack_brute_force_recursive(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_brute_force_recursive(profit_2, profits_length_2, weight_2, capacity_2))

    def test_knap_sack_memoization(self):
        self.assertEqual(220, knap_sack_memoization(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_memoization(profit_2, profits_length_2, weight_2, capacity_2))

    def test_knap_sack_tabularization(self):
        self.assertEqual(220, knap_sack_tabularization(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_tabularization(profit_2, profits_length_2, weight_2, capacity_2))

    def test_knap_sack_tabularization_optimized(self):
        self.assertEqual(220, knap_sack_tabularization_optimized(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_tabularization_optimized(profit_2, profits_length_2, weight_2, capacity_2))

    # Challenge 2: Staircase Problem
    def test_count_ways_brute_force(self):
        self.assertEqual(4, count_ways_brute_force(3))
        self.assertEqual(7, count_ways_brute_force(4))
        self.assertEqual(13, count_ways_brute_force(5))

    def test_count_ways_memoization(self):
        self.assertEqual(4, count_ways_memoization(3))
        self.assertEqual(7, count_ways_memoization(4))
        self.assertEqual(13, count_ways_memoization(5))

    def test_count_ways_tabularization(self):
        self.assertEqual(4, count_ways_tabularization(3))
        self.assertEqual(7, count_ways_tabularization(4))
        self.assertEqual(13, count_ways_tabularization(5))

    def test_count_ways_tabularization_optimized(self):
        self.assertEqual(4, count_ways_tabularization_optimized(3))
        self.assertEqual(7, count_ways_tabularization_optimized(4))
        self.assertEqual(13, count_ways_tabularization_optimized(5))

    # Challenge 3: The Partition Problem
    def test_can_partition_brute_force(self):
        self.assertTrue(can_partition_brute_force([1, 2, 3, 4]))
        self.assertTrue(can_partition_brute_force([1, 1, 3, 4, 7]))
        self.assertFalse(can_partition_brute_force([2, 3, 4, 6]))

    def test_can_partition_tabularization_optimized(self):
        self.assertTrue(can_partition_tabularization_optimized([1, 2, 3, 4]))
        self.assertTrue(can_partition_tabularization_optimized([1, 1, 3, 4, 7]))
        self.assertFalse(can_partition_tabularization_optimized([2, 3, 4, 6]))

    # Challenge 6: Longest Palindromic Subsequence
    def test_longest_palindromic_subsequence(self):
        self.assertEqual(3, longest_palindromic_subsequence_recursive_brute_force('aabca'))
        self.assertEqual(5, longest_palindromic_subsequence_recursive_brute_force('abdbca'))
        self.assertEqual(7, longest_palindromic_subsequence_recursive_brute_force('abadabaca'))

    def test_longest_palindromic_subsequence_memoization(self):
        self.assertEqual(3, longest_palindromic_subsequence_memoization('aabca'))
        self.assertEqual(5, longest_palindromic_subsequence_memoization('abdbca'))
        self.assertEqual(7, longest_palindromic_subsequence_memoization('abadabaca'))


    # Challenge 7: The Coin Change Problem
    def test_count_change_brute_force_recursive(self):
        self.assertEqual(18, count_change_brute_force_recursive([25, 10, 5, 1], 4, 30))
        self.assertEqual(4, count_change_brute_force_recursive([25, 10, 5, 1], 4, 10))
        self.assertEqual(13, count_change_brute_force_recursive([25, 10, 5, 1], 4, 28))
        self.assertEqual(121, count_change_brute_force_recursive([25, 10, 5, 1], 4, 75))

    def test_count_change_memoization(self):
        self.assertEqual(18, count_change_memoization([25, 10, 5, 1], 4, 30))
        self.assertEqual(4, count_change_memoization([25, 10, 5, 1], 4, 10))
        self.assertEqual(13, count_change_memoization([25, 10, 5, 1], 4, 28))
        self.assertEqual(121, count_change_memoization([25, 10, 5, 1], 4, 75))

    def test_count_change_tabularization(self):
        self.assertEqual(18, count_change_tabularization([25, 10, 5, 1], 4, 30))
        self.assertEqual(4, count_change_tabularization([25, 10, 5, 1], 4, 10))
        self.assertEqual(13, count_change_tabularization([25, 10, 5, 1], 4, 28))
        self.assertEqual(121, count_change_tabularization([25, 10, 5, 1], 4, 75))

    def test_count_change_tabularization_optimized(self):
        self.assertEqual(18, count_change_tabularization_optimized([25, 10, 5, 1], 4, 30))
        self.assertEqual(4, count_change_tabularization_optimized([25, 10, 5, 1], 4, 10))
        self.assertEqual(13, count_change_tabularization_optimized([25, 10, 5, 1], 4, 28))
        self.assertEqual(121, count_change_tabularization_optimized([25, 10, 5, 1], 4, 75))

