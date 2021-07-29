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
            lst = lst[rotate_arbitrary_number+1:] + lst[:rotate_arbitrary_number]
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
            lst = lst[rotate_arbitrary_number+1:] + lst[:rotate_arbitrary_number]
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
