from typing import Optional

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
