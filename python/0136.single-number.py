#  Category: algorithms
#  Level: Easy
#  Percent: 72.217445%


#  Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
#  You must implement a solution with a linear runtime complexity and use only constant extra space.
#
#
#  Example 1:
#  Input: nums = [2,2,1]
#  Output: 1
#  Example 2:
#  Input: nums = [4,1,2,1,2]
#  Output: 4
#  Example 3:
#  Input: nums = [1]
#  Output: 1
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 3 * 10⁴
#  	-3 * 10⁴ <= nums[i] <= 3 * 10⁴
#  	Each element in the array appears twice except for one element which appears only once.
#


import unittest
from typing import List


#  start_marker
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input = [2, 2, 1]
        expected_output = 1
        result = Solution().singleNumber(input)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        input = [4, 1, 2, 1, 2]
        expected_output = 4
        result = Solution().singleNumber(input)
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        input = [1]
        expected_output = 1
        result = Solution().singleNumber(input)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
