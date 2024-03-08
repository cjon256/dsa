#  Category: algorithms
#  Level: Medium
#  Percent: 43.4%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Given a string s which represents an expression, evaluate this expression and return its value.
#
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
#
#
# Example 1:
#
# Input: s = "3+2*2"
# Output: 7
#
# Example 2:
#
# Input: s = " 3/2 "
# Output: 1
#
# Example 3:
#
# Input: s = " 3+5 / 2 "
# Output: 5
#
#
#
# Constraints:
#
#     1 <= s.length <= 3 * 105
#     s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
#     s represents a valid expression.
#     All the integers in the expression are non-negative integers in the range [0, 231 - 1].
#     The answer is guaranteed to fit in a 32-bit integer.
#

import unittest


#  start_marker
class Solution:
    def calculate(self, s: str) -> int:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
