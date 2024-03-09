#  Category: algorithms
#  Level: Medium
#  Percent: 55.1%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

# Hint
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
#
#
#
# Example 1:
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Example 2:
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#
# Constraints:
#
#     m == matrix.length
#     n == matrix[0].length
#     1 <= m, n <= 200
#     -231 <= matrix[i][j] <= 231 - 1
#
#
#
# Follow up:
#
#     A straightforward solution using O(mn) space is probably a bad idea.
#     A simple improvement uses O(m + n) space, but still not the best solution.
#     Could you devise a constant space solution?
#

import unittest
from typing import List


#  start_marker
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        FAKE_ZERO = 1000

        def set_row_zero(r):
            for col in range(len(matrix[0])):
                if matrix[r][col] != 0:
                    matrix[r][col] = FAKE_ZERO

        def set_col_zero(c):
            for row in range(len(matrix)):
                if matrix[row][c] != 0:
                    matrix[row][c] = FAKE_ZERO

        def fix_fake_zeros(r, c):
            if matrix[r][c] == FAKE_ZERO:
                matrix[r][c] = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    set_row_zero(row)
                    set_col_zero(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                fix_fake_zeros(row, col)

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected_result = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, expected_result)

    def test_case_2(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected_result = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, expected_result)

    def test_case_3(self):
        matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
        expected_result = [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, expected_result)


if __name__ == "__main__":
    unittest.main()
