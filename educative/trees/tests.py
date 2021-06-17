import unittest

from BinaryTreeNode import create_BST
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
        lst2 = [25, 50, 75, 100, 125, 200, 350]
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

    # Write an In-Order Iterator for a Binary Tree
    def test_inorder_using_iterator(self):
        arr = sorted([25, 125, 200, 300, 75, 50, 12, 35, 60, 75])
        root = create_BST(arr)
        expected_result = "12 25 35 50 60 75 75 125 200 300 "
        function_result = InorderIterator(root).inorder_using_iterator()
        self.assertEqual(expected_result, function_result)
