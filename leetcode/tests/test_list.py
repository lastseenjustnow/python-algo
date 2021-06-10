import unittest
import random

from leetcode.solutions.list import *


class TestLinkedListSolution(unittest.TestCase):

    global s
    s = ListSolution()

    # 3. Longest Substring Without Repeating Characters
    def test_lengthOfLongestSubstring(self):
        test_list = ["abcabcbb", "bbbbb", "pwwkew", "", "aab", "dvdf"]
        expected_results_list = [3, 1, 3, 0, 2, 3]
        for string, result in zip(test_list, expected_results_list):
            self.assertEqual(s.lengthOfLongestSubstring(string), result)