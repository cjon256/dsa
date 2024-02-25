#  Category: algorithms
#  Level: Medium
#  Percent: 66.79542%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums and an integer k, return the kth largest element in the array.
#
#  Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
#  Can you solve it without sorting?
#
#
#  Example 1:
#  Input: nums = [3,2,1,5,6,4], k = 2
#  Output: 5
#  Example 2:
#  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#  Output: 4
#
#
#  Constraints:
#
#
#  	1 <= k <= nums.length <= 10⁵
#  	-10⁴ <= nums[i] <= 10⁴
#

import unittest
from typing import List

DUMMY = None
#  start_marker
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: List[int] = []
        for n in nums[:k]:
            heapq.heappush(heap, n)
        for n in nums[k:]:
            heapq.heappushpop(heap, n)
        return heapq.heappop(heap)

        #  end_marker

    def findKthLargest_sorted(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_case_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        result = self.s.findKthLargest(nums, k)
        self.assertEqual(result, 5)

    def test_case_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        result = self.s.findKthLargest(nums, k)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
