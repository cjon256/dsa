#  Category: algorithms
#  Level: Easy
#  Percent: 85.19016%


#  Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
#
#  A string is represented by an array if the array elements concatenated in order forms the string.
#
#
#  Example 1:
#
#  Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
#  Output: true
#  Explanation:
#  word1 represents string "ab" + "c" -> "abc"
#  word2 represents string "a" + "bc" -> "abc"
#  The strings are the same, so return true.
#
#  Example 2:
#
#  Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
#  Output: false
#
#
#  Example 3:
#
#  Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
#  Output: true
#
#
#
#  Constraints:
#
#
#  	1 <= word1.length, word2.length <= 10³
#  	1 <= word1[i].length, word2[i].length <= 10³
#  	1 <= sum(word1[i].length), sum(word2[i].length) <= 10³
#  	word1[i] and word2[i] consist of lowercase letters.
#


import unittest

#  start_marker
from itertools import chain, zip_longest
from typing import List


class Solution:
    """
    https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
    num = 1662
    """

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if word1 is word2:
            return True
        for l1, l2 in zip_longest(
            chain.from_iterable(word1), chain.from_iterable(word2)
        ):
            if l1 != l2:
                return False
        return True


#  end_marker
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        word1 = ["ab", "c"]
        word2 = ["a", "bc"]
        self.assertEqual(self.solution.arrayStringsAreEqual(word1, word2), True)

    def test_2(self):
        word1 = ["a", "cb"]
        word2 = ["ab", "c"]
        self.assertEqual(self.solution.arrayStringsAreEqual(word1, word2), False)

    def test_3(self):
        word1 = ["abc", "d", "defg"]
        word2 = ["abcddefg"]
        self.assertEqual(self.solution.arrayStringsAreEqual(word1, word2), True)


if __name__ == "__main__":
    unittest.main()
