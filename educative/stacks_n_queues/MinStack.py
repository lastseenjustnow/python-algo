from Stack import MyStack


# Challenge 9: min( ) Function Using a Stack
class MinStack:
    # Constructor
    def __init__(self):
        self.mainStack = MyStack()
        self.minStack = MyStack()

    def pop(self):
        v = self.mainStack.pop()
        self.minStack.pop()
        return v

    # Pushes value into new stack
    def push(self, value):
        self.mainStack.push(value)
        if self.minStack.is_empty() or value < self.minStack.peek():
            self.minStack.push(value)
        else:
            self.minStack.push(self.minStack.peek())

    # Returns minimum value from new stack in constant time
    def min(self):
        return self.minStack.peek()
