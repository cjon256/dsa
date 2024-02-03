#  Category: algorithms
#  Level: Medium
#  Percent: 48.084156%

# pylint: enable=useless-suppression
# pylint: disable=invalid-name, consider-using-enumerate, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
#  The distance between two adjacent cells is 1.
#
#
#  Example 1:
#
#  Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
#  Output: [[0,0,0],[0,1,0],[0,0,0]]
#
#
#  Example 2:
#
#  Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
#  Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#
#
#  Constraints:
#
#
#  	m == mat.length
#  	n == mat[i].length
#  	1 <= m, n <= 10⁴
#  	1 <= m * n <= 10⁴
#  	mat[i][j] is either 0 or 1.
#  	There is at least one 0 in mat.
#


import unittest
from typing import List

from _0542_01_matrix_dat import TEST_6_MAT, TEST_6_RES, TEST_9_MAT, TEST_9_RES


#  start_marker
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        MAX_INT = 10**14
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    mat[i][j] = MAX_INT
            for j in range(1, len(mat[0])):
                if mat[i][j] != 0:
                    mat[i][j] = min(mat[i][j], mat[i][j - 1] + 1)
            for j in range(len(mat[0]) - 2, -1, -1):
                if mat[i][j] != 0:
                    mat[i][j] = min(mat[i][j], mat[i][j + 1] + 1)

        for j in range(len(mat[0])):
            for i in range(1, len(mat)):
                mat[i][j] = min(mat[i][j], mat[i - 1][j] + 1)
            for i in range(len(mat) - 2, -1, -1):
                mat[i][j] = min(mat[i][j], mat[i + 1][j] + 1)
        return mat
        # end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        result = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(Solution().updateMatrix(mat), result)

    def test_case_2(self):
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        result = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        self.assertEqual(Solution().updateMatrix(mat), result)

    def test_case_3(self):
        mat = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
        result = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
        self.assertEqual(Solution().updateMatrix(mat), result)

    def test_case_4(self):
        mat = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
        result = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
        self.assertEqual(Solution().updateMatrix(mat), result)

    def test_case_5(self):
        mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        result = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
        self.assertEqual(Solution().updateMatrix(mat), result)

    def test_case_6(self):
        mat = TEST_6_MAT
        result = TEST_6_RES
        self.assertEqual(Solution().updateMatrix(mat), result)

    def test_case_7(self):
        mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(Solution().updateMatrix(mat), result)

    def test_case_8(self):
        mat = [[0], [0], [0], [0], [0]]
        result = [[0], [0], [0], [0], [0]]
        self.assertEqual(Solution().updateMatrix(mat), result)

    def test_case_9(self):
        mat = TEST_9_MAT
        result = TEST_9_RES
        self.assertEqual(Solution().updateMatrix(mat), result)


if __name__ == "__main__":
    unittest.main()
