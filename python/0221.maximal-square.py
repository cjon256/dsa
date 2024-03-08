#  Category: algorithms
#  Level: Medium
#  Percent: 46.3%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
#
#
# Example 1:
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
#
# Example 2:
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
#
# Example 3:
#
# Input: matrix = [["0"]]
# Output: 0
#
#
#
# Constraints:
#
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 300
#     matrix[i][j] is '0' or '1'.
#

import unittest
from typing import List


#  start_marker
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
