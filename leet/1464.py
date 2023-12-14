from typing import List
import unittest


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        second = 0
        for n in nums:
            if n > second:
                if n > largest:
                    second = largest
                    largest = n
                else:
                    second = n
        return (largest - 1) * (second - 1)


"""
Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
"""


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().maxProduct([3, 4, 5, 2]), 12)

    def test2(self):
        self.assertEqual(Solution().maxProduct([1, 5, 4, 5]), 16)

    def test3(self):
        self.assertEqual(Solution().maxProduct([3, 7]), 12)


if __name__ == "__main__":
    unittest.main()
