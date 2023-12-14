import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        self.assertEqual(Solution().search(nums, target), 4)

    def test_2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
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
