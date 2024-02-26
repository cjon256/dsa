#  Category: algorithms
#  Level: Medium
#  Percent: 73.75836%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
#  You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
#
#  Example 1:
#
#  Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#  Output: [[7,4,1],[8,5,2],[9,6,3]]
#
#
#  Example 2:
#
#  Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#  Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
#
#  Constraints:
#
#
#  	n == matrix.length == matrix[i].length
#  	1 <= n <= 20
#  	-1000 <= matrix[i][j] <= 1000
#


import unittest

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List


#  start_marker
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in matrix:
            r.reverse()
        # print(matrix)
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        last_this_row = len(matrix[0])
        for row in range(num_rows):
            for col in range(last_this_row):
                pair_row = num_cols - col - 1
                pair_col = num_rows - row - 1
                # print(f"swap mat[{row}][{col}] <-> matrix[{pair_row}][{pair_col}]")
                matrix[row][col], matrix[pair_row][pair_col] = (
                    matrix[pair_row][pair_col],
                    matrix[row][col],
                )
            last_this_row -= 1
        #  end_marker


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_case_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        result = self.s.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_case_2(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        result = self.s.rotate(matrix)
        self.assertEqual(matrix, expected)


if __name__ == "__main__":
    unittest.main()
