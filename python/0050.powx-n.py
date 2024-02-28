#  Category: algorithms
#  Level: Medium
#  Percent: 34.497135%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
#
#  Example 1:
#
#  Input: x = 2.00000, n = 10
#  Output: 1024.00000
#
#
#  Example 2:
#
#  Input: x = 2.10000, n = 3
#  Output: 9.26100
#
#
#  Example 3:
#
#  Input: x = 2.00000, n = -2
#  Output: 0.25000
#  Explanation: 2-2 = 1/2² = 1/4 = 0.25
#
#
#
#  Constraints:
#
#
#  	-100.0 < x < 100.0
#  	-2³¹ <= n <= 2³¹-1
#  	n is an integer.
#  	Either x is not zero or n > 0.
#  	-10⁴ <= xn <= 10⁴
#

import unittest


#  start_marker
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        if n < 0:
            x = 1 / x
            n *= -1
        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2
        return res

    def myPow_simple(self, x: float, n: int) -> float:
        return x**n
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        x = 2.00000
        n = 10
        res = 1024.00000
        self.assertEqual(Solution().myPow(x, n), res)

    def test_case_2(self):
        x = 2.10000
        n = 3
        res = 9.26100
        self.assertAlmostEqual(Solution().myPow(x, n), res)

    def test_case_3(self):
        x = 2.00000
        n = -2
        res = 0.25000
        self.assertEqual(Solution().myPow(x, n), res)

    def test_case_4(self):
        x = 2.00000
        n = 0
        res = 1
        self.assertEqual(Solution().myPow(x, n), res)

    def test_case_5(self):
        x = 0.00001
        n = 2147483647
        res = 0
        self.assertEqual(Solution().myPow(x, n), res)

    def test_case_6(self):
        x = 2.00000
        n = -2147483648
        res = 0
        self.assertEqual(Solution().myPow(x, n), res)

    def test_case_7(self):
        x = 1.00000
        n = 2147483647
        res = 1
        self.assertEqual(Solution().myPow(x, n), res)

    def test_case_8(self):
        x = 1.00000
        n = -2147483648
        res = 1
        self.assertEqual(Solution().myPow(x, n), res)


if __name__ == "__main__":
    unittest.main()
