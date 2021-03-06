import unittest
import random
from typing import Callable

from leetcode.solutions.list import *


class TestListSolution(unittest.TestCase):
    global s
    s = ListSolution()

    # 3. Longest Substring Without Repeating Characters
    def test_lengthOfLongestSubstring(self):
        test_list = ["abcabcbb", "bbbbb", "pwwkew", "", "aab", "dvdf"]
        expected_results_list = [3, 1, 3, 0, 2, 3]
        for string, result in zip(test_list, expected_results_list):
            self.assertEqual(s.lengthOfLongestSubstring(string), result)

    # Merge Sorted Array
    def test_mergeSortedArray(self):
        for _ in range(0, 100000):
            lst1_len = random.randint(0, 10)
            lst2_len = random.randint(0, 10)
            lst1 = [random.randint(-100, 100) for _ in range(0, lst1_len)]
            lst1.sort()
            lst1 += [0] * lst2_len
            lst2 = [random.randint(-100, 100) for _ in range(0, lst2_len)]
            lst2.sort()
            expected_result = lst1[:lst1_len] + lst2
            expected_result.sort()
            s.mergeSortedArray(lst1, lst1_len, lst2, lst2_len)
            self.assertEqual(expected_result, lst1)

    # 56. Merge Intervals
    def test_merge_intervals(self):
        def test_merge_intervals_f(f: Callable):
            intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
            expected_output = [[1, 6], [8, 10], [15, 18]]
            function_output = f(intervals)
            self.assertEqual(expected_output, function_output)

            intervals = [[1, 4], [4, 5]]
            expected_output = [[1, 5]]
            function_output = f(intervals)
            self.assertEqual(expected_output, function_output)

            intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [10, 14]]
            expected_output = [[1, 6], [8, 14], [15, 18]]
            function_output = f(intervals)
            self.assertEqual(expected_output, function_output)

            intervals = [[1, 3], [-1, -1], [2, 6], [8, 10], [15, 18], [10, 14], [14, 15]]
            expected_output = [[-1, -1], [1, 6], [8, 18]]
            function_output = f(intervals)
            self.assertEqual(expected_output, function_output)

            intervals = [[1, 4], [0, 4]]
            expected_output = [[0, 4]]
            function_output = f(intervals)
            self.assertEqual(expected_output, function_output)

        test_merge_intervals_f(s.merge_intervals)
        test_merge_intervals_f(s.merge_intervals_in_place)

    # 200. Number of Islands
    def test_numIslands(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]

        grid_2 = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]

        grid_3 = [
            ["1", "1", "0", "1", "0"],
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "1"]
        ]

        grid_4 = [
            ["1", "0", "1", "1", "1"],
            ["1", "0", "1", "0", "1"],
            ["1", "1", "1", "0", "1"]
        ]

        self.assertEqual(1, s.numIslands(grid))
        self.assertEqual(3, s.numIslands(grid_2))
        self.assertEqual(3, s.numIslands(grid_3))
        self.assertEqual(1, s.numIslands(grid_4))
