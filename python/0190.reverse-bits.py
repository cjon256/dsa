#  Category: algorithms
#  Level: Easy
#  Percent: 57.43684%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Reverse bits of a given 32 bits unsigned integer.
#
#  Note:
#
#
#  	Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#  	In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
#
#
#
#  Example 1:
#
#  Input: n = 00000010100101000001111010011100
#  Output:    964176192 (00111001011110000010100101000000)
#  Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
#
#
#  Example 2:
#
#  Input: n = 11111111111111111111111111111101
#  Output:   3221225471 (10111111111111111111111111111111)
#  Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
#
#
#
#  Constraints:
#
#
#  	The input must be a binary string of length 32
#
#
#
#  Follow up: If this function is called many times, how would you optimize it?

import unittest


#  start_marker
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        n = 0b00000010100101000001111010011100
        expected_result = 964176192
        self.assertEqual(Solution().reverseBits(n), expected_result)

    def test_case_2(self):
        n = 0b11111111111111111111111111111101
        expected_result = 3221225471
        self.assertEqual(Solution().reverseBits(n), expected_result)

    def test_case_3(self):
        n = 0b00000000000000000000000000000000
        expected_result = 0
        self.assertEqual(Solution().reverseBits(n), expected_result)

    def test_case_4(self):
        n = 0b00000000000000000000000000000001
        expected_result = 2147483648
        self.assertEqual(Solution().reverseBits(n), expected_result)


if __name__ == "__main__":
    unittest.main()
