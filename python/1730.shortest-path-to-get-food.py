#  Category: algorithms
#  Level: Medium
#  Percent: 54.4894%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.
#
#  You are given an m x n character matrix, grid, of these different types of cells:
#
#
#  	'*' is your location. There is exactly one '*' cell.
#  	'#' is a food cell. There may be multiple food cells.
#  	'O' is free space, and you can travel through these cells.
#  	'X' is an obstacle, and you cannot travel through these cells.
#
#
#  You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.
#
#  Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.
#
#
#  Example 1:
#
#  Input: grid = [["X","X","X","X","X","X"],
#                 ["X","*","O","O","O","X"],
#                 ["X","O","O","#","O","X"],
#                 ["X","X","X","X","X","X"]]
#  Output: 3
#  Explanation: It takes 3 steps to reach the food.
#
#
#  Example 2:
#
#  Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
#  Output: -1
#  Explanation: It is not possible to reach the food.
#
#
#  Example 3:
#
#  Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
#  Output: 6
#  Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
#
#
#  Constraints:
#
#
#  	m == grid.length
#  	n == grid[i].length
#  	1 <= m, n <= 200
#  	grid[row][col] is '*', 'X', 'O', or '#'.
#  	The grid contains exactly one '*'.
#


import unittest

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List


def print_arr(name, arr):
    print(f"{name} = [")
    for i in range(len(arr)):
        print(" [ ", end="")
        for j in range(len(arr[0])):
            ender = " " if j == len(arr[0]) - 1 else ", "
            print(arr[i][j], end=ender)
        print("]")
    print("]")


#  start_marker

from collections import deque


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        start: List[int] = []
        food: List[List[int]] = []
        not_visited = [[True] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = grid[i][j]
                match val:
                    case "#":
                        food.append([i, j])
                    case "*":
                        start = [i, j]
                        not_visited[i][j] = False
                    case "X":
                        not_visited[i][j] = False

        def is_not_visited(x, y) -> bool:
            res = not_visited[x][y]
            not_visited[x][y] = False
            return res

        def is_in_limits(x, y) -> bool:
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return False
            return True

        DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # vanilla bfs
        dist = -1
        queue: deque[List[int]] = deque()
        queue.append([*start, 0])
        while queue:
            x, y, dist = queue.popleft()
            if [x, y] in food:
                break
            for d in DIRS:
                dx, dy = d
                new_x, new_y = (x + dx, y + dy)
                if is_in_limits(new_x, new_y) and is_not_visited(new_x, new_y):
                    queue.append([new_x, new_y, dist + 1])
            dist = -1

        return dist
        #  end_marker


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        grid = [
            ["X", "X", "X", "X", "X", "X"],
            ["X", "*", "O", "O", "O", "X"],
            ["X", "O", "O", "#", "O", "X"],
            ["X", "X", "X", "X", "X", "X"],
        ]
        expected = 3
        result = Solution().getFood(grid)
        self.assertEqual(result, expected)

    def test_case_2(self):
        grid = [
            ["X", "X", "X", "X", "X"],
            ["X", "*", "X", "O", "X"],
            ["X", "O", "X", "#", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        expected = -1
        result = Solution().getFood(grid)
        self.assertEqual(result, expected)

    def test_case_3(self):
        grid = [
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "*", "O", "X", "O", "#", "O", "X"],
            ["X", "O", "O", "X", "O", "O", "X", "X"],
            ["X", "O", "O", "O", "O", "#", "O", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        expected = 6
        result = Solution().getFood(grid)
        self.assertEqual(result, expected)

    def test_case_4(self):
        grid = [["O", "*"], ["#", "O"]]
        expected = 2
        result = Solution().getFood(grid)
        self.assertEqual(result, expected)

    def test_case_5(self):
        grid = [
            ["O", "O", "O", "#", "X"],
            ["O", "X", "O", "O", "*"],
            ["O", "X", "#", "X", "O"],
            ["#", "O", "O", "X", "O"],
            ["O", "X", "O", "O", "O"],
        ]
        expected = 2
        result = Solution().getFood(grid)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
