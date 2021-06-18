from educative.stacks_n_queues.Stack import MyStack


class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def print_list(self):
        print([i for i in self.queue_list])

    def from_list(self, lst):
        for i in lst:
            self.enqueue(i)
        return self

    def to_list(self):
        return [i for i in self.queue_list]

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.queue_size

    def enqueue(self, value):
        self.queue_size += 1
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        self.queue_size -= 1
        return front

    # Challenge 3: Reversing First k Elements of Queue
    # Implementation using list
    def __reverseK_list(queue, k):
        # Write your code here
        if k > queue.size() or k < 0:
            return None

        l = []
        for i in range(0, k):
            l.append(queue.front())
            queue.dequeue()

        out = MyQueue()
        for i in l[::-1]:
            out.enqueue(i)

        h = queue.front()
        while h:
            out.enqueue(h)
            queue.dequeue()
            h = queue.front()

        return out

    # Correct implementation using Stack & Queue
    def reverseK(self, k):
        init_size = self.size()
        if k > init_size or k < 0:
            return None

        stack = MyStack()
        for _ in range(k):
            stack.push(self.dequeue())

        for _ in range(k):
            self.enqueue(stack.pop())

        for _ in range(init_size - k):
            self.enqueue(self.dequeue())

        return self




