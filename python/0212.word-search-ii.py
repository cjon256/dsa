#  Category: algorithms
#  Level: Hard
#  Percent: 36.2%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#
#
# Example 1:
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
# Example 2:
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#
# Constraints:
#
#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 12
#     board[i][j] is a lowercase English letter.
#     1 <= words.length <= 3 * 104
#     1 <= words[i].length <= 10
#     words[i] consists of lowercase English letters.
#     All the strings of words are unique.
#

import unittest
from typing import List


#  start_marker
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
