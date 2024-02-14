#  Category: algorithms
#  Level: Medium
#  Percent: 59.717697%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
#  A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#  Example 1:
#
#  Input: digits = "23"
#  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
#  Example 2:
#
#  Input: digits = ""
#  Output: []
#
#
#  Example 3:
#
#  Input: digits = "2"
#  Output: ["a","b","c"]
#
#
#
#  Constraints:
#
#
#  	0 <= digits.length <= 4
#  	digits[i] is a digit in the range ['2', '9'].
#


import unittest
from itertools import product
from typing import List


#  start_marker
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        LETTERS = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        letters_for_nums = [LETTERS[n] for n in digits]
        return list(map(lambda a: "".join(a), product(*letters_for_nums)))
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        result = Solution().letterCombinations(digits)
        self.assertEqual(result, expected)

    def test_case_2(self):
        digits = ""
        expected = []
        result = Solution().letterCombinations(digits)
        self.assertEqual(result, expected)

    def test_case_3(self):
        digits = "2"
        expected = ["a", "b", "c"]
        result = Solution().letterCombinations(digits)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
