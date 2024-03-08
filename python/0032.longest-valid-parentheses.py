#  Category: algorithms
#  Level: Hard
#  Percent: 33.9%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
# substring
# .
#
#
#
# Example 1:
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
# Example 2:
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
# Example 3:
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#     0 <= s.length <= 3 * 104
#     s[i] is '(', or ')'.
#

import unittest


#  start_marker
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
