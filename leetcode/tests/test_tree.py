import unittest

from leetcode.solutions.tree import *


class TestLinkedListSolution(unittest.TestCase):

    global s
    s = TreeSolution()

    # 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
    def test_getTargetCopy(self):
        tree1 = TreeNode(7)
        tree1.left = TreeNode(4)
        tree1.right = TreeNode(3)
        tree1.right.left = TreeNode(6)
        tree1.right.right = TreeNode(19)

        target = tree1.right

        tree2 = TreeNode(7)
        tree2.left = TreeNode(4)
        tree2.right = TreeNode(3)
        tree2.right.left = TreeNode(6)
        tree2.right.right = TreeNode(19)

        res = s.getTargetCopy(tree1, tree2, target)
        self.assertEqual(res.val, 3)

        tree3 = TreeNode(1)
        tree3.left = TreeNode(2)
        tree3.right = TreeNode(3)
        tree3.left.left = TreeNode(4)
        tree3.left.right = TreeNode(5)
        tree3.right.left = TreeNode(6)
        tree3.right.right = TreeNode(7)
        tree3.left.left.left = TreeNode(8)
        tree3.left.left.right = TreeNode(9)
        tree3.left.right.left = TreeNode(10)

        target = tree3.left.right

        tree4 = TreeNode(1)
        tree4.left = TreeNode(2)
        tree4.right = TreeNode(3)
        tree4.left.left = TreeNode(4)
        tree4.left.right = TreeNode(5)
        tree4.right.left = TreeNode(6)
        tree4.right.right = TreeNode(7)
        tree4.left.left.left = TreeNode(8)
        tree4.left.left.right = TreeNode(9)
        tree4.left.right.left = TreeNode(10)

        res = s.getTargetCopy(tree3, tree4, target)
        self.assertEqual(res.val, 5)

