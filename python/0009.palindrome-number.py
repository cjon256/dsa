#  Category: algorithms
#  Level: Easy
#  Percent: 55.457413%
# pylint: disable=missing-module-docstring, invalid-name, missing-function-docstring, line-too-long,
# pylint: disable=missing-class-docstring, too-few-public-methods


#  Given an integer x, return true if x is a palindrome, and false otherwise.
#
#
#  Example 1:
#
#  Input: x = 121
#  Output: true
#  Explanation: 121 reads as 121 from left to right and from right to left.
#
#
#  Example 2:
#
#  Input: x = -121
#  Output: false
#  Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
#
#  Example 3:
#
#  Input: x = 10
#  Output: false
#  Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
#
#  Constraints:
#
#
#  	-2³¹ <= x <= 2³¹ - 1
#
#
#
#  Follow up: Could you solve it without converting the integer to a string?

import unittest


#  start_marker
class Solution:
    def isPalindrome(self, x: int) -> bool:
        whole_number = f"{x}"
        if len(whole_number) % 2 == 0:
            left_half = whole_number[: len(whole_number) // 2]
            right_half = whole_number[len(whole_number) // 2 :]
        else:
            left_half = whole_number[: len(whole_number) // 2]
            right_half = whole_number[len(whole_number) // 2 + 1 :]
        return left_half == right_half[::-1]


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        x = 121
        expected_result = True
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_2(self):
        x = -121
        expected_result = False
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_3(self):
        x = 10
        expected_result = False
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_4(self):
        x = 0
        expected_result = True
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_5(self):
        x = 12321
        expected_result = True
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_6(self):
        x = 123321
        expected_result = True
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_7(self):
        x = 1234321
        expected_result = True
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_8(self):
        x = 1234322
        expected_result = False
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_9(self):
        x = 123456789012345678909876543210987654321
        expected_result = True
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_10(self):
        x = 1234567890123456789098765432109876543210
        expected_result = False
        self.assertEqual(Solution().isPalindrome(x), expected_result)

    def test_case_11(self):
        x = -1234567890123456789098765432109876543210
        expected_result = False
        self.assertEqual(Solution().isPalindrome(x), expected_result)


if __name__ == "__main__":
    unittest.main()
