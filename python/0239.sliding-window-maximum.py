#  Category: algorithms
#  Level: Hard
#  Percent: 46.5%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the max sliding window.
#
#
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
#
# Constraints:
#
#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     1 <= k <= nums.length
#

import unittest
from typing import List


#  start_marker
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass

        #  end_marker

    def maxSlidingWindow_TLE(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(1 + len(nums) - k):
            res.append(max(nums[i : i + k]))
        return res


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected_result = [3, 3, 5, 5, 6, 7]
        result = Solution().maxSlidingWindow(nums, k)
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        nums = [1]
        k = 1
        expected_result = [1]
        result = Solution().maxSlidingWindow(nums, k)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
