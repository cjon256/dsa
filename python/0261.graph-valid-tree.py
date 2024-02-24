#  Category: algorithms
#  Level: Medium
#  Percent: 47.807648%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
#
#  Return true if the edges of the given graph make up a valid tree, and false otherwise.
#
#
#  Example 1:
#
#  Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
#  Output: true
#
#
#  Example 2:
#
#  Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
#  Output: false
#
#
#
#  Constraints:
#
#
#  	1 <= n <= 2000
#  	0 <= edges.length <= 5000
#  	edges[i].length == 2
#  	0 <= ai, bi < n
#  	ai != bi
#  	There are no self-loops or repeated edges.
#


import unittest
from collections import namedtuple

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import Dict, List


#  start_marker
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        Group = namedtuple("Group", "num count")
        if len(edges) != n - 1:
            return False
        connected: Dict[int, Group] = {}
        for k in range(n):
            connected[k] = Group(k, 1)

        def lookup_group(num):
            k = num
            while connected[k].num != k:
                k = connected[k].num
            return k

        def merge_groups(g1, g2):
            count1 = connected[g1].count
            count2 = connected[g2].count
            if count1 < count2:
                connected[g2] = Group(g2, count1 + count2)
                connected[g1] = Group(g2, 1)
            else:
                connected[g1] = Group(g1, count1 + count2)
                connected[g2] = Group(g1, 1)

        for edge in edges:
            n1, n2 = edge
            g1 = lookup_group(n1)
            g2 = lookup_group(n2)
            if g1 == g2:
                return False
            merge_groups(g1, g2)
            # print(connected)
        return True


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        result = Solution().validTree(n, edges)
        self.assertTrue(result)

    def test_case_2(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        result = Solution().validTree(n, edges)
        self.assertFalse(result)

    def test_case_3(self):
        n = 4
        edges = [[2, 3], [1, 2], [1, 3]]
        result = Solution().validTree(n, edges)
        self.assertFalse(result)

    def test_case_4(self):
        n = 4
        edges = [[0, 1], [2, 3], [1, 2]]
        result = Solution().validTree(n, edges)
        self.assertTrue(result)

    def test_case_5(self):
        n = 4
        edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
        result = Solution().validTree(n, edges)
        self.assertFalse(result)

    def test_case_6(self):
        n = 1
        edges = []
        result = Solution().validTree(n, edges)
        self.assertTrue(result)

    def test_case_7(self):
        n = 2
        edges = [[0, 1]]
        result = Solution().validTree(n, edges)
        self.assertTrue(result)

    def test_case_8(self):
        n = 2
        edges = []
        result = Solution().validTree(n, edges)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
