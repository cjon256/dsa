import unittest
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_only = re.compile(r'[^a-zA-Z0-9]+')
        s = alpha_only.sub('', s).lower()
        half_len = len(s)//2
        return s[:half_len] == s[-1:-(half_len+1):-1]


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
        self.assertTrue(Solution().isPalindrome(
            "A man, a plan, a canal: Panama"))

    def test_isPalindrome_07(self):
        # Test case 7: Non-palindrome with special characters
        self.assertFalse(Solution().isPalindrome("race a car"))

    def test_isPalindrome_08(self):
        # Test case 8: Extremely long palindrome
        self.assertTrue(Solution().isPalindrome("a"*1000000))

    def test_isPalindrome_09(self):
        # Test case 9: Extremely long non-palindrome
        self.assertFalse(Solution().isPalindrome("a"*1000000+"b"))


if __name__ == '__main__':
    unittest.main()
