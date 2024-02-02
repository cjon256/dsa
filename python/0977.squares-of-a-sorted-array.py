#  Category: algorithms
#  Level: Easy
#  Percent: 71.77093%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
#
#  Example 1:
#
#  Input: nums = [-4,-1,0,3,10]
#  Output: [0,1,9,16,100]
#  Explanation: After squaring, the array becomes [16,1,0,9,100].
#  After sorting, it becomes [0,1,9,16,100].
#
#
#  Example 2:
#
#  Input: nums = [-7,-3,2,3,11]
#  Output: [4,9,9,49,121]
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁴
#  	-10⁴ <= nums[i] <= 10⁴
#  	nums is sorted in non-decreasing order.
#
#
#
#  Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

import unittest
from typing import List


#  start_marker
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x * x for x in nums])


#  end_marker
class OldSolution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [x * x for x in sorted(nums, key=abs)]


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [-4, -1, 0, 3, 10]
        expected_result = [0, 1, 9, 16, 100]
        self.assertEqual(Solution().sortedSquares(nums), expected_result)

    def test_case_2(self):
        nums = [-7, -3, 2, 3, 11]
        expected_result = [4, 9, 9, 49, 121]
        self.assertEqual(Solution().sortedSquares(nums), expected_result)


if __name__ == "__main__":
    unittest.main()
