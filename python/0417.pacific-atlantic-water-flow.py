#  Category: algorithms
#  Level: Medium
#  Percent: 55.028717%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  There is an m x n rectangular island that borders both the Pacific Ocean and
#  Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
#  and the Atlantic Ocean touches the island's right and bottom edges.
#
#  The island is partitioned into a grid of square cells. You are given an m x
#  n integer matrix heights where heights[r][c] represents the height above sea
#  level of the cell at coordinate (r, c).
#
#  The island receives a lot of rain, and the rain water can flow to
#  neighboring cells directly north, south, east, and west if the neighboring
#  cell's height is less than or equal to the current cell's height. Water can
#  flow from any cell adjacent to an ocean into the ocean.
#
#  Return a 2D list of grid coordinates result where result[i] = [ri, ci]
#  denotes that rain water can flow from cell (ri, ci) to both the Pacific and
#  Atlantic oceans.
#
#
#  Example 1:
#
#  Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
#  Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#  Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
#  [0,4]: [0,4] -> Pacific Ocean
#         [0,4] -> Atlantic Ocean
#  [1,3]: [1,3] -> [0,3] -> Pacific Ocean
#         [1,3] -> [1,4] -> Atlantic Ocean
#  [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
#         [1,4] -> Atlantic Ocean
#  [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
#         [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
#  [3,0]: [3,0] -> Pacific Ocean
#         [3,0] -> [4,0] -> Atlantic Ocean
#  [3,1]: [3,1] -> [3,0] -> Pacific Ocean
#         [3,1] -> [4,1] -> Atlantic Ocean
#  [4,0]: [4,0] -> Pacific Ocean
#         [4,0] -> Atlantic Ocean
#  Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
#
#
#  Example 2:
#
#  Input: heights = [[1]]
#  Output: [[0,0]]
#  Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
#
#
#
#  Constraints:
#
#
#  	m == heights.length
#  	n == heights[r].length
#  	1 <= m, n <= 200
#  	0 <= heights[r][c] <= 10⁵
#


import unittest
from pprint import pprint as pp
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
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # print_arr("heights", heights)
        num_rows, num_cols = len(heights), len(heights[0])
        pacific_drain = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        pacific_visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        atlantic_drain = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        atlantic_visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        for i in range(num_cols):
            pacific_drain[0][i] = 1
            atlantic_drain[-1][i] = 1
        for i in range(num_rows):
            pacific_drain[i][0] = 1
            atlantic_drain[i][-1] = 1

        def diffuse_from(drain_matrix, row, col, visited) -> None:
            if drain_matrix[row][col] == 0 or visited[row][col]:
                print(f"failed to diffuse_from r{row}c{col}")
                return
            curr_ht = heights[row][col]
            visited[row][col] = True
            # up
            if (
                row > 0
                and not visited[row - 1][col]
                and heights[row - 1][col] >= curr_ht
                and not drain_matrix[row - 1][col]
            ):
                drain_matrix[row - 1][col] = 1
                diffuse_from(drain_matrix, row - 1, col, visited)
            # down
            if (
                row < num_rows - 1
                and not visited[row + 1][col]
                and heights[row + 1][col] >= curr_ht
                and not drain_matrix[row + 1][col]
            ):
                drain_matrix[row + 1][col] = 1
                diffuse_from(drain_matrix, row + 1, col, visited)
            # left
            if (
                col > 0
                and not visited[row][col - 1]
                and heights[row][col - 1] >= curr_ht
                and not drain_matrix[row][col - 1]
            ):
                drain_matrix[row][col - 1] = 1
                diffuse_from(drain_matrix, row, col - 1, visited)
            # right
            if (
                col < num_cols - 1
                and not visited[row][col + 1]
                and heights[row][col + 1] >= curr_ht
                and not drain_matrix[row][col + 1]
            ):
                drain_matrix[row][col + 1] = 1
                diffuse_from(drain_matrix, row, col + 1, visited)

        for i in range(1, num_cols):
            diffuse_from(pacific_drain, row=0, col=i, visited=pacific_visited)
        for j in range(1, num_rows):
            diffuse_from(pacific_drain, row=j, col=0, visited=pacific_visited)

        for i in range(num_cols - 2, -1, -1):
            diffuse_from(
                atlantic_drain, row=num_rows - 1, col=i, visited=atlantic_visited
            )
        for j in range(num_rows - 2, -1, -1):
            diffuse_from(
                atlantic_drain, row=j, col=num_cols - 1, visited=atlantic_visited
            )

        # print_arr("pacific_drain", pacific_drain)
        # print_arr("pacific_visited", pacific_visited)
        # print_arr("atlantic_drain", atlantic_drain)
        # print_arr("atlantic_visited", atlantic_visited)

        res = []
        for i in range(num_rows):
            for j in range(num_cols):
                if pacific_drain[i][j] and atlantic_drain[i][j]:
                    res.append([i, j])
        return res
        #  end_marker

    def pacificAtlantic_original(self, heights: List[List[int]]) -> List[List[int]]:
        # print_arr("heights", heights)
        num_rows, num_cols = len(heights), len(heights[0])
        pacific_drain = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        atlantic_drain = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        for i in range(num_cols):
            pacific_drain[0][i] = 1
            atlantic_drain[-1][i] = 1
        for i in range(num_rows):
            pacific_drain[i][0] = 1
            atlantic_drain[i][-1] = 1
        # print_arr("pacific_drain", pacific_drain)
        # print_arr("atlantic_drain", atlantic_drain)
        changed = True
        while changed:
            changed = False
            for i in range(1, num_rows):
                for j in range(1, num_cols):
                    if pacific_drain[i][j]:
                        continue
                    if (
                        (
                            i > 0
                            and heights[i][j] >= heights[i - 1][j]
                            and pacific_drain[i - 1][j]
                        )
                        or (
                            i < num_rows - 1
                            and heights[i][j] >= heights[i + 1][j]
                            and pacific_drain[i + 1][j]
                        )
                        or (
                            j > 0
                            and (heights[i][j] >= heights[i][j - 1])
                            and pacific_drain[i][j - 1]
                        )
                        or (
                            j < num_cols - 1
                            and heights[i][j] >= heights[i][j + 1]
                            and pacific_drain[i][j + 1] == 1
                        )
                    ):
                        pacific_drain[i][j] = 1
                        changed = True

        changed = True
        while changed:
            changed = False
            for i in range(num_rows - 1, -1, -1):
                for j in range(num_cols - 1, -1, -1):
                    if atlantic_drain[i][j]:
                        continue
                    if (
                        (
                            i > 0
                            and heights[i][j] >= heights[i - 1][j]
                            and atlantic_drain[i - 1][j]
                        )
                        or (
                            i < num_rows - 1
                            and heights[i][j] >= heights[i + 1][j]
                            and atlantic_drain[i + 1][j]
                        )
                        or (
                            j > 0
                            and heights[i][j] >= heights[i][j - 1]
                            and atlantic_drain[i][j - 1]
                        )
                        or (
                            j < num_cols - 1
                            and heights[i][j] >= heights[i][j + 1]
                            and atlantic_drain[i][j + 1]
                        )
                    ):
                        atlantic_drain[i][j] = 1
                        changed = True

        res = []
        for i in range(num_rows):
            for j in range(num_cols):
                if pacific_drain[i][j] and atlantic_drain[i][j]:
                    res.append([i, j])
        return res


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        heights = [[2, 2], [3, 1]]
        expected = [[0, 0], [0, 1], [1, 0]]
        result = Solution().pacificAtlantic(heights)
        self.assertEqual(result, expected)

    def test_case_2(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        result = Solution().pacificAtlantic(heights)
        self.assertEqual(result, expected)

    def test_case_3(self):
        heights = [[1]]
        expected = [[0, 0]]
        result = Solution().pacificAtlantic(heights)
        self.assertEqual(result, expected)

    def test_case_4(self):
        heights = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        expected = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        result = Solution().pacificAtlantic(heights)
        self.assertEqual(result, expected)

    def test_case_5(self):
        heights = [[1, 2], [2, 3]]
        expected = [[0, 1], [1, 0], [1, 1]]
        result = Solution().pacificAtlantic(heights)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
    # # fmt: off
    # heights = [[1, 2, 3],
    #            [8, 9, 4],
    #            [7, 6, 5]]
    # # fmt: on
    # expected = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    # result = Solution().pacificAtlantic(heights)
    # print(expected)
    # print(result)
