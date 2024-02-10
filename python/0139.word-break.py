#  Category: algorithms
#  Level: Medium
#  Percent: 46.531208%
# pylint: enable=useless-suppression, import-outside-toplevel
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring
# noqa: E402


#  Given a string s and a dictionary of strings wordDict, return true if s can
#  be segmented into a space-separated sequence of one or more dictionary
#  words.
#
#  Note that the same word in the dictionary may be reused multiple times in
#  the segmentation.
#
#
#  Example 1:
#
#  Input: s = "leetcode", wordDict = ["leet","code"]
#  Output: true
#  Explanation: Return true because "leetcode" can be segmented as "leet code".
#
#
#  Example 2:
#
#  Input: s = "applepenapple", wordDict = ["apple","pen"]
#  Output: true
#  Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#  Note that you are allowed to reuse a dictionary word.
#
#
#  Example 3:
#
#  Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#  Output: false
#
#
#
#  Constraints:
#
#
#  	1 <= s.length <= 300
#  	1 <= wordDict.length <= 1000
#  	1 <= wordDict[i].length <= 20
#  	s and wordDict[i] consist of only lowercase English letters.
#  	All the strings of wordDict are unique.
#

import unittest
from pprint import pprint as pp
from typing import Dict, List

#  start_marker


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie: Dict[str, Dict] = {}
        for word in wordDict:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node["+"] = {}
        positions = [False] * (len(s) + 1)
        positions[0] = True
        for i in range(len(s)):
            if not positions[i]:
                continue
            node = trie
            for j in range(i, len(s)):
                if s[j] not in node:
                    break
                node = node[s[j]]
                if "+" in node:
                    positions[j + 1] = True
        # print(positions)
        # print(trie)
        return positions[-1]


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        res = True
        self.assertEqual(Solution().wordBreak(s, wordDict), res)

    def test_case_2(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        res = True
        self.assertEqual(Solution().wordBreak(s, wordDict), res)

    def test_case_3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        res = False
        self.assertEqual(Solution().wordBreak(s, wordDict), res)


if __name__ == "__main__":
    unittest.main()
