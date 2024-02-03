#  Category: algorithms
#  Level: Easy
#  Percent: 51.64373%
# pylint: enable=useless-suppression
# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring
# pylint: disable=invalid-name, line-too-long, too-few-public-methods


#  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
#  You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
#  You can return the answer in any order.
#
#
#  Example 1:
#
#  Input: nums = [2,7,11,15], target = 9
#  Output: [0,1]
#  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
#  Example 2:
#
#  Input: nums = [3,2,4], target = 6
#  Output: [1,2]
#
#
#  Example 3:
#
#  Input: nums = [3,3], target = 6
#  Output: [0,1]
#
#
#
#  Constraints:
#
#
#  	2 <= nums.length <= 10⁴
#  	-10⁹ <= nums[i] <= 10⁹
#  	-10⁹ <= target <= 10⁹
#  	Only one valid answer exists.
#
#
#
#  Follow-up: Can you come up with an algorithm that is less than O(n²) time complexity?
import unittest
#  start_marker
from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx: Dict[int, int] = {}

        for idx, n in enumerate(nums):
            difference = target - n
            if difference in num_to_idx:
                return [num_to_idx[difference], idx]
            num_to_idx[n] = idx
        return []


#  end_marker


class TestSolution(unittest.TestCase):
    def test_example(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertListEqual(Solution().twoSum(nums, target), expected)

    def test_example2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertListEqual(Solution().twoSum(nums, target), expected)

    def test_example3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertListEqual(Solution().twoSum(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
