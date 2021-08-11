from Stack import MyStack


# Challenge 4: Implement a Queue Using Stacks
class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        return self.main_stack.push(value)

    # Removes Element From Queue
    def dequeue(self):
        new_stack = MyStack()
        for i in range(self.main_stack.size() - 1):
            new_stack.push(self.main_stack.pop())
        v = self.main_stack.pop()
        while not new_stack.is_empty():
            self.main_stack.push(new_stack.pop())
        return v