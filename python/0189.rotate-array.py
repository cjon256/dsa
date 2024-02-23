#  Category: algorithms
#  Level: Medium
#  Percent: 40.306744%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
#
#  Example 1:
#
#  Input: nums = [1,2,3,4,5,6,7], k = 3
#  Output: [5,6,7,1,2,3,4]
#  Explanation:
#  rotate 1 steps to the right: [7,1,2,3,4,5,6]
#  rotate 2 steps to the right: [6,7,1,2,3,4,5]
#  rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
#  Example 2:
#
#  Input: nums = [-1,-100,3,99], k = 2
#  Output: [3,99,-1,-100]
#  Explanation:
#  rotate 1 steps to the right: [99,-1,-100,3]
#  rotate 2 steps to the right: [3,99,-1,-100]
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁵
#  	-2³¹ <= nums[i] <= 2³¹ - 1
#  	0 <= k <= 10⁵
#
#
#
#  Follow up:
#
#
#  	Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
#  	Could you do it in-place with O(1) extra space?
#


import unittest
from typing import List


#  start_marker
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected_result = [5, 6, 7, 1, 2, 3, 4]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected_result)

    def test_case_2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        expected_result = [3, 99, -1, -100]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected_result)

    def test_case_3(self):
        nums = [1, 2]
        k = 3
        expected_result = [2, 1]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected_result)

    # single element
    def test_case_4(self):
        nums = [1]
        k = 0
        expected_result = [1]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected_result)

    # single element
    def test_case_5(self):
        nums = [1]
        k = 1
        expected_result = [1]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected_result)

    # single element
    def test_case_6(self):
        nums = [1]
        k = 2
        expected_result = [1]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected_result)

    # single element
    def test_case_7(self):
        nums = [1]
        k = 3
        expected_result = [1]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected_result)

    # k equal to length
    def test_case_8(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 7
        expected_result = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected_result)

    # k more than length
    def test_case_9(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 8
        expected_result = [7, 1, 2, 3, 4, 5, 6]
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected_result)


if __name__ == "__main__":
    unittest.main()
