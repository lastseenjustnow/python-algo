from educative.stacks_n_queues.Stack import MyStack


class InorderIterator:
    def __init__(self, root):
        self.root = root
        self.stk = MyStack()
        # Assuming that when iterator is initialized
        # it is always at the first element of tree in its in-order
        self.populate_iterator(root)
        return

    def populate_iterator(self, root):
        while root is not None:
            self.stk.push(root)
            root = root.left

    def hasNext(self):
        return False if self.stk.is_empty() else True

    def getNext(self):
        if self.stk.is_empty():
            return None

        r_val = self.stk.pop()
        temp = r_val.right
        self.populate_iterator(temp)

        return r_val

    # In-Order Iterator for a Binary Tree
    def inorder_using_iterator(self):
        result = ""
        while self.hasNext():
            ptr = self.getNext()
            result += str(ptr.data) + " "
        return result
