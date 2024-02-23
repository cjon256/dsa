#  Category: algorithms
#  Level: Medium
#  Percent: 57.76931%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an array of strings words and an integer k, return the k most frequent strings.
#
#  Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
#
#
#  Example 1:
#
#  Input: words = ["i","love","leetcode","i","love","coding"], k = 2
#  Output: ["i","love"]
#  Explanation: "i" and "love" are the two most frequent words.
#  Note that "i" comes before "love" due to a lower alphabetical order.
#
#
#  Example 2:
#
#  Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
#  Output: ["the","is","sunny","day"]
#  Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
#
#
#
#  Constraints:
#
#
#  	1 <= words.length <= 500
#  	1 <= words[i].length <= 10
#  	words[i] consists of lowercase English letters.
#  	k is in the range [1, The number of unique words[i]]
#
#
#
#  Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?


import unittest
from typing import List

DUMMY = None

#  start_marker
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_list = Counter(words).most_common()
        words_in_order = []
        last_count = word_list[0][1]
        words_at_this_count = []
        for i in range(len(word_list)):
            word = word_list[i][0]
            freq = word_list[i][1]
            if freq == last_count:
                words_at_this_count.append(word)
            else:
                words_in_order.extend(sorted(words_at_this_count))
                words_at_this_count = [word]
                last_count = word_list[i][1]
        if words_at_this_count:
            words_at_this_count.sort()
            words_in_order.extend(words_at_this_count)

        return words_in_order[:k]
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        expected = ["i", "love"]
        result = Solution().topKFrequent(words, k)
        self.assertEqual(result, expected)

    def test_case_2(self):
        words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        k = 4
        expected = ["the", "is", "sunny", "day"]
        result = Solution().topKFrequent(words, k)
        self.assertEqual(result, expected)

    def test_case_3(self):
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 3
        expected = ["i", "love", "coding"]
        result = Solution().topKFrequent(words, k)
        self.assertEqual(result, expected)

    def test_case_4(self):
        words = ["i", "love", "leetcode", "i", "like", "coding"]
        k = 3
        expected = ["i", "coding", "leetcode"]
        result = Solution().topKFrequent(words, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
