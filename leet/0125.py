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
        solution = Solution()

        # Test case 1: Empty string
        self.assertTrue(solution.isPalindrome(""))

        # Test case 2: Single character
        self.assertTrue(solution.isPalindrome("a"))

        # Test case 3: Palindrome with even length
        self.assertTrue(solution.isPalindrome("racecar"))

        # Test case 4: Palindrome with odd length
        self.assertTrue(solution.isPalindrome("level"))

        # Test case 5: Non-palindrome
        self.assertFalse(solution.isPalindrome("hello"))


if __name__ == '__main__':
    unittest.main()
class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertTrue(Solution().isPalindrome(""))
        self.assertTrue(Solution().isPalindrome("a"))
        self.assertTrue(Solution().isPalindrome("racecar"))
        self.assertTrue(Solution().isPalindrome("level"))
        self.assertTrue(Solution().isPalindrome(


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()

        # Test case 1: Empty string
        self.assertTrue(solution.isPalindrome(""))

        # Test case 2: Single character
        self.assertTrue(solution.isPalindrome("a"))

        # Test case 3: Palindrome with even length
        self.assertTrue(solution.isPalindrome("racecar"))

        # Test case 4: Palindrome with odd length
        self.assertTrue(solution.isPalindrome("level"))

        # Test case 5: Non-palindrome
        self.assertFalse(solution.isPalindrome("hello"))

        # Test case 6: Palindrome with special characters
        self.assertTrue(solution.isPalindrome(
            "A man, a plan, a canal: Panama"))

        # Test case 7: Non-palindrome with special characters
        self.assertFalse(solution.isPalindrome("race a car"))


if __name__ == '__main__':
    unittest.main()
