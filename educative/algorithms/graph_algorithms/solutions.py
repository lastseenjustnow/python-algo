from typing import Optional, List

from collections import deque

from Graph_Class import Graph, AdjNode


# Challenge 3: Calculate the Number of Nodes in a Graph Level
def number_of_nodes(graph: Graph, level):
    """
    Calculates the number of nodes at given level

    Time: O(V + E)
    Space: O(V)

    :param graph: The graph
    :return: Total number of nodes at given level
    """

    stack_nodes = deque([0, None])
    current_level, level_count, saved_count = 1, 0, 0

    while current_level <= level:
        node_id: Optional[int] = stack_nodes.popleft()
        if node_id is None:
            current_level += 1
            saved_count = level_count
            level_count = 0
            stack_nodes.append(None)
            continue
        level_count += 1
        current_node: AdjNode = graph.graph[node_id]
        while current_node:
            stack_nodes.append(current_node.vertex)
            current_node = current_node.next

    return saved_count


# Challenge 4: Transpose a Graph
def transpose(graph: Graph):
    """
    Transpose the given graph

    Time: O(V+E)
    Space: O(V+E)

    :param graph: The graph
    :return: a new transposed graph of the given graph
    """

    new_graph = Graph(graph.V)  # Creating a new graph
    visited = [0] * graph.V
    heads = {i for i in range(graph.V)}
    stack = deque()

    while sum(visited) != len(visited):
        head_id = heads.pop()
        stack.append(head_id)
        while stack:
            head = stack.popleft()
            dest: Optional[AdjNode] = graph.graph[head]
            while dest:
                new_graph.add_edge(dest.vertex, head)
                if not visited[dest.vertex]:
                    stack.append(dest.vertex)
                dest = dest.next
            visited[head] = 1
            heads.discard(head_id)

    return new_graph


# Challenge 5: Find all Paths between Two Nodes
def find_all_paths(graph, source, destination):
    """
    Finds all paths between source and destination in given graph

    Time: O(V + E)
    Space: O(V!)

    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """

    paths = []

    def rec(this_node: int, current_path: List[int], visited: List[bool]):
        if this_node == destination:
            paths.append(current_path + [this_node])
            return

        node_dest: Optional[AdjNode] = graph.graph[this_node]
        while node_dest:
            new_visited = visited.copy()
            new_visited[this_node] = True
            rec(node_dest.vertex, current_path + [this_node], new_visited)
            node_dest = node_dest.next

    rec(source, [], [0] * graph.V)
    return paths


# Challenge 6: Check if a Graph is Strongly Connected
def is_strongly_connected(graph):
    """
    Finds if the graph is strongly connected or not

    Kosaraju-Sharir's algorithm:
    https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm

    Time: O(n)

    :param graph: The graph
    :return: returns True if the graph is strongly connected, otherwise False
    """
    L, visited, root_dict, components = deque(), [False] * graph.V, {}, set()

    def visit(u):
        if not visited[u]:
            visited[u] = True
            out_neighbor: AdjNode = graph.graph[u]
            while out_neighbor:
                visit(out_neighbor.vertex)
                out_neighbor = out_neighbor.next
            L.appendleft(u)

    for vertex in range(graph.V):
        visit(vertex)

    transposed_graph = transpose(graph)

    def assign(vertex, root):
        if root_dict.get(vertex) is None:
            components.add(root)
            root_dict[vertex] = root
            in_neighbor = transposed_graph.graph[vertex]
            while in_neighbor:
                assign(in_neighbor.vertex, root)
                in_neighbor = in_neighbor.next

    for elem in L:
        assign(elem, elem)

    return True if len(components) == 1 else False
