#  Category: algorithms
#  Level: Easy
#  Percent: 60.433704%


#  Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#  Symbol       Value
#  I             1
#  V             5
#  X             10
#  L             50
#  C             100
#  D             500
#  M             1000
#
#  For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
#  Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#
#  	I can be placed before V (5) and X (10) to make 4 and 9.
#  	X can be placed before L (50) and C (100) to make 40 and 90.
#  	C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
#  Given a roman numeral, convert it to an integer.
#
#
#  Example 1:
#
#  Input: s = "III"
#  Output: 3
#  Explanation: III = 3.
#
#
#  Example 2:
#
#  Input: s = "LVIII"
#  Output: 58
#  Explanation: L = 50, V= 5, III = 3.
#
#
#  Example 3:
#
#  Input: s = "MCMXCIV"
#  Output: 1994
#  Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
#  Constraints:
#
#
#  	1 <= s.length <= 15
#  	s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#  	It is guaranteed that s is a valid roman numeral in the range [1, 3999].
#


import unittest


#  start_marker
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev_char = ""
        for current_char in s:
            if current_char == "I":
                total += 1
                prev_char = "I"
            elif current_char == "V":
                if prev_char == "I":
                    total += 3
                else:
                    total += 5
                prev_char = "V"
            elif current_char == "X":
                if prev_char == "I":
                    total += 8
                else:
                    total += 10
                prev_char = "X"
            elif current_char == "L":
                if prev_char == "X":
                    total += 30
                else:
                    total += 50
                prev_char = "L"
            elif current_char == "C":
                if prev_char == "X":
                    total += 80
                else:
                    total += 100
                prev_char = "C"
            elif current_char == "D":
                if prev_char == "C":
                    total += 300
                else:
                    total += 500
                prev_char = "D"
            elif current_char == "M":
                if prev_char == "C":
                    total += 800
                else:
                    total += 1000
                prev_char = "M"
        return total


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input = "III"
        output = 3
        self.assertEqual(Solution().romanToInt(input), output)

    def test_case_2(self):
        input = "LVIII"
        output = 58
        self.assertEqual(Solution().romanToInt(input), output)

    def test_case_3(self):
        input = "MCMXCIV"
        output = 1994
        self.assertEqual(Solution().romanToInt(input), output)

    def test_case_4(self):
        input = "MCDLXXVI"
        output = 1476
        self.assertEqual(Solution().romanToInt(input), output)

    def test_case_5(self):
        input = "MMCDXIX"
        output = 2419
        self.assertEqual(Solution().romanToInt(input), output)


if __name__ == "__main__":
    unittest.main()
