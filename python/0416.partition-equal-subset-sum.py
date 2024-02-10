#  Category: algorithms
#  Level: Medium
#  Percent: 46.217373%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
#
#
#  Example 1:
#
#  Input: nums = [1,5,11,5]
#  Output: true
#  Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
#  Example 2:
#
#  Input: nums = [1,2,3,5]
#  Output: false
#  Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 200
#  	1 <= nums[i] <= 100
#


import unittest
from itertools import permutations
from typing import List


#  start_marker
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half_total = total // 2
        computable_sums = [False] * (half_total + 1)
        computable_sums[0] = True
        nums.sort()
        biggest = nums.pop()
        if biggest > half_total:
            return False
        if biggest == half_total:
            return True
        computable_sums[biggest] = True
        for n in nums:
            for i in range(half_total, n - 1, -1):
                # a number is computable if we marked it before or
                # if this number minus the current n is computable
                computable_sums[i] = computable_sums[i] or computable_sums[i - n]
        return computable_sums[half_total]
        #  end_marker

    def canPartition_permutation_slow(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half_total = total // 2
        computable = [False] * (half_total + 1)
        computable[0] = True
        for seq in permutations(nums):
            seqlist = list(seq)
            sum_ = 0
            while sum_ < half_total:
                n = seqlist.pop()
                sum_ += n
                if sum_ <= half_total:
                    computable[sum_] = True
        return computable[half_total]


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 5, 11, 5]
        expected = True
        self.assertEqual(Solution().canPartition(nums), expected)

    def test_case_2(self):
        nums = [1, 2, 3, 5]
        expected = False
        self.assertEqual(Solution().canPartition(nums), expected)

    def test_case_3(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        expected = True
        self.assertEqual(Solution().canPartition(nums), expected)

    def test_case_4(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = True
        self.assertEqual(Solution().canPartition(nums), expected)

    def test_case_5(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = False
        self.assertEqual(Solution().canPartition(nums), expected)

    def test_case_6(self):
        nums = [1, 2, 5]
        expected = False
        self.assertEqual(Solution().canPartition(nums), expected)


if __name__ == "__main__":
    unittest.main()
