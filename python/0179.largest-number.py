#  Category: algorithms
#  Level: Medium
#  Percent: 35.9%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.
#
#
#
# Example 1:
#
# Input: nums = [10,2]
# Output: "210"
#
# Example 2:
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
#
# Constraints:
#
#     1 <= nums.length <= 100
#     0 <= nums[i] <= 109
#

import unittest
from typing import List


#  start_marker
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
