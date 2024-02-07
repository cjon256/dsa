#  Category: algorithms
#  Level: Easy
#  Percent: 61.33056%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
#
#  Example 1:
#  Input: nums = [1,2,3,1]
#  Output: true
#  Example 2:
#  Input: nums = [1,2,3,4]
#  Output: false
#  Example 3:
#  Input: nums = [1,1,1,3,3,4,3,2,4,2]
#  Output: true
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁵
#  	-10⁹ <= nums[i] <= 10⁹
#

import unittest
from typing import List


#  start_marker
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 1]
        expected_result = True
        self.assertEqual(Solution().containsDuplicate(nums), expected_result)

    def test_case_2(self):
        nums = [1, 2, 3, 4]
        expected_result = False
        self.assertEqual(Solution().containsDuplicate(nums), expected_result)

    def test_case_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected_result = True
        self.assertEqual(Solution().containsDuplicate(nums), expected_result)


if __name__ == "__main__":
    unittest.main()
