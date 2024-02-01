#  Category: algorithms
#  Level: Easy
#  Percent: 70.11301%


#  Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#
#  Note:
#
#
#  	Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#  	In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
#
#
#
#  Example 1:
#
#  Input: n = 00000000000000000000000000001011
#  Output: 3
#  Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
#
#
#  Example 2:
#
#  Input: n = 00000000000000000000000010000000
#  Output: 1
#  Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
#
#
#  Example 3:
#
#  Input: n = 11111111111111111111111111111101
#  Output: 31
#  Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
#
#
#
#  Constraints:
#
#
#  	The input must be a binary string of length 32.
#
#
#
#  Follow up: If this function is called many times, how would you optimize it?


import unittest


#  start_marker
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


#  end_marker
class OldSolution:
    def hammingWeight_nybble(self, n: int) -> int:
        def count_nybble(n: int) -> int:
            match n:
                case 0:
                    return 0
                case 1:
                    return 1
                case 2:
                    return 1
                case 3:
                    return 2
                case 4:
                    return 1
                case 5:
                    return 2
                case 6:
                    return 2
                case 7:
                    return 3
                case 8:
                    return 1
                case 9:
                    return 2
                case 10:
                    return 2
                case 11:
                    return 3
                case 12:
                    return 2
                case 13:
                    return 3
                case 14:
                    return 3
                case 15:
                    return 4
                case _:
                    return 0

        total_bits = 0
        for i in range(8):
            last_nybble = n & 0xF
            n >>= 4
            total_bits += count_nybble(last_nybble)
        return total_bits

    def hammingWeight_clever_trimmed(self, n: int) -> int:
        # from https://wiki.python.org/moin/BitManipulation
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

    def hammingWeight_clever_orig(self, n: int) -> int:
        # from https://wiki.python.org/moin/BitManipulation
        def bitCount(int_type):
            count = 0
            while int_type:
                int_type &= int_type - 1
                count += 1
            return count

        return bitCount(n)


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input = int("00000000000000000000000000001011", 2)
        output = 3
        self.assertEqual(Solution().hammingWeight(input), output)

    def test_case_2(self):
        input = int("00000000000000000000000010000000", 2)
        output = 1
        self.assertEqual(Solution().hammingWeight(input), output)


if __name__ == "__main__":
    unittest.main()
