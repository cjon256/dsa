#  Category: algorithms
#  Level: Easy
#  Percent: 42.204334%


#  Write a function to find the longest common prefix string amongst an array of strings.
#
#  If there is no common prefix, return an empty string "".
#
#
#  Example 1:
#
#  Input: strs = ["flower","flow","flight"]
#  Output: "fl"
#
#
#  Example 2:
#
#  Input: strs = ["dog","racecar","car"]
#  Output: ""
#  Explanation: There is no common prefix among the input strings.
#
#
#
#  Constraints:
#
#
#  	1 <= strs.length <= 200
#  	0 <= strs[i].length <= 200
#  	strs[i] consists of only lowercase English letters.
#

import unittest
from typing import List


#  start_marker
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        retstr = ""
        for i, j in enumerate(zip(*strs)):
            s = set(j)
            if len(s) > 1:
                return retstr
            retstr += j[0]
        return retstr


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        result = Solution().longestCommonPrefix(["flower", "flow", "flight"])
        self.assertEqual(result, "fl")

    def test_case_2(self):
        result = Solution().longestCommonPrefix(["dog", "racecar", "car"])
        self.assertEqual(result, "")

    def test_case_3(self):
        result = Solution().longestCommonPrefix(["dog"])
        self.assertEqual(result, "dog")

    def test_case_4(self):
        result = Solution().longestCommonPrefix([])
        self.assertEqual(result, "")

    def test_case_5(self):
        result = Solution().longestCommonPrefix(["", ""])
        self.assertEqual(result, "")

    def test_case_6(self):
        result = Solution().longestCommonPrefix(["", "a"])
        self.assertEqual(result, "")

    def test_case_7(self):
        result = Solution().longestCommonPrefix(["a", ""])
        self.assertEqual(result, "")

    def test_case_8(self):
        result = Solution().longestCommonPrefix(["a", "a"])
        self.assertEqual(result, "a")

    def test_case_9(self):
        result = Solution().longestCommonPrefix(["a", "ab"])
        self.assertEqual(result, "a")


if __name__ == "__main__":
    unittest.main()
