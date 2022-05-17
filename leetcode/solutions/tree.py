class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeSolution:

    # 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def rec(orig: TreeNode, clon: TreeNode):
            if not orig:
                return None
            if orig.val == target.val:
                return clon
            else:
                le = rec(orig.left, clon.left)
                if le is None:
                    return rec(orig.right, clon.right)
                else:
                    return le

        return rec(original, cloned)
