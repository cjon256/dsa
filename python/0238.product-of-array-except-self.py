#  Category: algorithms
#  Level: Medium
#  Percent: 65.23016%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#  You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
#  Example 1:
#  Input: nums = [1,2,3,4]
#  Output: [24,12,8,6]
#  Example 2:
#  Input: nums = [-1,1,0,-3,3]
#  Output: [0,0,9,0,0]
#
#
#  Constraints:
#
#
#  	2 <= nums.length <= 10⁵
#  	-30 <= nums[i] <= 30
#  	The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#
#
#  Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

import unittest
from typing import List


#  start_marker
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = [1 for _ in range(len(nums))]
        running_product = 1
        for i, n in enumerate(nums[:-1]):
            i = i + 1
            running_product *= n
            # print(f"{output_array=} {i=} {n=} {running_product=}")
            output_array[i] = running_product
        running_product = 1
        # print(f"left done {output_array}")
        for i, n in enumerate(nums[-1:0:-1]):
            i = len(nums) - i - 2
            running_product *= n
            # print(f"{output_array=} {i=} {n=} {running_product=}")
            output_array[i] *= running_product
        return output_array
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        result = Solution().productExceptSelf(nums)
        self.assertEqual(expected, result)

    def test_2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        result = Solution().productExceptSelf(nums)
        self.assertEqual(expected, result)

    def test_3(self):
        nums = [2, 3, 4, 5]
        expected = [60, 40, 30, 24]
        result = Solution().productExceptSelf(nums)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
