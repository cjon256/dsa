#  Category: algorithms
#  Level: Medium
#  Percent: 38.800243%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  A tree is an undirected graph in which any two vertices are connected
#  by exactly one path. In other words, any connected graph without simple
#  cycles is a tree.
#
#  Given a tree of n nodes labelled from 0 to n - 1, and an array of n -
#  1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge
#  between the two nodes ai and bi in the tree, you can choose any node of the
#  tree as the root. When you select a node x as the root, the result tree has
#  height h. Among all possible rooted trees, those with minimum height (i.e.
#  min(h))  are called minimum height trees (MHTs).
#
#  Return a list of all MHTs' root labels. You can return the answer in any order.
#
#  The height of a rooted tree is the number of edges on the longest downward
#  path between the root and a leaf.
#
#
#  Example 1:
#
#  Input: n = 4, edges = [[1,0],[1,2],[1,3]]
#  Output: [1]
#  Explanation: As shown, the height of the tree is 1 when the root is the node
#  with label 1 which is the only MHT.
#
#
#  Example 2:
#
#  Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
#  Output: [3,4]
#
#
#
#  Constraints:
#
#
#  	1 <= n <= 2 * 10⁴
#  	edges.length == n - 1
#  	0 <= ai, bi < n
#  	ai != bi
#  	All the pairs (ai, bi) are distinct.
#  	The given input is guaranteed to be a tree and there will be no repeated edges.
#


import unittest
from collections import defaultdict
from pprint import pprint as pp
from typing import List, Set


#  start_marker
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        node_to_edge: defaultdict[int, Set] = defaultdict(set)
        nodes: Set[int] = set(range(n))
        for e in edges:
            et = tuple(e)
            node_to_edge[e[0]].add(et)
            node_to_edge[e[1]].add(et)
        while len(nodes) > 2:
            edges_to_remove = []
            res: List[int] = []
            for nd, ed in node_to_edge.items():
                if len(ed) == 1:
                    edge_to_remove = ed.pop()
                    res.append(nd)
                    edges_to_remove.append([nd, edge_to_remove])
            for n in res:
                nodes.remove(n)
            for nd, edg in edges_to_remove:
                if edg[0] == nd:
                    other_node = edg[1]
                    node_to_edge[other_node].remove(edg)
                else:
                    other_node = edg[0]
                    node_to_edge[other_node].remove(edg)
        return list(nodes)
        #  end_marker

    def findMinHeightTrees_withprints(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        if n == 1:
            return [0]
        node_to_edge: defaultdict[int, Set] = defaultdict(set)
        nodes: Set[int] = set(range(n))
        for e in edges:
            et = tuple(e)
            node_to_edge[e[0]].add(et)
            node_to_edge[e[1]].add(et)
        print(f"nodes: {nodes}")
        while len(nodes) > 2:
            edges_to_remove = []
            res: List[int] = []
            for nd, ed in node_to_edge.items():
                if len(ed) == 1:
                    print(f"len(ed) == 1 -- nd: {nd}, ed: {ed}")
                    print(f"res: {res}")
                    print("node_to_edge: ", end="")
                    pp(node_to_edge)
                    edge_to_remove = ed.pop()
                    print(f"edge_to_remove: {edge_to_remove}")
                    res.append(nd)
                    edges_to_remove.append([nd, edge_to_remove])
            for n in res:
                print(f"removing node: {n}")
                nodes.remove(n)
            for nd, edg in edges_to_remove:
                if edg[0] == nd:
                    other_node = edg[1]
                    node_to_edge[other_node].remove(edg)
                else:
                    other_node = edg[0]
                    node_to_edge[other_node].remove(edg)

        pp(nodes)
        return list(nodes)


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        n = 4
        edges = [[1, 0], [1, 2], [1, 3]]
        expected = [1]
        result = Solution().findMinHeightTrees(n, edges)
        self.assertEqual(result, expected)

    def test_case_2(self):
        n = 6
        edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
        expected = [3, 4]
        result = Solution().findMinHeightTrees(n, edges)
        self.assertEqual(result, expected)

    def test_case_3(self):
        n = 1
        edges = []
        expected = [0]
        result = Solution().findMinHeightTrees(n, edges)
        self.assertEqual(result, expected)

    def test_case_4(self):
        n = 2
        edges = [[0, 1]]
        expected = [0, 1]
        result = Solution().findMinHeightTrees(n, edges)
        self.assertEqual(result, expected)

    def test_case_5(self):
        n = 7
        edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [6, 5]]
        expected = [4]
        result = Solution().findMinHeightTrees(n, edges)
        self.assertEqual(result, expected)

    def test_case_6(self):
        n = 6
        edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
        expected = [3]
        result = Solution().findMinHeightTrees(n, edges)
        self.assertEqual(result, expected)

    def test_case_7(self):
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [3, 4]]
        expected = [0, 3]
        result = Solution().findMinHeightTrees(n, edges)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
