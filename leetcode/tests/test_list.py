import unittest
import random

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


