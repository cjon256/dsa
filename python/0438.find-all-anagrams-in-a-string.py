#  Category: algorithms
#  Level: Medium
#  Percent: 50.70218%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
#  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#  Example 1:
#
#  Input: s = "cbaebabacd", p = "abc"
#  Output: [0,6]
#  Explanation:
#  The substring with start index = 0 is "cba", which is an anagram of "abc".
#  The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#  Example 2:
#
#  Input: s = "abab", p = "ab"
#  Output: [0,1,2]
#  Explanation:
#  The substring with start index = 0 is "ab", which is an anagram of "ab".
#  The substring with start index = 1 is "ba", which is an anagram of "ab".
#  The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#
#  Constraints:
#
#
#  	1 <= s.length, p.length <= 3 * 10⁴
#  	s and p consist of lowercase English letters.
#


import unittest
from collections import Counter

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List


#  start_marker
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        res: list[int] = []
        counter_p = [0] * 26
        counter_s = [0] * 26
        start = 0
        end_ = 0
        for end_ in range(len(p)):
            counter_p[ord(p[end_]) - ord("a")] += 1
            counter_s[ord(s[end_]) - ord("a")] += 1
        while True:
            if counter_p == counter_s:
                res.append(start)
            end_ += 1
            if end_ == len(s):
                break
            counter_s[ord(s[start]) - ord("a")] -= 1
            counter_s[ord(s[end_]) - ord("a")] += 1
            start += 1
        return res
        #  end_marker

    def findAnagrams_counter(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        res: list[int] = []
        counter_p = Counter(p)
        counter_s: Counter[str] = Counter(s[: len(p)])
        start = 0
        end_ = len(p) - 1
        while True:
            if counter_p == counter_s:
                res.append(start)
            end_ += 1
            if end_ == len(s):
                break
            counter_s.subtract(s[start])
            counter_s.update(s[end_])
            start += 1
        return res


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "cbaebabacd"
        p = "abc"
        expected = [0, 6]
        self.assertEqual(Solution().findAnagrams(s, p), expected)

    def test_case_2(self):
        s = "abab"
        p = "ab"
        expected = [0, 1, 2]
        self.assertEqual(Solution().findAnagrams(s, p), expected)

    def test_case_3(self):
        s = "aa"
        p = "bb"
        expected = []
        self.assertEqual(Solution().findAnagrams_counter(s, p), expected)


if __name__ == "__main__":
    unittest.main()
