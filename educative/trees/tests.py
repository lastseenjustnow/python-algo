import unittest
import random

from BinaryTreeNode import create_BST
from educative.trees.InorderIterator import InorderIterator
from solutions import *


class TestStackSolution(unittest.TestCase):

    # Check if Two Binary Trees are Identical
    def test_are_identical(self):
        lst = [25, 50, 75, 100, 125, 200, 300]
        tree1 = create_BST(lst)

        tree2 = BinaryTreeNode(100)
        tree2.left = BinaryTreeNode(50)
        tree2.left.left = BinaryTreeNode(25)
        tree2.left.right = BinaryTreeNode(75)
        tree2.right = BinaryTreeNode(200)
        tree2.right.left = BinaryTreeNode(125)
        tree2.right.right = BinaryTreeNode(300)

        self.assertTrue(are_identical(tree1, tree2))

        lst1 = [25, 50, 75, 100, 125, 200, 350]
        lst2 = [25, 50, 75, 100, 125, 200, 355]
        tree1 = create_BST(lst1)
        tree2 = create_BST(lst2)

        self.assertFalse(are_identical(tree1, tree2))

        tree1 = BinaryTreeNode(100)
        tree1.left = BinaryTreeNode(50)
        tree1.left.left = BinaryTreeNode(25)
        tree1.right = BinaryTreeNode(200)
        tree1.right.left = BinaryTreeNode(125)
        tree1.right.right = BinaryTreeNode(350)

        tree2 = BinaryTreeNode(100)
        tree2.left = BinaryTreeNode(50)
        tree2.left.right = BinaryTreeNode(25)
        tree2.right = BinaryTreeNode(200)
        tree2.right.left = BinaryTreeNode(125)
        tree2.right.right = BinaryTreeNode(350)

        self.assertFalse(are_identical(tree1, tree2))

    # In-Order Iterator for a Binary Tree
    def test_inorder_using_iterator(self):
        arr = sorted([25, 125, 200, 300, 75, 50, 12, 35, 60, 75])
        root = create_BST(arr)
        expected_result = "12 25 35 50 60 75 75 125 200 300 "
        function_result = InorderIterator(root).inorder_using_iterator()
        self.assertEqual(expected_result, function_result)

    def test_inorder_successor_bst(self):
        arr = sorted(list(set([random.randint(-1000, 1000) for _ in range(random.randint(0, 100000))])))
        root = create_BST(arr)
        for i, el in enumerate(arr[:-1], 0):
            self.assertEqual(arr[i+1], inorder_successor_bst(root, el))

    def test_level_order_traversal(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.right = BinaryTreeNode(200)
        root.right.right = BinaryTreeNode(350)

        function_res = level_order_traversal(root)
        expected_res = "100\n50 200\n25 75 350"
        self.assertEqual(expected_res, function_res)

    def test_traverse(self):
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(9)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)

        function_res = traverse(root)
        expected_res = deque([[9, 10, 5], [7, 1], [12]])

        self.assertEqual(expected_res, function_res)

    def test_find_level_averages(self):
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(9)
        root.left.right = BinaryTreeNode(2)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)

        function_res = find_level_averages(root)
        expected_res = [12.0, 4.0, 6.5]

        self.assertEqual(expected_res, function_res)

    def test_find_successor(self):
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(9)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)

        self.assertEqual(7, find_successor(root, 12))
        self.assertEqual(10, find_successor(root, 9))

    def test_zigzag_traverse(self):
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(7)

        expected_res = [[1], [3, 2], [4, 5, 6, 7]]
        function_res = zigzag_traverse(root)

        self.assertEqual(expected_res, function_res)

        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(9)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)
        root.right.left.left = BinaryTreeNode(20)
        root.right.left.right = BinaryTreeNode(17)

        expected_res = [[12], [1, 7], [9, 10, 5], [17, 20]]
        function_res = zigzag_traverse(root)

        self.assertEqual(expected_res, function_res)

    def test_connect_level_order_siblings(self):
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(7)

        connect_level_order_siblings(root)
        self.assertIsNone(root.next)
        self.assertEqual(7, root.right.left.next.data)

    def test_is_bst(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.right = BinaryTreeNode(200)
        root.right.left = BinaryTreeNode(125)
        root.right.right = BinaryTreeNode(350)

        self.assertTrue(is_bst(root))

        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.right = BinaryTreeNode(200)
        root.right.left = BinaryTreeNode(90)
        root.right.right = BinaryTreeNode(350)

        self.assertFalse(is_bst(root))

        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(110)
        root.right = BinaryTreeNode(200)
        root.right.left = BinaryTreeNode(150)
        root.right.right = BinaryTreeNode(350)

        self.assertFalse(is_bst(root))

    def test_convert_to_linked_list(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.right = BinaryTreeNode(200)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.left.left.right = BinaryTreeNode(30)
        root.left.right.left = BinaryTreeNode(60)
        root.left.right.left.left = BinaryTreeNode(55)
        root.right.left = BinaryTreeNode(125)
        root.right.right = BinaryTreeNode(350)

        res_root = convert_to_linked_list(root)
        expected_results = [25, 30, 50, 55, 60, 75, 100, 125, 200, 350]

        for result in expected_results:
            self.assertEqual(result, res_root.data)
            res_root = res_root.right

    def test_display_tree_perimeter(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.right = BinaryTreeNode(200)
        root.left.left = BinaryTreeNode(25)
        root.left.left.left = BinaryTreeNode(10)
        root.left.right = BinaryTreeNode(60)
        root.left.right.right = BinaryTreeNode(70)
        root.right = BinaryTreeNode(200)
        root.right.right = BinaryTreeNode(350)
        root.right.right.right = BinaryTreeNode(400)

        expected_result = '100 50 25 10 70 400 350 200 '

        self.assertEqual(expected_result, display_tree_perimeter(root))

    def test_populate_sibling_pointers(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.right = BinaryTreeNode(200)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.right.right = BinaryTreeNode(300)
        root.right.right.right = BinaryTreeNode(350)

        expected_results = [100, 50, 200, 25, 75, 300, 350]
        populate_sibling_pointers(root)
        for result in expected_results:
            self.assertEqual(result, root.data)
            root = root.right

    def test_serializer(self):
        arr = [100, 50, 200, 25, 75, 125, 350]
        root = create_BST(arr)
        output = open('data.class', 'wb')
        p = pickle.Pickler(output)
        serialize(root, p)
        output.close()
        input2 = open('data.class', 'rb')
        root_deserialized = deserialize(input2)
        self.assertEqual(25, root_deserialized.data)
        input2.close()
