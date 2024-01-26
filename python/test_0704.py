import unittest
from typing import List


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


if __name__ == '__main__':
    unittest.main()


"""
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
