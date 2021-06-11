import unittest
import random

from leetcode.solutions.linked_list import *


class TestLinkedListSolution(unittest.TestCase):

    global s
    s = LinkedListSolution()

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

    # 1041. Robot Bounded In Circle
    def test_isRobotBounded(self):
        self.assertTrue(s.isRobotBounded("GGLLGG"))
        self.assertFalse(s.isRobotBounded("GG"))
        self.assertTrue(s.isRobotBounded("GL"))
