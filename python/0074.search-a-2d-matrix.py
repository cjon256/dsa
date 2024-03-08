#  Category: algorithms
#  Level: Medium
#  Percent: 49.8%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# You are given an m x n integer matrix matrix with the following two properties:
#
#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.
#
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.
#
#
#
# Example 1:
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
# Example 2:
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 100
#     -104 <= matrix[i][j], target <= 104
#

import unittest
from typing import List


#  start_marker
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
