# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods
import unittest

#  start_marker
from typing import assert_never


class Solution:
    def addBinary_1(self, a: str, b: str) -> str:
        def binfmt(n):
            if n == 0:
                return "0"
            binstr = ""
            while n > 0:
                if n % 2 == 0:
                    binstr = "0" + binstr
                else:
                    binstr = "1" + binstr
                n = n // 2
            return binstr

        return binfmt(int(a, 2) + int(b, 2))

    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        if len(a) < len(b):
            a, b = b, a
        diff = len(a) - len(b)
        for i in range(diff):
            b = "0" + b
        for i in range(len(a) - 1, -1, -1):
            match (a[i], b[i], carry):
                case ("0", "0", 0):
                    result = "0" + result
                    carry = 0
                case ("0", "0", 1):
                    result = "1" + result
                    carry = 0
                case ("0", "1", 0):
                    result = "1" + result
                    carry = 0
                case ("0", "1", 1):
                    result = "0" + result
                    carry = 1
                case ("1", "0", 0):
                    result = "1" + result
                    carry = 0
                case ("1", "0", 1):
                    result = "0" + result
                    carry = 1
                case ("1", "1", 0):
                    result = "0" + result
                    carry = 1
                case ("1", "1", 1):
                    result = "1" + result
                    carry = 1
                case _:
                    assert_never("Unexpected case")
        if carry:
            result = "1" + result
        return result


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        sol = Solution()
        a = "11"
        b = "1"
        expected = "100"
        self.assertEqual(sol.addBinary(a, b), expected)

    def test_case_2(self):
        sol = Solution()
        a = "1010"
        b = "1011"
        expected = "10101"
        self.assertEqual(sol.addBinary(a, b), expected)


if __name__ == "__main__":
    unittest.main()
