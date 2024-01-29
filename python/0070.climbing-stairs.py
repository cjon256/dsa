#  Category: algorithms
#  Level: Easy
#  Percent: 52.78638%
#
#  You are climbing a staircase. It takes n steps to reach the top.
#
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#  Example 1:
#
#  Input: n = 2
#  Output: 2
#  Explanation: There are two ways to climb to the top.
#  1. 1 step + 1 step
#  2. 2 steps
#
#
#  Example 2:
#
#  Input: n = 3
#  Output: 3
#  Explanation: There are three ways to climb to the top.
#  1. 1 step + 1 step + 1 step
#  2. 1 step + 2 steps
#  3. 2 steps + 1 step
#
#
#
#  Constraints:
#
#
#  	1 <= n <= 45
#

import unittest

#  start_marker
from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        j, k = 1, 1
        for _ in range(n - 1):
            j, k = k, j + k
        return k

    def climbStairs_precompute(self, n: int) -> int:
        fibs = [
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
            10946,
            17711,
            28657,
            46368,
            75025,
            121393,
            196418,
            317811,
            514229,
            832040,
            1346269,
            2178309,
            3524578,
            5702887,
            9227465,
            14930352,
            24157817,
            39088169,
            63245986,
            102334155,
            165580141,
            267914296,
            433494437,
            701408733,
            1134903170,
            1836311903,
        ]
        return fibs[n - 1]

    def climbStairs_memo(self, n: int) -> int:
        @cache
        def fib_r(m: int) -> int:
            match m:
                case 1:
                    return 1
                case 2:
                    return 2
                case _:
                    return fib_r(m - 1) + fib_r(m - 2)

        return fib_r(n)


#  end_marker
class TestSolution(unittest.TestCase):
    def test_1(self):
        assert Solution().climbStairs(1) == 1

    def test_2(self):
        assert Solution().climbStairs(2) == 2

    def test_3(self):
        assert Solution().climbStairs(3) == 3

    def test_4(self):
        assert Solution().climbStairs(4) == 5

    def test_5(self):
        assert Solution().climbStairs(5) == 8

    def test_6(self):
        assert Solution().climbStairs(6) == 13


if __name__ == "__main__":
    unittest.main()
