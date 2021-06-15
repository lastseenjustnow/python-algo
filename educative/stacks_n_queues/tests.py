import unittest
import random

from Queue import MyQueue
from NewQueue import NewQueue
from MinStack import MinStack
from educative.stacks_n_queues.solutions import *


class TestStackSolution(unittest.TestCase):

    def test_stack_implementation(self):
        stack_obj = MyStack()
        self.assertTrue(stack_obj.is_empty())
        self.assertIsNone(stack_obj.peek())
        self.assertEqual(0, stack_obj.size())

        for i in range(5):
            stack_obj.push(i)

        self.assertFalse(stack_obj.is_empty())
        self.assertEqual(4, stack_obj.peek())
        self.assertEqual(5, stack_obj.size())

        for i in range(5):
            stack_obj.pop()

        self.assertTrue(stack_obj.is_empty())
        self.assertIsNone(stack_obj.peek())
        self.assertEqual(0, stack_obj.size())

    def test_queue_implementation(self):
        queue_obj = MyQueue()
        self.assertTrue(queue_obj.is_empty())
        self.assertIsNone(queue_obj.front())
        self.assertIsNone(queue_obj.rear())
        self.assertEqual(0, queue_obj.size())

        for i in range(2, 11, 2):
            queue_obj.enqueue(i)

        self.assertFalse(queue_obj.is_empty())
        self.assertEqual(2, queue_obj.front())
        self.assertEqual(10, queue_obj.rear())

        queue_obj.dequeue()
        queue_obj.dequeue()

        self.assertEqual(6, queue_obj.front())
        self.assertEqual(10, queue_obj.rear())

    def test_challenge_3(self):
        for _ in range(50):
            leng = random.randint(0, 10000)
            k = random.randint(0, leng)
            lst = [random.randint(0, 10000) for _ in range(0, leng)]
            expected_result = lst[:k][::-1] + lst[k:]
            queue = MyQueue().from_list(lst)
            queue.reverseK(k)
            function_result = queue.to_list()
            self.assertTrue(expected_result, function_result)

    def test_challenge_4(self):
        q = NewQueue()
        lst = [i for i in range(2, 11, 2)]
        for i in range(2, 11, 2):
            q.enqueue(i)

        for el in lst:
            self.assertEqual(el, q.dequeue())

    def test_challenge_6(self):
        res = evaluate_post_fix("921*-8-4+")
        self.assertEqual(3, res)

        res = evaluate_post_fix("642/+")
        self.assertEqual(8, res)

    def test_challenge_7(self):
        lst = [4, 6, 3, 2, 8, 1]
        expected_result = [6, 8, 8, 8, -1, -1]
        function_output = next_greater_element(lst)
        self.assertEqual(expected_result, function_output)

    def test_challenge_9(self):
        lst = [5, 0, 2, 4, 1, 3, 0]
        stack = MinStack()
        for el in lst:
            stack.push(el)
        self.assertEqual(0, stack.min())
        stack.pop()
        stack.push(-2)
        self.assertEqual(-2, stack.min())
        stack.pop()
        self.assertEqual(0, stack.min())


