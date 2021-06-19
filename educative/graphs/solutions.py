from typing import List

from Graph import Graph, UndirectedGraph
from educative.linked_lists.LinkedList import LinkedList, Node
from educative.stacks_n_queues.Queue import MyQueue
from educative.stacks_n_queues.Stack import MyStack


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


# Challenge 2: Depth First Search
# Recursive approach
def dfs_traversal_recursive(g: Graph, source: int) -> str:
    def rec(vertex: int, t: List[bool], res: str):
        if not t[vertex]:
            res += str(vertex)
            t[vertex] = True
            vertex_head = g.array[vertex].get_head()
            while vertex_head:
                res = rec(vertex_head.data, t, res)[0]
                vertex_head = vertex_head.next_element

        return res, t

    result, traversed = rec(source, [False] * g.vertices, "")

    for i, b in enumerate(traversed, 0):
        if not b:
            result += rec(i, traversed, "")[0]

    return result


# Stack approach
def dfs_traversal(g: Graph, source: int) -> str:

    is_traversed = [False] * g.vertices

    res = ""
    stack = MyStack()
    stack.push(source)

    while not stack.is_empty():
        current_vertex_id = stack.pop()
        res += str(current_vertex_id)
        is_traversed[current_vertex_id] = True
        current_vertex_head: Node = g.array[current_vertex_id].get_head()
        while current_vertex_head:
            if not is_traversed[current_vertex_head.data]:
                stack.push(current_vertex_head.data)
            current_vertex_head = current_vertex_head.next_element
        if stack.is_empty():
            for disjoined_vertex_id, is_visited in enumerate(is_traversed, 0):
                if not is_visited:
                    stack.push(disjoined_vertex_id)
                    break

    return res


# Challenge 3: Detect Cycle in a Directed Graph
# Recursive approach
def detect_cycle(g: Graph):
    outer_traversed_list = [False] * g.vertices

    def go_deep(vertex_id: int, inner_traversed_list):
        if inner_traversed_list[vertex_id]:
            return True
        inner_traversed_list[vertex_id] = True
        outer_traversed_list[vertex_id] = True
        vertex_head = g.array[vertex_id].get_head()
        if vertex_head:
            return go_deep(vertex_head.data, inner_traversed_list)
        else:
            return False

    while not all(outer_traversed_list):
        is_cycle = go_deep(outer_traversed_list.index(False), [False] * g.vertices)
        if is_cycle:
            return True

    return False


# Challenge 4: "Mother Vertex" in a Directed Graph
def find_mother_vertex(g):
    mother_vertex = -1
    for vertex_id in range(g.vertices):
        stack = MyStack()
        stack.push(vertex_id)
        count = 0
        while not stack.is_empty():
            vertex_head = g.array[stack.pop()].get_head()
            count += 1
            while vertex_head:
                stack.push(vertex_head.data)
                vertex_head = vertex_head.next_element
            if count >= g.vertices:
                mother_vertex = vertex_id
                break

    return mother_vertex


# Challenge 5: Count Number of Edges in an Undirected Graph
def num_edges(g: UndirectedGraph):
    visited = [False] * g.vertices
    num_edges = 0
    for vertex_id in range(g.vertices):
        visited[vertex_id] = True
        vertex_head = g.array[vertex_id].get_head()
        while vertex_head:
            if not visited[vertex_head.data]:
                num_edges += 1
            vertex_head = vertex_head.next_element
    return num_edges
