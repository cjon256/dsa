#  Category: algorithms
#  Level: Medium
#  Percent: 50.554733%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums, find the subarray with the largest sum, and return its sum.
#
#
#  Example 1:
#
#  Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#  Output: 6
#  Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#
#  Example 2:
#
#  Input: nums = [1]
#  Output: 1
#  Explanation: The subarray [1] has the largest sum 1.
#
#
#  Example 3:
#
#  Input: nums = [5,4,-1,7,8]
#  Output: 23
#  Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁵
#  	-10⁴ <= nums[i] <= 10⁴
#
#
#
#  Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


import unittest
from typing import List


#  start_marker
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_ = curr = nums[0]
        for n in nums[1:]:
            curr = max(curr + n, n)
            max_ = max(curr, max_)
        return max_


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_result = 6
        self.assertEqual(Solution().maxSubArray(nums), expected_result)

    def test_case_2(self):
        nums = [1]
        expected_result = 1
        self.assertEqual(Solution().maxSubArray(nums), expected_result)

    def test_case_3(self):
        nums = [5, 4, -1, 7, 8]
        expected_result = 23
        self.assertEqual(Solution().maxSubArray(nums), expected_result)

    def test_case_4(self):
        nums = []
        expected_result = 0
        self.assertEqual(Solution().maxSubArray(nums), expected_result)


if __name__ == "__main__":
    unittest.main()
