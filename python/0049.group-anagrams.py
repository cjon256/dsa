#  Category: algorithms
#  Level: Medium
#  Percent: 67.49146%


#  Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
#  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#  Example 1:
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
#  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#  Example 2:
#  Input: strs = [""]
#  Output: [[""]]
#  Example 3:
#  Input: strs = ["a"]
#  Output: [["a"]]
#
#
#  Constraints:
#
#
#  	1 <= strs.length <= 10⁴
#  	0 <= strs[i].length <= 100
#  	strs[i] consists of lowercase English letters.
#


import unittest
from typing import List


#  start_marker
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}

        output = []
        for word in strs:
            cw = "".join(sorted(word))
            if cw in anagrams_dict:
                anagrams_dict[cw].append(word)
            else:
                word_list = [word]
                output.append(word_list)
                anagrams_dict[cw] = word_list
        return output


def sort_and_compare(list1: List[List[str]], list2: List[List[str]]):
    list1.sort(key=lambda x: len(x))
    list2.sort(key=lambda x: len(x))
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if set(list1[i]) != set(list2[i]):
            return False
    return True


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertTrue(sort_and_compare(Solution().groupAnagrams(strs), output))

    def test_case_2(self):
        strs = [""]
        output = [[""]]
        self.assertEqual(Solution().groupAnagrams(strs), output)

    def test_case_3(self):
        strs = ["a"]
        output = [["a"]]
        self.assertEqual(Solution().groupAnagrams(strs), output)


if __name__ == "__main__":
    unittest.main()
