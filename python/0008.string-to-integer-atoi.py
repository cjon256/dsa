#  Category: algorithms
#  Level: Medium
#  Percent: 17.029736%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Implement the myAtoi(string s) function, which converts a string to a 32-bit
#  signed integer (similar to C/C++'s atoi function).
#
#  The algorithm for myAtoi(string s) is as follows:
#
#
#  	Read in and ignore any leading whitespace.
#
#  	Check if the next character (if not already at the end of the string) is
#  	'-' or '+'. Read this character in if it is either. This determines if the
#  	final result is negative or positive respectively. Assume the result is
#  	positive if neither is present.
#
#  	Read in next the characters until the next non-digit character or the end
#  	of the input is reached. The rest of the string is ignored.
#
#  	Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If
#  	no digits were read, then the integer is 0. Change the sign as necessary
#  	(from step 2).
#
#  	If the integer is out of the 32-bit signed integer range [-2³¹, 2³¹ - 1],
#  	then clamp the integer so that it remains in the range. Specifically,
#  	integers less than -2³¹ should be clamped to -2³¹, and integers greater
#  	than 2³¹ - 1 should be clamped to 2³¹ - 1.
#
#  	Return the integer as the final result.
#
#
#  Note:
#
#
#  	Only the space character ' ' is considered a whitespace character.
#  	Do not ignore any characters other than the leading whitespace or the rest
#  	of the string after the digits.
#
#
#
#  Example 1:
#
#  Input: s = "42"
#  Output: 42
#  Explanation: The underlined characters are what is read in, the caret is the
#  current reader position.
#
#  Step 1: "42" (no characters read because there is no leading whitespace)
#           ^
#  Step 2: "42" (no characters read because there is neither a '-' nor '+')
#           ^
#  Step 3: "42" ("42" is read in)
#             ^
#  The parsed integer is 42.
#  Since 42 is in the range [-2³¹, 2³¹ - 1], the final result is 42.
#
#
#  Example 2:
#
#  Input: s = "   -42"
#  Output: -42
#  Explanation:
#  Step 1: "   -42" (leading whitespace is read and ignored)
#              ^
#  Step 2: "   -42" ('-' is read, so the result should be negative)
#               ^
#  Step 3: "   -42" ("42" is read in)
#                 ^
#  The parsed integer is -42.
#  Since -42 is in the range [-2³¹, 2³¹ - 1], the final result is -42.
#
#
#  Example 3:
#
#  Input: s = "4193 with words"
#  Output: 4193
#  Explanation:
#  Step 1: "4193 with words" (no characters read because there is no leading whitespace)
#           ^
#  Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
#           ^
#  Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
#               ^
#  The parsed integer is 4193.
#  Since 4193 is in the range [-2³¹, 2³¹ - 1], the final result is 4193.
#
#
#
#  Constraints:
#
#
#  	0 <= s.length <= 200
#  	s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
#


import unittest

# from conversions import ListNode, linked_list_to_list, list_to_linked_list
# from conversions import liststr_to_tree, treenode_to_liststr, TreeNode
from typing import List


#  start_marker
class Solution:
    def myAtoi(self, s: str) -> int:
        D = set("0123456789")
        # [-2³¹, 2³¹ - 1]
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        if not s:
            return 0
        # returned value
        retval = 0
        # current position
        start = 0

        # handle leading whitespace
        if s[0] == " ":
            while start < len(s) and s[start] == " ":
                start += 1
        if start == len(s):
            return 0

        # handle sign
        sign = 1
        if s[start] == "-":
            sign = -1
            start += 1
        elif s[start] == "+":
            start += 1

        # handle leading zeros
        while start < len(s) and s[start] == "0":
            start += 1

        # handle digits
        while start < len(s) and s[start] in D:
            val = ord(s[start]) - ord("0")
            retval = retval * 10 + val
            start += 1

        # handle digits and over/underflow
        retval = sign * retval
        if retval > MAX_INT:
            return MAX_INT
        if retval < MIN_INT:
            return MIN_INT
        return retval


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_0(self):
        s = ""
        expected = 0
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_1(self):
        s = "42"
        expected = 42
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_2(self):
        s = "   -42"
        expected = -42
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_3(self):
        s = "4193 with words"
        expected = 4193
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_4(self):
        s = "words and 987"
        expected = 0
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_5(self):
        MIN_INT = -(2**31)
        s = "-91283472332"
        expected = MIN_INT
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_6(self):
        MAX_INT = 2**31 - 1
        s = "91283472332"
        expected = MAX_INT
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_7(self):
        s = "3.14159"
        expected = 3
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_8(self):
        s = "   +0 123"
        expected = 0
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_9(self):
        s = "   - 321"
        expected = 0
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_10(self):
        s = "   -0 321"
        expected = 0
        self.assertEqual(Solution().myAtoi(s), expected)

    def test_case_11(self):
        s = "   -c321"
        expected = 0
        self.assertEqual(Solution().myAtoi(s), expected)


if __name__ == "__main__":
    unittest.main()
