import unittest
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_only = re.compile(r'[^a-zA-Z0-9]+')
        s = alpha_only.sub('', s).lower()
        half_len = len(s)//2
        return s[:half_len] == s[-1:-(half_len+1):-1]


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertTrue(Solution().isPalindrome(""))
        self.assertTrue(Solution().isPalindrome("a"))
        self.assertTrue(Solution().isPalindrome("racecar"))
        self.assertTrue(Solution().isPalindrome("level"))
        self.assertTrue(Solution().isPalindrome(
            "A man, a plan, a canal: Panama"))
        self.assertFalse(Solution().isPalindrome("hello"))


if __name__ == '__main__':
    unittest.main()
