from Graph import Graph
from educative.linked_lists.LinkedList import LinkedList, Node
from educative.stacks_n_queues.Queue import MyQueue


# Challenge 1: Implement Breadth First Search
def bfs_traversal(g: Graph, source: int):
    result = ""
    q = MyQueue()
    q.enqueue(source)
    while not q.is_empty():
        q_front: int = q.front()
        vertex: LinkedList = g.array[q_front]
        vertex_head: Node = vertex.get_head()
        result += str(q_front)

        while vertex_head:
            q.enqueue(vertex_head.data)
            vertex_head = vertex_head.next_element

        q.dequeue()

    return result
