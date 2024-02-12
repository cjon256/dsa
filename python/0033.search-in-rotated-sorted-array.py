#  Category: algorithms
#  Level: Medium
#  Percent: 40.370457%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#  There is an integer array nums sorted in ascending order (with distinct values).
#
#  Prior to being passed to your function, nums is possibly rotated at an
#  unknown pivot index k (1 <= k < nums.length) such that the resulting array
#  is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
#  (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
#  and become [4,5,6,7,0,1,2].
#
#  Given the array nums after the possible rotation and an integer target,
#  return the index of target if it is in nums, or -1 if it is not in nums.
#
#  You must write an algorithm with O(log n) runtime complexity.
#
#
#  Example 1:
#    Input: nums = [4,5,6,7,0,1,2], target = 0
#    Output: 4
#  Example 2:
#    Input: nums = [4,5,6,7,0,1,2], target = 3
#    Output: -1
#  Example 3:
#    Input: nums = [1], target = 0
#    Output: -1
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 5000
#  	-10⁴ <= nums[i] <= 10⁴
#  	All values of nums are unique.
#  	nums is an ascending array that is possibly rotated.
#  	-10⁴ <= target <= 10⁴
#


import unittest
from typing import List


#  start_marker
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def bin_search(left: int, right: int) -> int:
            mid = (right - left) // 2 + left
            # print(f"left: {left}, right: {right}, mid: {mid}")
            if nums[mid] == target:
                return mid
            if left == right:
                return -1
            if len(nums) == 1:
                return -1
            if nums[mid] < target:
                # print(f"nums[mid] < target, mid: {mid}, right: {right}")
                return bin_search(mid + 1, right)
            else:
                # print(f"nums[mid] > target, mid: {mid}, right: {right}")
                return bin_search(left, mid)

        def find_pivot(left: int, right: int) -> int:
            mid = (right - left) // 2 + left
            # print(f"left: {left}, right: {right}, mid: {mid}")
            if left == right:
                # print(f"left == right, left: {left}, right: {right}")
                return left
            if nums[mid] > nums[mid + 1]:
                # print(f"nums[mid] > nums[mid + 1], mid: {mid}, right: {right}")
                return mid + 1
            if nums[mid] > nums[right]:
                # print(f"mid > nums[left], mid: {mid}, right: {right}")
                return find_pivot(mid, right)
            else:
                # print(f"mid < nums[left], mid: {mid}, right: {right}")
                return find_pivot(left, mid)

        if nums[0] < nums[-1]:
            # print(f"no pivot, nums[0]: {nums[0]}, nums[-1]: {nums[-1]}")
            return bin_search(0, len(nums) - 1)
        else:
            pivot = find_pivot(0, len(nums) - 1)
            # print(f"pivot: {pivot}")
            if target == nums[pivot]:
                # print(f"target == nums[pivot], pivot: {pivot}")
                return pivot
            if target > nums[-1]:
                # print(f"target > nums[-1], pivot: {pivot}")
                return bin_search(0, pivot)
            else:
                # print(f"target < nums[-1], pivot: {pivot}")
                return bin_search(pivot, len(nums) - 1)


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_01(self):
        nums = [0, 1, 2, 4, 5, 6, 7]
        target = 0
        expected_result = 0
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_02(self):
        nums = [4, 5, 6, 7, 8, 9, 10, 11]
        target = 3
        expected_result = -1
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_03(self):
        nums = [1]
        target = 0
        expected_result = -1
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_04(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 1
        expected_result = 5
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_05(self):
        nums = [1, 3, 5]
        target = 1
        expected_result = 0
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_06(self):
        nums = [3, 1]
        target = 1
        expected_result = 1
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_07(self):
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 1]
        target = 9
        expected_result = 7
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_08(self):
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 1]
        target = 1
        expected_result = 8
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_09(self):
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 1]
        target = 3
        expected_result = 1
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_10(self):
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 1]
        target = 2
        expected_result = 0
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_11(self):
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 1]
        target = 7
        expected_result = 5
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_12(self):
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 1]
        target = 8
        expected_result = 6
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_13(self):
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 1]
        target = 10
        expected_result = -1
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_14(self):
        nums = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8]
        target = 9
        expected_result = 0
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_15(self):
        nums = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8]
        target = 1
        expected_result = 11
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_16(self):
        nums = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8]
        target = 8
        expected_result = 18
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_17(self):
        nums = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8]
        target = 19
        expected_result = 10
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_18(self):
        nums = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8]
        target = 20
        expected_result = -1
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_19(self):
        nums = list(range(5000))
        target = 3477
        expected_result = 3477
        result = Solution().search(nums, target)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
