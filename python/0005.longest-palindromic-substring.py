#  Category: algorithms
#  Level: Medium
#  Percent: 33.536964%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a string s, return the longest palindromic substring in s.
#
#
#  Example 1:
#
#  Input: s = "babad"
#  Output: "bab"
#  Explanation: "aba" is also a valid answer.
#
#
#  Example 2:
#
#  Input: s = "cbbd"
#  Output: "bb"
#
#
#
#  Constraints:
#
#
#  	1 <= s.length <= 1000
#  	s consist of only digits and English letters.
#


import unittest

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List


#  start_marker
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            return s[0]

        max_palindrome = s[0]
        two_centers = []
        three_centers = []
        for i in range(1, len(s) - 1):
            if s[i - 1] == s[i + 1]:
                three_centers.append(i)
            if s[i] == s[i - 1]:
                two_centers.append(i)
        if s[0] == s[1]:
            two_centers.append(0)
        if s[-1] == s[-2]:
            two_centers.append(len(s) - 1)

        def expand_three_center(center):
            nonlocal max_palindrome
            left = center - 1
            right = center + 1
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            if len(max_palindrome) < right - left - 1:
                max_palindrome = s[left + 1 : right]

        def expand_two_center(center):
            nonlocal max_palindrome
            left = center - 1
            right = center
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            if len(max_palindrome) < right - left - 1:
                max_palindrome = s[left + 1 : right]

        for center in three_centers:
            expand_three_center(center)
        for center in two_centers:
            expand_two_center(center)
        return max_palindrome


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "babad"
        expected = "bab"
        self.assertEqual(Solution().longestPalindrome(s), expected)

    def test_case_2(self):
        s = "cbbd"
        expected = "bb"
        self.assertEqual(Solution().longestPalindrome(s), expected)

    def test_case_3(self):
        s = "a"
        expected = "a"
        self.assertEqual(Solution().longestPalindrome(s), expected)

    def test_case_4(self):
        s = ""
        expected = ""
        self.assertEqual(Solution().longestPalindrome(s), expected)

    def test_case_5(self):
        s = "acc"
        expected = "cc"
        self.assertEqual(Solution().longestPalindrome(s), expected)

    def test_case_6(self):
        s = "acbc"
        expected = "cbc"
        self.assertEqual(Solution().longestPalindrome(s), expected)

    def test_case_7(self):
        s = "abcda"
        expected = "a"
        self.assertEqual(Solution().longestPalindrome(s), expected)

    def test_case_8(self):
        s = "dfgdcababacdgfdaeeea"
        expected = "dfgdcababacdgfd"
        self.assertEqual(Solution().longestPalindrome(s), expected)

    def test_case_9(self):
        s = "dfgdcayabacdgfdaeeea"
        expected = "aeeea"
        self.assertEqual(Solution().longestPalindrome(s), expected)

    def test_case_10(self):
        s = "dfgdcayacecdgfdaceea"
        expected = "cayac"
        self.assertEqual(Solution().longestPalindrome(s), expected)


if __name__ == "__main__":
    unittest.main()
