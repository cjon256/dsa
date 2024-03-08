#  Category: algorithms
#  Level: Hard
#  Percent: 62.3%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
#
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
#
#
#
# Example 1:
#
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
#
# Example 2:
#
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
#
#
#
# Constraints:
#
#     nums.length == k
#     1 <= k <= 3500
#     1 <= nums[i].length <= 50
#     -105 <= nums[i][j] <= 105
#     nums[i] is sorted in non-decreasing order.
#

import unittest
from typing import List


#  start_marker
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
