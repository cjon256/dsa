#  Category: algorithms
#  Level: Medium
#  Percent: 48.62678%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
#  Example 1:
#
#  Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#  Output: [1,2,3,6,9,8,7,4,5]
#
#
#  Example 2:
#
#  Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#  Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#  Constraints:
#
#
#  	m == matrix.length
#  	n == matrix[i].length
#  	1 <= m, n <= 10
#  	-100 <= matrix[i][j] <= 100
#


import unittest
from typing import List, Tuple


#  start_marker
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        width = len(matrix[0])
        length = len(matrix)
        res = []

        def ring(ul: Tuple[int, int], lr: Tuple[int, int]) -> None:
            if ul == lr:
                res.append(matrix[ul[1]][ul[0]])
                return
            ulx, uly = ul
            lrx, lry = lr
            for i in range(ulx, lrx):
                res.append(matrix[uly][i])
            for i in range(uly, lry):
                res.append(matrix[i][lrx])
            for i in range(lrx, ulx, -1):
                res.append(matrix[lry][i])
            for i in range(lry, uly, -1):
                res.append(matrix[i][ulx])

        ulx = 0
        uly = 0
        lrx = width - 1
        lry = length - 1
        while ulx < lrx and uly < lry:
            ring((ulx, uly), (lrx, lry))
            ulx += 1
            uly += 1
            lrx -= 1
            lry -= 1

        if ulx == lrx and uly == lry:
            res.append(matrix[uly][ulx])
        elif ulx == lrx:
            for i in range(uly, lry + 1):
                res.append(matrix[i][ulx])
        elif uly == lry:
            for i in range(ulx, lrx + 1):
                res.append(matrix[uly][i])

        return res
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_2(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_3(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
        expected = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_4(self):
        matrix = [[]]
        expected = []
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_5(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_6(self):
        matrix = []
        expected = []
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_7(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        expected = [
            # fmt: off
            1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13
        ]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_8(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ]
        expected = [
            # fmt: off
            1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
        ]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_9(self):
        matrix = [[1, 2], [3, 4]]
        expected = [1, 2, 4, 3]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_10(self):
        matrix = [[1, 2, 3, 4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_11(self):
        matrix = [[1], [2], [3], [4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_12(self):
        matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        expected = [1, 2, 4, 6, 8, 10, 9, 7, 5, 3]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_13(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        expected = [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_case_14(self):
        matrix = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        ]
        expected = [
            # fmt: off
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        ]
        self.assertEqual(Solution().spiralOrder(matrix), expected)


if __name__ == "__main__":
    unittest.main()
