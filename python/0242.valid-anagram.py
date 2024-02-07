#  Category: algorithms
#  Level: Easy
#  Percent: 64.1548%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#  Example 1:
#  Input: s = "anagram", t = "nagaram"
#  Output: true
#  Example 2:
#  Input: s = "rat", t = "car"
#  Output: false
#
#
#  Constraints:
#
#
#  	1 <= s.length, t.length <= 5 * 10⁴
#  	s and t consist of lowercase English letters.
#
#
#
#  Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

import unittest
from collections import Counter


#  start_marker
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(t) == Counter(s)


# end_marker
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isAnagram(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))
        self.assertFalse(self.solution.isAnagram("rat", "car"))


if __name__ == "__main__":
    unittest.main()
