#  Category: algorithms
#  Level: Medium
#  Percent: 50.68141%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
#  Evaluate the expression. Return an integer that represents the value of the expression.
#
#  Note that:
#
#
#  	The valid operators are '+', '-', '*', and '/'.
#  	Each operand may be an integer or another expression.
#  	The division between two integers always truncates toward zero.
#  	There will not be any division by zero.
#  	The input represents a valid arithmetic expression in a reverse polish notation.
#  	The answer and all the intermediate calculations can be represented in a 32-bit integer.
#
#
#
#  Example 1:
#
#  Input: tokens = ["2","1","+","3","*"]
#  Output: 9
#  Explanation: ((2 + 1) * 3) = 9
#
#
#  Example 2:
#
#  Input: tokens = ["4","13","5","/","+"]
#  Output: 6
#  Explanation: (4 + (13 / 5)) = 6
#
#
#  Example 3:
#
#  Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#  Output: 22
#  Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#  = ((10 * (6 / (12 * -11))) + 17) + 5
#  = ((10 * (6 / -132)) + 17) + 5
#  = ((10 * 0) + 17) + 5
#  = (0 + 17) + 5
#  = 17 + 5
#  = 22
#
#
#
#  Constraints:
#
#
#  	1 <= tokens.length <= 10⁴
#  	tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
#


import unittest
from typing import List


#  start_marker
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # print("----------------")
        # print(f"tokens: {tokens}")
        if not tokens:
            return 0
        stack: List[int] = []
        for token in tokens:
            # print("----------------")
            # print(f"token: {token}")
            # print(f"stack before: {stack}")
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    denominator = stack.pop()
                    stack.append(stack.pop() - denominator)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    denominator = stack.pop()
                    numerator = stack.pop()
                    stack.append(int(numerator / denominator))
                case _:
                    stack.append(int(token))
        #     print(f"stack after: {stack}")
        # print(f"returning {stack[0]}")
        return stack.pop()


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        expected = 9
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_2(self):
        tokens = ["4", "13", "5", "/", "+"]
        expected = 6
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        expected = 22
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_4(self):
        tokens = ["4", "3", "-"]
        expected = 1
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_5(self):
        # test division truncation towards zero from negative number
        tokens = ["-1", "1", "/"]
        expected = -1
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_6(self):
        tokens = ["-1", "-1", "/"]
        expected = 1
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_7(self):
        tokens = ["-1", "-2", "/"]
        expected = 0
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_8(self):
        tokens = ["-1", "-3", "/"]
        expected = 0
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_9(self):
        tokens = ["-1", "-4", "/"]
        expected = 0
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_10(self):
        tokens = ["-1", "-5", "/"]
        expected = 0
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_11(self):
        tokens = ["-1", "-6", "/"]
        expected = 0
        self.assertEqual(Solution().evalRPN(tokens), expected)

    def test_case_12(self):
        tokens = ["-1", "-7"]
        expected = -7
        self.assertEqual(Solution().evalRPN(tokens), expected)


if __name__ == "__main__":
    unittest.main()
