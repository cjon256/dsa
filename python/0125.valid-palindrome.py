#  Category: algorithms
#  Level: Easy
#  Percent: 46.640915%


#  A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
#  Given a string s, return true if it is a palindrome, or false otherwise.
#
#
#  Example 1:
#
#  Input: s = "A man, a plan, a canal: Panama"
#  Output: true
#  Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
#  Example 2:
#
#  Input: s = "race a car"
#  Output: false
#  Explanation: "raceacar" is not a palindrome.
#
#
#  Example 3:
#
#  Input: s = " "
#  Output: true
#  Explanation: s is an empty string "" after removing non-alphanumeric characters.
#  Since an empty string reads the same forward and backward, it is a palindrome.
#
#
#
#  Constraints:
#
#
#  	1 <= s.length <= 2 * 10⁵
#  	s consists only of printable ASCII characters.
#
import re
import timeit
import unittest


#  start_marker
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_only = re.compile(r"[^a-zA-Z0-9]+")
        s = alpha_only.sub("", s).lower()
        half_len = len(s) // 2
        return s[:half_len] == s[-1 : -(half_len + 1) : -1]


#  end_marker
class TestSolution(unittest.TestCase):
    def test_isPalindrome_01(self):
        # Test case 1: Empty string
        self.assertTrue(Solution().isPalindrome(""))

    def test_isPalindrome_02(self):
        # Test case 2: Single character
        self.assertTrue(Solution().isPalindrome("a"))

    def test_isPalindrome_03(self):
        # Test case 3: Palindrome with even length
        self.assertTrue(Solution().isPalindrome("racecar"))

    def test_isPalindrome_04(self):
        # Test case 4: Palindrome with odd length
        self.assertTrue(Solution().isPalindrome("level"))

    def test_isPalindrome_05(self):
        # Test case 5: Non-palindrome
        self.assertFalse(Solution().isPalindrome("hello"))

    def test_isPalindrome_06(self):
        # Test case 6: Palindrome with special characters
        self.assertTrue(Solution().isPalindrome("A man, a plan, a canal: Panama"))

    def test_isPalindrome_07(self):
        # Test case 7: Non-palindrome with special characters
        self.assertFalse(Solution().isPalindrome("race a car"))

    def test_isPalindrome_08(self):
        # Test case 8: Extremely long palindrome
        self.assertTrue(Solution().isPalindrome("a" * 1000000))

    def test_isPalindrome_09(self):
        # Test case 9: Extremely long non-palindrome
        self.assertFalse(Solution().isPalindrome("a" * 1000000 + "b"))

    def test_isPalindrome_10(self):
        # Test case 10: Extremely long palindrome with special characters
        start = timeit.default_timer()
        self.assertTrue(
            Solution().isPalindrome(("a" * 1000000 + "b") * 1000000 + "a" * 1000000)
        )
        stop = timeit.default_timer()
        print("Time for test_10: ", stop - start)

    def test_isPalindrome_11(self):
        # Test case 11: Extremely long non-palindrome with special characters
        start = timeit.default_timer()
        self.assertFalse(
            Solution().isPalindrome(
                ("a" * 1000000 + "b") * 1000000 + "ab" * 1000000 + "a"
            )
        )
        stop = timeit.default_timer()
        print("Time for test_11: ", stop - start)


if __name__ == "__main__":
    unittest.main()
