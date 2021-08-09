import unittest
import random

from collections import Counter
from itertools import accumulate

from solutions import *


class TestArraySolution(unittest.TestCase):
    # Find Maximum in Sliding Window
    def test_find_max_sliding_window(self):
        arr = [-4, 2, -5, 3, 6]
        self.assertTrue([2, 3, 6], find_max_sliding_window(arr, 3))

        arr = [-4, 2, -5, 1, -1, 6]
        self.assertTrue([2, 2, 1, 6], find_max_sliding_window(arr, 3))

    # Search a Rotated Array
    def test_binary_search_rotated(self):
        arr = [176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162]
        for index, elem in enumerate(arr, 0):
            self.assertEqual(index, binary_search_rotated(arr, elem))

        for _ in range(100):
            lst_len = random.randint(1, 100)
            rotate_arbitrary_number = random.randint(1, lst_len)
            lst = sorted(list(set([random.randint(-100, 100) for _ in range(lst_len)])))
            lst = lst[rotate_arbitrary_number + 1:] + lst[:rotate_arbitrary_number]
            for index, elem in enumerate(lst, 0):
                self.assertEqual(index, binary_search_rotated(lst, elem))

    def test_binary_search_rotated_iter(self):
        arr = [176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162]
        for index, elem in enumerate(arr, 0):
            self.assertEqual(index, binary_search_rotated_iter(arr, elem))

        for _ in range(100):
            lst_len = random.randint(1, 100)
            rotate_arbitrary_number = random.randint(1, lst_len)
            lst = sorted(list(set([random.randint(-100, 100) for _ in range(lst_len)])))
            lst = lst[rotate_arbitrary_number + 1:] + lst[:rotate_arbitrary_number]
            for index, elem in enumerate(lst, 0):
                self.assertEqual(index, binary_search_rotated_iter(lst, elem))

    def test_find_least_common_number(self):
        a = [6, 7, 10, 25, 30, 63, 64]
        b = [0, 4, 5, 6, 7, 8, 50]
        c = [1, 6, 10, 14]
        self.assertTrue(6, find_least_common_number(a, b, c))

        a = [1, 4, 6, 7, 8, 10, 14]
        b = [1, 4, 5, 6, 7, 8, 50]
        c = [0, 6, 7, 8, 10, 25, 30, 40]
        self.assertTrue(6, find_least_common_number(a, b, c))

        a = [1, 5, 6, 7, 17, 20]
        b = [3, 4, 7, 9, 12, 16, 50]
        c = [5, 6, 7, 10, 16, 25]
        self.assertTrue(7, find_least_common_number(a, b, c))

    def test_find_low_index(self):

        def test_array(arr):
            vals, indexes = Counter(arr).keys(), [0] + list(accumulate(Counter(arr).values()))[:-1]
            for elem, index in zip(vals, indexes):
                self.assertEqual(index, find_low_index(arr, elem))

        arr = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]
        test_array(arr)
        arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
        test_array(arr)

        for _ in range(100):
            arr = sorted([random.randint(-10000, 10000) for _ in range(1, 100)])
            test_array(arr)

    def test_find_high_index(self):

        def test_array(arr):
            vals, indexes = Counter(arr).keys(), [x - 1 for x in accumulate(Counter(arr).values())]
            for elem, index in zip(vals, indexes):
                self.assertEqual(index, find_high_index(arr, elem))

        arr = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]
        test_array(arr)
        arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
        test_array(arr)

        for _ in range(100):
            arr = sorted([random.randint(-10000, 10000) for _ in range(1, 100)])
            test_array(arr)

    def test_find_low_index_iter(self):
        def test_array(arr):
            vals, indexes = Counter(arr).keys(), [0] + list(accumulate(Counter(arr).values()))[:-1]
            for elem, index in zip(vals, indexes):
                self.assertEqual(index, find_low_index_iter(arr, elem))

        arr = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]
        test_array(arr)
        arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
        test_array(arr)

        for _ in range(100):
            arr = sorted([random.randint(-10000, 10000) for _ in range(1, 1000)])
            test_array(arr)

    def test_find_high_index_iter(self):

        def test_array(arr):
            vals, indexes = Counter(arr).keys(), [x - 1 for x in accumulate(Counter(arr).values())]
            for elem, index in zip(vals, indexes):
                self.assertEqual(index, find_high_index_iter(arr, elem))

        arr = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]
        test_array(arr)
        arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
        test_array(arr)

        for _ in range(100):
            arr = sorted([random.randint(-10000, 10000) for _ in range(1, 100)])
            test_array(arr)

    # Move All Zeros to the Beginning of the Array
    def test_move_zeros_to_left(self):
        A = [1, 10, 20, 0, 59, 63, 0, 88, 0]
        expected_result = [0, 0, 0, 1, 10, 20, 59, 63, 88]
        self.assertEqual(expected_result, move_zeros_to_left_naive(A))
        self.assertEqual(expected_result, move_zeros_to_left(A))

        B = [1, 10, -1, 11, 5, 0, -7, 0, 25, -35]
        expected_result = [0, 0, 1, 10, -1, 11, 5, -7, 25, -35]
        self.assertEqual(expected_result, move_zeros_to_left_naive(B))
        self.assertEqual(expected_result, move_zeros_to_left(B))

    def test_find_buy_sell_stock_prices(self):
        arr = [8, 5, 12, 9, 19, 1]
        self.assertEqual((5, 19), find_buy_sell_stock_prices(arr))

        arr = [21, 12, 11, 9, 6, 3]
        self.assertEqual((12, 11), find_buy_sell_stock_prices(arr))

        arr = [8, 6, 5, 4, 3, 2, 1]
        self.assertEqual((6, 5), find_buy_sell_stock_prices(arr))

        arr = [1, 2, 3, 4, 3, 2, 1, 2, 5]
        self.assertEqual((1, 5), find_buy_sell_stock_prices(arr))

    # Merge an Array With Overlapping Intervals
    def test_merge_intervals(self):
        arr = [Pair(1, 5), Pair(3, 7), Pair(4, 6), Pair(6, 8)]
        self.assertEqual(1, merge_intervals(arr)[0].first)
        self.assertEqual(8, merge_intervals(arr)[0].second)

        arr = [Pair(10, 12), Pair(12, 15)]
        self.assertEqual(10, merge_intervals(arr)[0].first)
        self.assertEqual(15, merge_intervals(arr)[0].second)

        arr = [Pair(1, 5), Pair(3, 7), Pair(4, 6), Pair(6, 8), Pair(10, 12), Pair(10, 15)]
        self.assertEqual(1, merge_intervals(arr)[0].first)
        self.assertEqual(8, merge_intervals(arr)[0].second)
        self.assertEqual(10, merge_intervals(arr)[1].first)
        self.assertEqual(15, merge_intervals(arr)[1].second)

    def test_cyclic_sort(self):
        input = [3, 1, 5, 4, 2]
        output = [1, 2, 3, 4, 5]
        self.assertEqual(output, cyclic_sort(input))

        input = [2, 6, 4, 3, 1, 5]
        output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(output, cyclic_sort(input))

        input = [1, 5, 6, 4, 3, 2]
        output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(output, cyclic_sort(input))

    def test_max_sub_array_of_size_k(self):
        arr = [2, 1, 5, 1, 3, 2]
        self.assertEqual(9, max_sub_array_of_size_k(3, arr))

        arr = [2, 3, 4, 1, 5]
        self.assertEqual(7, max_sub_array_of_size_k(2, arr))

    def test_smallest_subarray_with_given_sum(self):
        arr = [2, 1, 5, 2, 3, 2]
        self.assertEqual(2, smallest_subarray_with_given_sum(7, arr))

        arr = [2, 1, 5, 2, 8]
        self.assertEqual(1, smallest_subarray_with_given_sum(7, arr))

        arr = [3, 4, 1, 1, 6]
        self.assertEqual(3, smallest_subarray_with_given_sum(8, arr))

    def test_make_squares(self):
        arr = [-2, -1, 0, 2, 3]
        exp = [0, 1, 4, 4, 9]
        self.assertEqual(exp, make_squares(arr))

        arr = [-3, -1, 0, 1, 2]
        exp = [0, 1, 1, 4, 9]
        self.assertEqual(exp, make_squares(arr))

    def test_find_subsets(self):
        input = [1, 3, 3]
        output = [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
        self.assertEqual(output, find_subsets(input))

        input = [1, 5, 3, 3]
        output = [[], [1], [3], [1, 3], [3, 3], [1, 3, 3], [5], [1, 5], [3, 5], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]]
        self.assertEqual(output, find_subsets(input))

    def test_find_max_in_bitonic_array(self):
        input = [1, 3, 8, 12, 4, 2]
        self.assertEqual(12, find_max_in_bitonic_array(input))

        input = [3, 8, 3, 1]
        self.assertEqual(8, find_max_in_bitonic_array(input))

        input = [1, 3, 8, 12]
        self.assertEqual(12, find_max_in_bitonic_array(input))

        input = [10, 9, 8]
        self.assertEqual(10, find_max_in_bitonic_array(input))

    def test_find_permutations(self):
        input = [1, 3, 5]
        function_output = find_permutations(input)
        self.assertTrue(function_output.__contains__([1, 3, 5]))
        self.assertTrue(function_output.__contains__([1, 5, 3]))
        self.assertTrue(function_output.__contains__([3, 1, 5]))
        self.assertTrue(function_output.__contains__([3, 5, 1]))
        self.assertTrue(function_output.__contains__([5, 3, 1]))
        self.assertTrue(function_output.__contains__([5, 1, 3]))

    def test_search_triplets(self):
        input = [-3, 0, 1, 2, -1, 1, -2]
        output = [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
        self.assertEqual(output, search_triplets(input))

        input = [-5, 2, -1, -2, 3]
        output = [[-5, 2, 3], [-2, -1, 3]]
        self.assertEqual(output, search_triplets(input))

    def test_triplet_sum_close_to_target(self):
        input = [-2, 0, 1, 2]
        self.assertEqual(1, triplet_sum_close_to_target(input, 2))

        input = [-3, -1, 1, 2]
        self.assertEqual(0, triplet_sum_close_to_target(input, 1))

        input = [1, 0, 1, 1]
        self.assertEqual(3, triplet_sum_close_to_target(input, 100))

    def test_triplet_with_smaller_sum(self):
        input = [-1, 0, 2, 3]
        self.assertEqual(2, triplet_with_smaller_sum(input, 3))

        input = [-1, 4, 2, 1, 3]
        self.assertEqual(4, triplet_with_smaller_sum(input, 5))

    def test_find_subarrays(self):
        input = [2, 5, 3, 10]
        output = [[2], [5], [2, 5], [3], [5, 3], [10]]
        self.assertEqual(output, find_subarrays(input, 30))

        input = [8, 2, 6, 5]
        output = [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]
        self.assertEqual(output, find_subarrays(input, 50))