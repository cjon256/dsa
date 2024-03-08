#  Category: algorithms
#  Level: Easy
#  Percent: 45.5%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
#
#
# Constraints:
#
#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums contains distinct values sorted in ascending order.
#     -104 <= target <= 104
#

import unittest
from typing import List


#  start_marker
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected_result = 2
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        nums = [1, 3, 5, 6]
        target = 2
        expected_result = 1
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        nums = [1, 3, 5, 6]
        target = 7
        expected_result = 4
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_4(self):
        nums = [1, 3, 5, 6]
        target = 0
        expected_result = 0
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_5(self):
        nums = [1]
        target = 0
        expected_result = 0
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_6(self):
        nums = [1, 3]
        target = 2
        expected_result = 1
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_7(self):
        nums = [1, 3, 5]
        target = 4
        expected_result = 2
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_8(self):
        nums = [1, 3, 5]
        target = 6
        expected_result = 3
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_case_9(self):
        nums = [1, 3, 5]
        target = 0
        expected_result = 0
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
