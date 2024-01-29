import unittest
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        def count_odd(s: str) -> int:
            ctr = Counter(s)
            result = 0
            for v in ctr.values():
                if v % 2 == 1:
                    result += 1
            return result

        num_odd = count_odd(s)
        if num_odd == 0:
            return len(s)
        return len(s) - num_odd + 1


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().longestPalindrome("babad"), 5)

    def test2(self):
        self.assertEqual(Solution().longestPalindrome("cbbd"), 3)

    def test3(self):
        self.assertEqual(Solution().longestPalindrome("abb"), 3)

    def test4(self):
        self.assertEqual(Solution().longestPalindrome("ac"), 1)

    def test5(self):
        self.assertEqual(Solution().longestPalindrome("abccccdd"), 7)

    def test6(self):
        self.assertEqual(Solution().longestPalindrome("aaaaccc"), 7)


if __name__ == "__main__":
    unittest.main()