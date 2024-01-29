#  Category: algorithms
#  Level: Easy
#  Percent: 77.91289%


#  Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
#
#
#  Example 1:
#
#  Input: n = 2
#  Output: [0,1,1]
#  Explanation:
#  0 --> 0
#  1 --> 1
#  2 --> 10
#
#
#  Example 2:
#
#  Input: n = 5
#  Output: [0,1,1,2,1,2]
#  Explanation:
#  0 --> 0
#  1 --> 1
#  2 --> 10
#  3 --> 11
#  4 --> 100
#  5 --> 101
#
#
#
#  Constraints:
#
#
#  	0 <= n <= 10⁵
#
#
#
#  Follow up:
#
#
#  	It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
#  	Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
#

import unittest
from typing import List


#  start_marker
class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(n + 1):
            bits.append(bin(i).count("1"))
        return bits


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input = 2
        output = [0, 1, 1]
        self.assertEqual(Solution().countBits(input), output)

    def test_case_2(self):
        input = 5
        output = [0, 1, 1, 2, 1, 2]
        self.assertEqual(Solution().countBits(input), output)

    def test_case_3(self):
        input = 0
        output = [0]
        self.assertEqual(Solution().countBits(input), output)

    def test_case_4(self):
        input = 1
        output = [0, 1]
        self.assertEqual(Solution().countBits(input), output)

    def test_case_5(self):
        input = 32
        output = [
            0,
            1,
            1,
            2,
            1,
            2,
            2,
            3,
            1,
            2,
            2,
            3,
            2,
            3,
            3,
            4,
            1,
            2,
            2,
            3,
            2,
            3,
            3,
            4,
            2,
            3,
            3,
            4,
            3,
            4,
            4,
            5,
            1,
        ]
        self.assertEqual(Solution().countBits(input), output)

    def test_case_6(self):
        input = 128
        ouput = []
        for i in range(129):
            ouput.append(bin(i).count("1"))
        self.assertEqual(Solution().countBits(input), ouput)


if __name__ == "__main__":
    unittest.main()
