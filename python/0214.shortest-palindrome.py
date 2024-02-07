#  Category: algorithms
#  Level: Hard
#  Percent: 33.052643%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given a string s. You can convert s to a palindrome by adding characters in front of it.
#
#  Return the shortest palindrome you can find by performing this transformation.
#
#
#  Example 1:
#  Input: s = "aacecaaa"
#  Output: "aaacecaaa"
#  Example 2:
#  Input: s = "abcd"
#  Output: "dcbabcd"
#
#
#  Constraints:
#
#
#  	0 <= s.length <= 5 * 10⁴
#  	s consists of lowercase English letters only.
#

import unittest


#  start_marker
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        def is_pal(s1):
            half_len = len(s1) // 2
            return s1[:half_len] == s1[-1 : -(half_len + 1) : -1]

        def find_longest_pre_palindrome2(s2):
            tail = len(s2) - 1
            while tail >= 0:
                if s2[0] == s2[tail]:
                    if is_pal(s2[0 : tail + 1]):
                        return tail + 1
                tail -= 1
            return 1

        if is_pal(s):
            return s
        longest = find_longest_pre_palindrome2(s)
        if longest == len(s):
            return s
        else:
            prefix = s[len(s) : longest - 1 : -1]
            return prefix + s


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "aacecaaa"
        res = "aaacecaaa"
        self.assertEqual(Solution().shortestPalindrome(s), res)

    def test_case_2(self):
        s = "abcd"
        res = "dcbabcd"
        self.assertEqual(Solution().shortestPalindrome(s), res)


if __name__ == "__main__":
    unittest.main()
