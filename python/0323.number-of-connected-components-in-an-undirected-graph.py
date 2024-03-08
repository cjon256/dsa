#  Category: algorithms
#  Level: Medium
#  Percent: 62.7%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
#
# Return the number of connected components in the graph.
#
#
#
# Example 1:
#
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
#
# Example 2:
#
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
#
#
#
# Constraints:
#
#     1 <= n <= 2000
#     1 <= edges.length <= 5000
#     edges[i].length == 2
#     0 <= ai <= bi < n
#     ai != bi
#     There are no repeated edges.
#

import unittest
from typing import List


#  start_marker
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
