#  Category: algorithms
#  Level: Easy
#  Percent: 53.8822%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#
#  Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#
#
#  Example 1:
#
#  Input: s = "abccccdd"
#  Output: 7
#  Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#
#  Example 2:
#
#  Input: s = "a"
#  Output: 1
#  Explanation: The longest palindrome that can be built is "a", whose length is 1.
#
#
#
#  Constraints:
#
#
#  	1 <= s.length <= 2000
#  	s consists of lowercase and/or uppercase English letters only.
#

import unittest
from collections import Counter


#  start_marker
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
        #  end_marker


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
