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
