#  Category: algorithms
#  Level: Medium
#  Percent: 64.00146%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#
#  Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
#  The test cases are generated so that the answer will be less than or equal to 2 * 10⁹.
#
#
#  Example 1:
#
#  Input: m = 3, n = 7
#  Output: 28
#
#
#  Example 2:
#
#  Input: m = 3, n = 2
#  Output: 3
#  Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
#  1. Right -> Down -> Down
#  2. Down -> Down -> Right
#  3. Down -> Right -> Down
#
#
#
#  Constraints:
#
#
#  	1 <= m, n <= 100
#

import math
import unittest


#  start_marker
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m

        return math.comb(m + n - 2, n - 1)
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        m = 3
        n = 1
        expected = 1
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_2(self):
        m = 3
        n = 2
        expected = 3
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_3(self):
        m = 3
        n = 3
        expected = 6
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_4(self):
        m = 3
        n = 4
        expected = 10
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_5(self):
        m = 3
        n = 7
        expected = 28
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_6(self):
        m = 1
        n = 1
        expected = 1
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_7(self):
        m = 1
        n = 2
        expected = 1
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_8(self):
        m = 2
        n = 2
        expected = 2
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_9(self):
        m = 2
        n = 3
        expected = 3
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_10(self):
        m = 2
        n = 4
        expected = 4
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_11(self):
        m = 2
        n = 5
        expected = 5
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_12(self):
        m = 2
        n = 6
        expected = 6
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_13(self):
        m = 2
        n = 7
        expected = 7
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_14(self):
        m = 2
        n = 8
        expected = 8
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_15(self):
        m = 2
        n = 9
        expected = 9
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_16(self):
        m = 4
        n = 1
        expected = 1
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_17(self):
        m = 4
        n = 2
        expected = 4
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_18(self):
        m = 4
        n = 3
        expected = 10
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_19(self):
        m = 4
        n = 4
        expected = 20
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_20(self):
        m = 4
        n = 5
        expected = 35
        self.assertEqual(Solution().uniquePaths(m, n), expected)

    def test_case_21(self):
        m = 4
        n = 6
        expected = 56
        self.assertEqual(Solution().uniquePaths(m, n), expected)


if __name__ == "__main__":
    unittest.main()
