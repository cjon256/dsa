#  Category: algorithms
#  Level: Easy
#  Percent: 87.526%


#
# Given two integers num1 and num2, return the sum of the two integers.
#
#
#
# Example 1:
#
# Input: num1 = 12, num2 = 5
# Output: 17
# Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
#
# Example 2:
#
# Input: num1 = -10, num2 = 4
# Output: -6
# Explanation: num1 + num2 = -6, so -6 is returned.
#
#
#
# Constraints:
#
#     -100 <= num1, num2 <= 100
#
#
#

import unittest


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        num1 = 12
        num2 = 5
        expected = 17
        result = Solution().sum(num1, num2)
        self.assertEqual(result, expected)

    def test_case_2(self):
        num1 = -10
        num2 = 4
        expected = -6
        result = Solution().sum(num1, num2)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
