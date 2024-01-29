#  Category: algorithms
#  Level: Easy
#  Percent: 40.373753%


#  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#  An input string is valid if:
#
#
#  	Open brackets must be closed by the same type of brackets.
#  	Open brackets must be closed in the correct order.
#  	Every close bracket has a corresponding open bracket of the same type.
#
#
#
#  Example 1:
#
#  Input: s = "()"
#  Output: true
#
#
#  Example 2:
#
#  Input: s = "()[]{}"
#  Output: true
#
#
#  Example 3:
#
#  Input: s = "(]"
#  Output: false
#
#
#
#  Constraints:
#
#
#  	1 <= s.length <= 10⁴
#  	s consists of parentheses only '()[]{}'.
#


import unittest


#  start_marker
class Solution:
    def isValid(self, s: str) -> bool:
        pstack = []
        try:
            for c in s:
                match c:
                    case "(" | "[" | "{":
                        pstack.append(c)
                    case ")":
                        opener = pstack.pop()
                        if opener != "(":
                            return False
                    case "]":
                        opener = pstack.pop()
                        if opener != "[":
                            return False
                    case "}":
                        opener = pstack.pop()
                        if opener != "{":
                            return False
            return not pstack
        except IndexError:
            return False


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "()"
        self.assertEqual(Solution().isValid(s), True)

    def test_case_2(self):
        s = "()[]{}"
        self.assertEqual(Solution().isValid(s), True)

    def test_case_3(self):
        s = "(]"
        self.assertEqual(Solution().isValid(s), False)


if __name__ == "__main__":
    unittest.main()
