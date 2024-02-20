#  Category: algorithms
#  Level: Medium
#  Percent: 39.274597%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  A permutation of an array of integers is an arrangement of its members into
#  a sequence or linear order.
#
#
#  	For example, for arr = [1,2,3], the following are all the permutations of arr:
#     [1,2,3],
#     [1,3,2],
#     [2,1,3],
#     [2,3,1],
#     [3,1,2],
#     [3,2,1].
#
#
#  The next permutation of an array of integers is the next lexicographically
#  greater permutation of its integer. More formally, if all the permutations
#  of the array are sorted in one container according to their lexicographical
#  order, then the next permutation of that array is the permutation that
#  follows it in the sorted container. If such arrangement is not possible, the
#  array must be rearranged as the lowest possible order (i.e., sorted in
#  ascending order).
#
#
#  	For example, the next permutation of arr = [1,2,3] is [1,3,2].
#  	Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
#  	While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does
#  	not have a lexicographical larger rearrangement.
#
#
#  Given an array of integers nums, find the next permutation of nums.
#
#  The replacement must be in place and use only constant extra memory.
#
#
#  Example 1:
#
#  Input: nums = [1,2,3]
#  Output: [1,3,2]
#
#
#  Example 2:
#
#  Input: nums = [3,2,1]
#  Output: [1,2,3]
#
#
#  Example 3:
#
#  Input: nums = [1,1,5]
#  Output: [1,5,1]
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 100
#  	0 <= nums[i] <= 100
#

import unittest
from typing import List


#  start_marker
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        if nums[-2] < nums[-1]:
            nums[-2], nums[-1] = nums[-1], nums[-2]
            return
        pivot = -1
        for i in range(len(nums) - 1, 0, -1):
            # print(f"{i=} {nums[i-1]=} {nums[i]}")
            if nums[i - 1] < nums[i]:
                pivot = i
                break
        if pivot == -1:
            nums[:] = reversed(nums)
            return
        value_before = nums[pivot - 1]
        # print(f"{pivot=} {value_before=}")
        least_idx = 101

        for i in range(len(nums) - 1, pivot - 1, -1):
            curr = nums[i]
            if least_idx == 101:
                least = 101
            else:
                least = nums[least_idx]

            if curr < least and curr > value_before:
                least_idx = i
            # print(f"{i=} {curr=} {least=} {least_idx=}")
        # print(f"{pivot=} {least_idx=}")
        # print(nums[pivot:])
        # print(f"nums before swp: {nums}")
        nums[pivot - 1], nums[least_idx] = nums[least_idx], nums[pivot - 1]
        # print(f"nums after swap: {nums}")
        # print(f"nums[pivot:] = {nums[pivot:]}")
        nums[pivot:] = reversed(nums[pivot:])
        # print(f"nums after revs: {nums}")

        """
        Do not return anything, modify nums in-place instead.
        """

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 4, 5, 3]
        expected = [1, 2, 5, 3, 4]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_case_2(self):
        nums = [1, 2, 3]
        expected = [1, 3, 2]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_case_3(self):
        nums = [3, 2, 1]
        expected = [1, 2, 3]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_case_4(self):
        nums = [2, 3, 1, 3, 3]
        expected = [2, 3, 3, 1, 3]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_case_X(self):
        s = Solution()
        nums = [1, 2, 3, 4]
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)
        s.nextPermutation(nums)
        print(nums)


if __name__ == "__main__":
    unittest.main()
