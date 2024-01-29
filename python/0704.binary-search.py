#  Category: algorithms
#  Level: Easy
#  Percent: 57.053288%


#  Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
#  You must write an algorithm with O(log n) runtime complexity.
#
#
#  Example 1:
#
#  Input: nums = [-1,0,3,5,9,12], target = 9
#  Output: 4
#  Explanation: 9 exists in nums and its index is 4
#
#
#  Example 2:
#
#  Input: nums = [-1,0,3,5,9,12], target = 2
#  Output: -1
#  Explanation: 2 does not exist in nums so return -1
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁴
#  	-10⁴ < nums[i], target < 10⁴
#  	All the integers in nums are unique.
#  	nums is sorted in ascending order.
#
import unittest
from typing import List


#  start_marker
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        while start < end:
            midpoint = (start + end) // 2
            if target == nums[midpoint]:
                return midpoint
            if target > nums[midpoint]:
                start = midpoint + 1
            else:
                end = midpoint
        return -1


#  end_marker


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        self.assertEqual(Solution().search(nums, target), 4)

    def test_2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        self.assertEqual(Solution().search(nums, target), -1)

    def test_3(self):
        nums = [5]
        target = 5
        self.assertEqual(Solution().search(nums, target), 0)

    def test_4(self):
        nums = [5]
        target = -5
        self.assertEqual(Solution().search(nums, target), -1)

    def test_5(self):
        nums = []
        target = 0
        self.assertEqual(Solution().search(nums, target), -1)


if __name__ == "__main__":
    unittest.main()
