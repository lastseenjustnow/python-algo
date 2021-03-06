from typing import Optional, List

from collections import deque
import copy

from Graph_Class import Graph, UndirectedGraph, AdjNode


# Challenge 1: Breadth-First Graph Traversal
def bfs(graph: Graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """

    stack = deque()
    stack.append(source)
    result = ''

    while stack:
        this_node_id = stack.popleft()
        result += str(this_node_id)
        this_node: AdjNode = graph.graph[this_node_id]
        while this_node:
            stack.append(this_node.vertex)
            this_node = this_node.next

    return result


# Challenge 2: Depth-First Graph Traversal
def dfs(graph: Graph, source):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    # Mark all the vertices as not visited
    visited = [False] * (len(graph.graph))

    # Create a stack for DFS
    stack = []

    # Result string
    result = ""

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack.pop()

        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next

    return result


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


# Challenge 7: Find All Connected Components in a Graph
def connected_components(graph: UndirectedGraph):
    """
    Function to find the connected components

    Time: O(V + E)

    :param graph: The graph
    :return: returns a list of connected components
    """

    # Helper Function of DFS. Might be useful
    def dfs(g, source, visited):
        """
        Function to print a DFS of graph
        :param graph: The graph
        :param source: starting vertex
        :return: returns the traversal in a list
        """

        graph = copy.deepcopy(g)

        # Create a stack for DFS
        stack = []

        # Result list
        result = []

        # Push the source
        stack.append(source)

        while stack:

            # Pop a vertex from stack
            source = stack[-1]
            stack.pop()

            if not visited[source]:
                result += str(source)
                visited[source] = True

            # Get all adjacent vertices of the popped vertex source.
            # If a adjacent has not been visited, then push it
            while graph.graph[source] is not None:
                data = graph.graph[source].vertex
                if not visited[data]:
                    stack.append(data)
                graph.graph[source] = graph.graph[source].next

        return result

    visited, results = [False] * graph.V, []
    for elem in range(graph.V):
        res = dfs(graph, elem, visited)
        if res:
            results.append(res)

    return results
