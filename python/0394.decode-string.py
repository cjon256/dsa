#  Category: algorithms
#  Level: Medium
#  Percent: 58.964764%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an encoded string, return its decoded string.
#
#  The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
#  You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
#  The test cases are generated so that the length of the output will never exceed 10⁵.
#
#
#  Example 1:
#
#  Input: s = "3[a]2[bc]"
#  Output: "aaabcbc"
#
#
#  Example 2:
#
#  Input: s = "3[a2[c]]"
#  Output: "accaccacc"
#
#
#  Example 3:
#
#  Input: s = "2[abc]3[cd]ef"
#  Output: "abcabccdcdcdef"
#
#
#
#  Constraints:
#
#
#  	1 <= s.length <= 30
#  	s consists of lowercase English letters, digits, and square brackets '[]'.
#  	s is guaranteed to be a valid input.
#  	All the integers in s are in the range [1, 300].
#

import unittest


#  start_marker
class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def decoder_r():
            nonlocal i
            res = ""
            number = ""
            repeat = 0
            while i < len(s):
                c = s[i]
                match c:
                    case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                        number += c
                    case "[":
                        repeat = int(number)
                        number = ""
                        i += 1
                        rstr = decoder_r()
                        res += rstr * repeat
                    case "]":
                        return res
                        # we do not increment 1 because caller will handle
                    case _:
                        res += c
                i += 1
            return res

        return decoder_r()
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "3[a]"
        expected = "aaa"
        result = Solution().decodeString(s)
        self.assertEqual(result, expected)

    def test_case_2(self):
        s = "13[a]"
        expected = "aaaaaaaaaaaaa"
        result = Solution().decodeString(s)
        self.assertEqual(result, expected)

    def test_case_3(self):
        s = "3[a]2[bc]"
        expected = "aaabcbc"
        result = Solution().decodeString(s)
        self.assertEqual(result, expected)

    def test_case_4(self):
        s = "3[a2[c]]"
        expected = "accaccacc"
        result = Solution().decodeString(s)
        self.assertEqual(result, expected)

    def test_case_5(self):
        s = "2[abc]3[cd]ef"
        expected = "abcabccdcdcdef"
        result = Solution().decodeString(s)
        self.assertEqual(result, expected)

    def test_case_6(self):
        s = "abc"
        expected = "abc"
        result = Solution().decodeString(s)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
