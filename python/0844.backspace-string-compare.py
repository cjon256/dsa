#  Category: algorithms
#  Level: Easy
#  Percent: 49.090725%
import unittest
from typing import Tuple

#  Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
#
#  Note that after backspacing an empty text, the text will continue empty.
#
#
#  Example 1:
#
#  Input: s = "ab#c", t = "ad#c"
#  Output: true
#  Explanation: Both s and t become "ac".
#
#
#  Example 2:
#
#  Input: s = "ab##", t = "c#d#"
#  Output: true
#  Explanation: Both s and t become "".
#
#
#  Example 3:
#
#  Input: s = "a#c", t = "b"
#  Output: false
#  Explanation: s becomes "c" while t becomes "b".
#
#
#
#  Constraints:
#
#
#  	1 <= s.length, t.length <= 200
#  	s and t only contain lowercase letters and '#' characters.
#
#
#
#  Follow up: Can you solve it in O(n) time and O(1) space?


#  start_marker
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next(str1: str, index: int) -> Tuple[str, int]:
            backspaces = 0
            for i in range(index, -1, -1):
                if str1[i] == "#":
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    return str1[i], i - 1
            return None, -1

        idx_s = len(s) - 1
        idx_t = len(t) - 1
        while True:
            s_char, idx_s = get_next(s, idx_s)
            t_char, idx_t = get_next(t, idx_t)
            if s_char is None and t_char is None:
                return True
            if s_char != t_char:
                return False
        return True


#  end_marker
class Solution_old:
    def backspaceCompare_simple(self, s: str, t: str) -> bool:
        def remove_backspaces(s: str) -> str:
            chars = []
            for char in s:
                if char == "#":
                    if chars:
                        chars.pop()
                else:
                    chars.append(char)
            return "".join(chars)

        return remove_backspaces(s) == remove_backspaces(t)


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "ab#c"
        t = "ad#c"
        answer = True
        self.assertEqual(Solution().backspaceCompare(s, t), answer)

    def test_case_2(self):
        s = "ab##"
        t = "c#d#"
        answer = True
        self.assertEqual(Solution().backspaceCompare(s, t), answer)

    def test_case_3(self):
        s = "a#c"
        t = "b"
        answer = False
        self.assertEqual(Solution().backspaceCompare(s, t), answer)

    def test_case_4(self):
        s = "a##c"
        t = "#a#c"
        answer = True
        self.assertEqual(Solution().backspaceCompare(s, t), answer)

    def test_case_5(self):
        s = "a#c"
        t = "b#c"
        answer = True
        self.assertEqual(Solution().backspaceCompare(s, t), answer)

    def test_case_6(self):
        s = "x#xx##x#"
        t = "y#f#o##f#"
        answer = True
        self.assertEqual(Solution().backspaceCompare(s, t), answer)

    def test_case_7(self):
        s = "bxj##tw"
        t = "bxj###tw"
        expected = False
        self.assertEqual(Solution().backspaceCompare(s, t), expected)

    def test_case_8(self):
        s = "bxjtw"
        t = "bxjtw"
        expected = True
        self.assertEqual(Solution().backspaceCompare(s, t), expected)

    def test_case_9(self):
        s = "bxjtw"
        t = "tw"
        expected = False
        self.assertEqual(Solution().backspaceCompare(s, t), expected)

    def test_case_10(self):
        s = "xj##tw"
        t = "bxj###tw"
        expected = True
        self.assertEqual(Solution().backspaceCompare(s, t), expected)

    def test_case_11(self):
        s = "aaaaaaa"
        t = "aaaaaaaa"
        expected = False
        self.assertEqual(Solution().backspaceCompare(s, t), expected)


if __name__ == "__main__":
    unittest.main()
