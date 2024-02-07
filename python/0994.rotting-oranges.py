#  Category: algorithms
#  Level: Medium
#  Percent: 53.806473%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given an m x n grid where each cell can have one of three values:
#
#
#  	0 representing an empty cell,
#  	1 representing a fresh orange, or
#  	2 representing a rotten orange.
#
#
#  Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
#  Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
#
#  Example 1:
#
#  Input: grid = [[2,1,1],
#                 [1,1,0],
#                 [0,1,1]]
#  Output: 4
#
#
#  Example 2:
#
#  Input: grid = [[2,1,1],
#                 [0,1,1],
#                 [1,0,1]]
#  Output: -1
#  Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
#
#  Example 3:
#
#  Input: grid = [[0,2]]
#  Output: 0
#  Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
#
#  Constraints:
#
#
#  	m == grid.length
#  	n == grid[i].length
#  	1 <= m, n <= 10
#  	grid[i][j] is 0, 1, or 2.
#

import unittest
from pprint import pprint as pp
from typing import List

#  start_marker


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rot_orange(i, j) -> bool:
            # if out of bounds then return False
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return False
            # if not a fresh orange then return False
            if grid[i][j] == 0 or grid[i][j] == 2:
                return False
            # mark as rotting and return True
            grid[i][j] = 3
            return True

        def rot_adjacent(i, j) -> bool:
            # mark all adjacent fresh oranges as rotten and return True if any
            # of them was fresh
            up = rot_orange(i - 1, j)
            down = rot_orange(i + 1, j)
            left = rot_orange(i, j - 1)
            right = rot_orange(i, j + 1)
            return up or down or left or right

        minutes = 0
        # keep rotting until no more fresh oranges are left
        while True:
            rotting = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        if rot_adjacent(i, j):
                            rotting = True
            if not rotting:
                break
            # mark all rotting oranges as rotten
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 3:
                        grid[i][j] = 2
            minutes += 1
        # if there are still fresh oranges then return -1
        if any(1 in row for row in grid):
            return -1
        return minutes


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        expected = 4
        self.assertEqual(Solution().orangesRotting(grid), expected)

    def test_case_2(self):
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        expected = -1
        self.assertEqual(Solution().orangesRotting(grid), expected)

    def test_case_3(self):
        grid = [[0, 2]]
        expected = 0
        self.assertEqual(Solution().orangesRotting(grid), expected)

    def test_case_4(self):
        grid = [[2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
        expected = 0
        self.assertEqual(Solution().orangesRotting(grid), expected)

    def test_case_5(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        expected = -1
        self.assertEqual(Solution().orangesRotting(grid), expected)

    def test_case_6(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 2, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        expected = 126
        self.assertEqual(Solution().orangesRotting(grid), expected)

    def test_case_7(self):
        grid = [[1], [2], [1], [1]]
        expected = 2
        self.assertEqual(Solution().orangesRotting(grid), expected)


if __name__ == "__main__":
    unittest.main()
