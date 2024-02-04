#  Category: algorithms
#  Level: Medium
#  Percent: 34.425365%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring
#


#  Given a string s, find the length of the longest substring without repeating
#  characters.
#
#
#  Example 1:
#
#  Input: s = "abcabcbb"
#  Output: 3
#  Explanation: The answer is "abc", with the length of 3.
#
#
#  Example 2:
#
#  Input: s = "bbbbb"
#  Output: 1
#  Explanation: The answer is "b", with the length of 1.
#
#
#  Example 3:
#
#  Input: s = "pwwkew"
#  Output: 3
#  Explanation: The answer is "wke", with the length of 3.
#  Notice that the answer must be a substring, "pwke" is a subsequence and not
#  a substring.
#
#
#
#  Constraints:
#
#
#  	0 <= s.length <= 5 * 10⁴
#  	s consists of English letters, digits, symbols and spaces.
#

import unittest

#  start_marker
from collections import defaultdict
from typing import Dict, List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        start = 0
        end = 1
        letters_between = set(s[start])
        max_length = 0
        while end < len(s):
            if s[end] not in letters_between:
                letters_between.add(s[end])
                end += 1
            else:
                letters_between.remove(s[start])
                start += 1
            if end - start > max_length:
                max_length = end - start
        return max_length
        # end_marker


class OldSolution:
    def lengthOfLongestSubstring_still_slow(self, s: str) -> int:
        if not s:
            return 0

        letter_positions: Dict[str, int] = {}
        next_position: Dict[int, int] = defaultdict(lambda: len(s))
        for i, c in enumerate(s):
            if c in letter_positions:
                next_position[letter_positions[c]] = i
            letter_positions[c] = i
        del letter_positions

        longest_seen = 0
        for i in range(len(s)):
            next_pos = next_position[i]
            j = i + 1
            while j < next_pos:
                next_pos = min(next_pos, next_position[j])
                j += 1
            longest_seen = max(longest_seen, next_pos - i)
        return longest_seen
        #  end_marker

    def lengthOfLongestSubstring_slowwww(self, s: str) -> int:
        if not s:
            return 0

        letter_positions: Dict[str, List[int]] = defaultdict(list)
        for i, c in enumerate(s):
            letter_positions[c].append(i)
        if max(len(v) for v in letter_positions.values()) == 1:
            return len(s)

        def next_position_(c: str, current_position: int) -> int:
            positions = letter_positions[c]

            for i in positions:
                if i > current_position:
                    return i
            return len(s)

        longest_seen = 0
        for i, c1 in enumerate(s):
            next_pos = next_position_(c1, i)
            j = i + 1
            while j < next_pos:
                c2 = s[j]
                next_pos = min(next_pos, next_position_(c2, j))
                j += 1
            longest_seen = max(longest_seen, next_pos - i)
        return longest_seen


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "abcabcbb"
        expected_result = 3
        result = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        s = "bbbbb"
        expected_result = 1
        result = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        s = "pwwkew"
        expected_result = 3
        result = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(result, expected_result)

    def test_case_4(self):
        s = ""
        expected_result = 0
        result = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(result, expected_result)

    def test_case_5(self):
        s = "snthdaoeuiypfgcrlqjkxmwvzb"
        expected_result = 26
        result = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
