import unittest
import random

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