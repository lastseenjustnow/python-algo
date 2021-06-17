from typing import Optional

from BinaryTreeNode import BinaryTreeNode
from InorderIterator import InorderIterator


# Check if Two Binary Trees are Identical
def are_identical(root1: BinaryTreeNode, root2: BinaryTreeNode) -> bool:
    if root1 is None and root2 is not None:
        return False
    if root1 is not None and root2 is None:
        return False
    if root1 is None and root2 is None:
        return True

    return are_identical(root1.left, root2.left) \
        and are_identical(root1.right, root2.right)\
        and root1.data == root2.data


# In-order Successor of Binary Search Tree
def inorder_successor_bst(root: BinaryTreeNode, d: int) -> Optional[int]:
    potential_next = None
    while root.data != d:
        if d < root.data:
            potential_next = root.data
            root = root.left
        else:
            root = root.right

    if root.right:
        right_tree = root.right
        while right_tree:
            potential_next = right_tree.data
            right_tree = right_tree.left

    return potential_next
