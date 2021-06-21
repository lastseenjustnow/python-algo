from typing import List, Optional

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


# Challenge 6: Check if a Path Exists Between Two Vertices
def check_path(g, source, destination):
    traversed = [False] * g.vertices
    # Write your code here
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        vertex_id = stack.pop()
        if vertex_id == destination:
            return True
        traversed[vertex_id] = True
        vertex_head = g.array[vertex_id].get_head()
        while vertex_head:
            if not traversed[vertex_head.data]:
                stack.push(vertex_head.data)
            vertex_head = vertex_head.next_element

    return False


# Challenge 7: Check if a Given Undirected Graph is Tree
# Stack approach
def is_tree(g):
    visited = [False] * g.vertices

    stack = MyStack()
    stack.push(0)

    parent_stack = MyStack()
    parent_stack.push(None)

    while not stack.is_empty():
        vertex_id = stack.pop()
        parent_vertex_id = parent_stack.pop()
        vertex_head = g.array[vertex_id].get_head()
        while vertex_head:
            if vertex_head.data == parent_vertex_id:
                pass
            elif visited[vertex_head.data]:
                return False
            else:
                stack.push(vertex_head.data)
                parent_stack.push(vertex_id)
            vertex_head = vertex_head.next_element
        visited[vertex_id] = True

    if not all(visited):
        return False

    return True


# Recursive approach
def is_tree_recursive(g):

    visited = [False] * g.vertices

    def go_deep(vertex_id: int, parent_vertex_id: Optional[int], v: List[bool]):
        v[vertex_id] = True
        vertex_head = g.array[vertex_id].get_head()
        while vertex_head:
            if vertex_head.data == parent_vertex_id:
                pass
            elif v[vertex_head.data]:
                return False
            else:
                go_deep(vertex_head.data, vertex_id, v)
            vertex_head = vertex_head.next_element
        return True

    res = go_deep(0, None, visited)
    if not all(visited):
        return False

    return res