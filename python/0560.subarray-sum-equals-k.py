#  Category: algorithms
#  Level: Medium
#  Percent: 43.4%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
#
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
#
# Constraints:
#
#     1 <= nums.length <= 2 * 104
#     -1000 <= nums[i] <= 1000
#     -107 <= k <= 107
#

import unittest
from typing import List


#  start_marker
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
