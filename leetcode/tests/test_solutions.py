import unittest
import random

from leetcode.linked_lists.leetcode_solutions import *


class TestSolution(unittest.TestCase):

    global s
    s = Solution()

    # 2. Add Two Numbers
    def test_addTwoNumbers(self):
        def reverse_int(x):
            return list(map(int, str(x)[::-1]))

        def addTwoNumbers_test(int1, int2):
            linked_list1 = ListNode().from_list(reverse_int(int1))
            linked_list2 = ListNode().from_list(reverse_int(int2))

            function_output = s.addTwoNumbers(linked_list1, linked_list2)
            expected_result = reverse_int(int1 + int2)
            return function_output.to_list() == expected_result


        for _ in range(0, 50000):
            int1 = random.randint(0, 1000000)
            int2 = random.randint(0, 1000000)
            self.assertTrue(addTwoNumbers_test(int1, int2))

    # 3. Longest Substring Without Repeating Characters
    def test_lengthOfLongestSubstring(self):
        test_list = ["abcabcbb", "bbbbb", "pwwkew", "", "aab", "dvdf"]
        expected_results_list = [3, 1, 3, 0, 2, 3]
        for string, result in zip(test_list, expected_results_list):
            self.assertEqual(s.lengthOfLongestSubstring(string), result)