#  Category: algorithms
#  Level: Medium
#  Percent: 58.39311%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
#  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#  Example 1:
#
#  Input: grid = [
#    ["1","1","1","1","0"],
#    ["1","1","0","1","0"],
#    ["1","1","0","0","0"],
#    ["0","0","0","0","0"]
#  ]
#  Output: 1
#
#
#  Example 2:
#
#  Input: grid = [
#    ["1","1","0","0","0"],
#    ["1","1","0","0","0"],
#    ["0","0","1","0","0"],
#    ["0","0","0","1","1"]
#  ]
#  Output: 3
#
#
#
#  Constraints:
#
#
#  	m == grid.length
#  	n == grid[i].length
#  	1 <= m, n <= 300
#  	grid[i][j] is '0' or '1'.
#

import unittest
from typing import List


#  start_marker
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if (  # if out of bounds
                i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])
            ):
                return
            # or if it's water
            if grid[i][j] == "0":
                return
            # mark as water
            grid[i][j] = "0"
            # propagate in all 4 directions
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        expected = 1
        self.assertEqual(Solution().numIslands(input), expected)

    def test_case_2(self):
        input = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        expected = 3
        self.assertEqual(Solution().numIslands(input), expected)

    def test_case_3(self):
        input = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
        expected = 1
        self.assertEqual(Solution().numIslands(input), expected)


if __name__ == "__main__":
    unittest.main()
