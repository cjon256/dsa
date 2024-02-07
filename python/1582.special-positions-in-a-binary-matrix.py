#  Category: algorithms
#  Level: Easy
#  Percent: 68.814674%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an m x n binary matrix mat, return the number of special positions in mat.
#
#  A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
#
#
#  Example 1:
#
#  Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
#  Output: 1
#  Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
#
#
#  Example 2:
#
#  Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
#  Output: 3
#  Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
#
#
#
#  Constraints:
#
#
#  	m == mat.length
#  	n == mat[i].length
#  	1 <= m, n <= 100
#  	mat[i][j] is either 0 or 1.
#

import unittest
from collections import Counter
from typing import List


#  start_marker
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def cols_with_ones(row: List[int]) -> List[int]:
            cols = []
            for col in range(len(row)):
                if row[col] == 1:
                    cols.append(col)
            return cols

        count = 0
        singular_rows = {}
        cols_seen = Counter()
        for row in range(len(mat)):
            cols = cols_with_ones(mat[row])
            if cols:
                if len(cols) == 1:
                    # singular_row
                    singular_rows[row] = cols[0]
                for col in cols:
                    cols_seen[col] += 1
        for row in singular_rows:
            if cols_seen[singular_rows[row]] == 1:
                count += 1
        return count
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_1(self):
        mat1 = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
        self.assertEqual(Solution().numSpecial(mat1), 1)

    def test_2(self):
        mat2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(Solution().numSpecial(mat2), 3)

    def test_3(self):
        mat3 = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        self.assertEqual(Solution().numSpecial(mat3), 2)

    def test_4(self):
        mat4 = [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
        ]
        self.assertEqual(Solution().numSpecial(mat4), 3)

    def test_5(self):
        mat5 = [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
        ]
        self.assertEqual(Solution().numSpecial(mat5), 3)

    def test_6(self):
        mat6 = [
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
        ]
        self.assertEqual(Solution().numSpecial(mat6), 1)


if __name__ == "__main__":
    unittest.main()
