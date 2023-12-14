from typing import List
import unittest
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for k in c:
            if c[k] % 2 == 1:
                return False
        return True


"""
Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

"""


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().divideArray([3, 2, 3, 2, 2, 2]), True)

    def test2(self):
        self.assertEqual(Solution().divideArray([1, 2, 3, 4]), False)


if __name__ == '__main__':
    unittest.main()
