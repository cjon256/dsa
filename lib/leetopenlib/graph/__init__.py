import unittest
from collections import deque
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Node:
    val: int
    neighbors: List["Node"] = field(default_factory=list)


def graph_to_adj_list(node: Optional[Node]) -> List[List[int]]:
    if not node:
        return []
    adj_map = {}
    visited = set()
    queue = deque([node])
    while queue:
        current = queue.popleft()
        visited.add(current.val)
        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)
        adj_map[current.val] = [neighbor.val for neighbor in current.neighbors]
    adj_list = [adj_map[i + 1] for i in range(len(adj_map))]
    return adj_list


def adj_list_to_graph(adj_list: List[List[int]]) -> Optional[Node]:
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        node = nodes[i]
        for neighbor in neighbors:
            node.neighbors.append(nodes[neighbor - 1])
    return nodes[0]


class TestNode(unittest.TestCase):
    def test_graph_to_adj_list(self):
        node = Node(1, [Node(2), Node(3)])
        self.assertEqual(graph_to_adj_list(node), [[2, 3], [], []])

    def test_adj_list_to_graph(self):
        adj_list = [[2, 3], [], []]
        node = Node(1, [Node(2), Node(3)])
        self.assertEqual(adj_list_to_graph(adj_list), node)


if __name__ == "__main__":
    unittest.main()
