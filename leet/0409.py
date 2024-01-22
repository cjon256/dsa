import unittest
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ctr = Counter(s)
        result = 0
        at_least_one_odd = False
        for v in ctr.values():
            result += v // 2
            if not at_least_one_odd and v % 2 == 1:
                at_least_one_odd = True
        return result * 2 + 1 if at_least_one_odd else result * 2


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
