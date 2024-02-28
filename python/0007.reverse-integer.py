#  Category: algorithms
#  Level: Medium
#  Percent: 28.37851%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], then return 0.
#
#  Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#  Example 1:
#
#  Input: x = 123
#  Output: 321
#
#
#  Example 2:
#
#  Input: x = -123
#  Output: -321
#
#
#  Example 3:
#
#  Input: x = 120
#  Output: 21
#
#
#
#  Constraints:
#
#
#  	-2³¹ <= x <= 2³¹ - 1
#

import unittest
from typing import List


#  start_marker
class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        res = 0
        if negative:
            x *= -1
        while x:
            digit = x % 10
            res *= 10
            x //= 10
            res += digit
        if negative:
            res *= -1
        if res > (2**31) - 1 or res < -(2**31):
            return 0
        return res
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        x = 123
        res = 321
        self.assertEqual(Solution().reverse(x), res)

    def test_case_2(self):
        x = -123
        res = -321
        self.assertEqual(Solution().reverse(x), res)

    def test_case_3(self):
        x = 120
        res = 21
        self.assertEqual(Solution().reverse(x), res)

    def test_case_4(self):
        x = 0
        res = 0
        self.assertEqual(Solution().reverse(x), res)

    def test_case_5(self):
        x = 1534236469
        res = 0
        self.assertEqual(Solution().reverse(x), res)

    def test_case_6(self):
        x = -2147483648
        res = 0
        self.assertEqual(Solution().reverse(x), res)

    def test_case_7(self):
        x = 1563847412
        res = 0
        self.assertEqual(Solution().reverse(x), res)


if __name__ == "__main__":
    unittest.main()
