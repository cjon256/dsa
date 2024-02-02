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

# from conversions import ListNode, linked_list_to_list, list_to_linked_list
# from conversions import liststr_to_tree, treenode_to_liststr, TreeNode
from typing import List


#  start_marker
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def get_all_n_dist(i, j, n):
            for vert in range(max(0, i - n), min(len(mat), i + n + 1)):
                horz1 = n - abs(vert - i)
                if j + horz1 < len(mat[0]):
                    yield (vert, j + horz1)
                if j - horz1 >= 0:
                    yield (vert, j - horz1)

        def distance_to_nearest_zero(i, j):
            for n in range(1, (len(mat) + len(mat[0]) + 1)):
                for vert, horz in get_all_n_dist(i, j, n):
                    if mat[vert][horz] == 0:
                        return n
            return float("inf")

        retval = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    retval[i][j] = distance_to_nearest_zero(i, j)
        return retval
        #  end_marker


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


if __name__ == "__main__":
    unittest.main()
