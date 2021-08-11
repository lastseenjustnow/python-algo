from typing import List, Optional, Dict, Set

from Graph import Graph, UndirectedGraph
from GraphNode import GraphNode
from educative.data_structures.linked_lists.LinkedList import LinkedList, Node
from educative.data_structures.stacks_n_queues.Queue import MyQueue
from educative.data_structures.stacks_n_queues.Stack import MyStack


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


# Challenge 8: Find the Shortest Path Between Two Vertices
# Stack approach
def find_min(g, source, destination):
    min = -1
    vertex_stack = MyStack()
    steps_stack = MyStack()
    vertex_stack.push(source)
    steps_stack.push(0)

    while not vertex_stack.is_empty():
        vertex_id = vertex_stack.pop()
        steps_num = steps_stack.pop()
        if vertex_id == destination and (min < 0 or steps_num < min):
            min = steps_num
        else:
            vertex_head = g.array[vertex_id].get_head()
            while vertex_head:
                vertex_stack.push(vertex_head.data)
                steps_stack.push(steps_num + 1)
                vertex_head = vertex_head.next_element

    return min


# Recursive approach
def find_min_recursive(g, source, destination):
    def go_deep(vertex_id: int, counter: int, path_length: int):
        if vertex_id == destination and (path_length < 0 or counter < path_length):
            return counter
        else:
            vertex_head = g.array[vertex_id].get_head()
            while vertex_head:
                go_further = go_deep(vertex_head.data, counter + 1, path_length)
                if path_length < 0 or go_further < path_length:
                    path_length = go_further
                vertex_head = vertex_head.next_element
            return path_length

    return go_deep(source, 0, -1)


# Clone a Directed Graph
def clone(root: GraphNode) -> GraphNode:
    def fill_rec(this_node: GraphNode, d_v: Dict[int, List[int]], d_n: Dict[int, GraphNode]):
        if d_v.get(this_node.data) is None:
            d_v[this_node.data] = [neighbor.data for neighbor in this_node.neighbors]
            d_n[this_node.data] = GraphNode(this_node.data)
        for neighbor in this_node.neighbors:
            if d_v.get(neighbor.data) is None:
                d_v, d_n = fill_rec(neighbor, d_v, d_n)
        return d_v, d_n

    d_values, d_nodes = fill_rec(root, dict(), dict())

    for value, node in d_nodes.items():
        node.neighbors = [d_nodes[node_value] for node_value in d_values[value]]

    return d_nodes[root.data]


# Tasks Scheduling
# Solution importing Graph data structure
def is_scheduling_possible_graph(tasks, prerequisites):
    g = Graph(tasks)
    for edge in prerequisites:
        g.add_edge(edge[0], edge[1])

    return bool(1 - detect_cycle(g))


# Plain python
# Kahn algorithm
def is_scheduling_possible(tasks, prerequisites):
    edges, counts, heads = {}, {}, set()
    for v in range(tasks):
        edges[v] = set()
        counts[v] = 0
        heads.add(v)

    for start, finish in prerequisites:
        edges[start].add(finish)
        counts[finish] += 1
        heads.discard(finish)

    while heads:
        head = heads.pop()
        while edges[head]:
            dest = edges[head].pop()
            counts[dest] -= 1
            if counts[dest] == 0:
                heads.add(dest)

    return sum(counts.values()) == 0


# Tasks Scheduling Order
def find_order(tasks, prerequisites):
    edges, counts, heads, sortedOrder = {}, {}, set(), []
    for v in range(tasks):
        edges[v] = set()
        counts[v] = 0
        heads.add(v)

    for start, finish in prerequisites:
        edges[start].add(finish)
        counts[finish] += 1
        heads.discard(finish)

    while heads:
        head = heads.pop()
        sortedOrder.append(head)
        while edges[head]:
            dest = edges[head].pop()
            counts[dest] -= 1
            if counts[dest] == 0:
                heads.add(dest)

    return sortedOrder if sum(counts.values()) == 0 else []


# All Tasks Scheduling Order
def print_orders(tasks, prerequisites):

    """
    Edges - a dictionary with keys as a list of vertices and values as a sets of destination vertices for key vertices
    Counts - a dictionary with keys as a list of vertices and counts of incoming edges
    Heads - a set of vertices with no incoming edges
    """

    # Initial construction of the graph:
    edges, counts, heads = {}, {}, set()
    for v in range(tasks):
        edges[v] = set()
        counts[v] = 0
        heads.add(v)

    # Filling the graph
    for start, finish in prerequisites:
        edges[start].add(finish)
        counts[finish] += 1
        heads.discard(finish)

    result = []

    def rec(seq: List[int], this_edges: Dict, this_counts: Dict, this_heads: Set):

        if len(seq) == tasks and sum(this_counts.values()) == 0:
            print(seq)
            result.append(seq)

        for head in this_heads:
            new_seq = seq + [head]
            new_edges = this_edges.copy()
            new_counts = this_counts.copy()
            new_heads = this_heads.copy()
            new_heads.discard(head)
            dests = this_edges[head].copy()

            # First stage of backtracking
            for dest in dests:
                new_edges[head].discard(dest)
                new_counts[dest] -= 1
                if new_counts[dest] == 0:
                    new_heads.add(dest)

            rec(new_seq, new_edges, new_counts, new_heads)

            # Second stage of backtracking
            for dest in dests:
                if new_counts[dest] == 0:
                    new_heads.discard(dest)
                new_counts[dest] += 1
                new_edges[head].add(dest)

    rec([], edges, counts, heads)
    return result


# Alien Dictionary
def alien_dictionary(words):

    # Initialize & fill the graph
    edges, counts, heads, non_heads = {}, {}, set(), set()
    for i in range(len(words) - 1):

        # Find different letters
        first_word, second_word = words[i], words[i+1]
        letter_i = 0
        while letter_i + 1 < min(len(first_word), len(second_word)) \
                and first_word[letter_i] == second_word[letter_i]:
            letter_i += 1
        if letter_i + 1 > min(len(first_word), len(second_word)):
            continue

        # Add to edges & counts
        if edges.get(first_word[letter_i]) is None:
            edges[first_word[letter_i]] = set()
            counts[first_word[letter_i]] = 0
            heads.add(first_word[letter_i])
        if edges.get(second_word[letter_i]) is None:
            edges[second_word[letter_i]] = set()
            counts[second_word[letter_i]] = 0
            heads.add(second_word[letter_i])

        if not edges[first_word[letter_i]].__contains__(second_word[letter_i]):
            edges[first_word[letter_i]].add(second_word[letter_i])
            counts[second_word[letter_i]] += 1
            non_heads.add(second_word[letter_i])

    heads = heads - non_heads
    alphabet = ""

    while heads:
        head = heads.pop()
        alphabet += head
        while edges[head]:
            dest = edges[head].pop()
            counts[dest] -= 1
            if counts[dest] == 0:
                heads.add(dest)

    return alphabet if sum(counts.values()) == 0 else ""
