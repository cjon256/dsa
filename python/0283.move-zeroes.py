#  Category: algorithms
#  Level: Easy
#  Percent: 61.554993%
# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
# pylint: disable=invalid-name,line-too-long,too-few-public-methods,too-many-arguments


#  Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
#  Note that you must do this in-place without making a copy of the array.
#
#
#  Example 1:
#  Input: nums = [0,1,0,3,12]
#  Output: [1,3,12,0,0]
#  Example 2:
#  Input: nums = [0]
#  Output: [0]
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁴
#  	-2³¹ <= nums[i] <= 2³¹ - 1
#
#
#
#  Follow up: Could you minimize the total number of operations done?


import unittest
from typing import List


#  start_marker
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_zero = length = len(nums)
        curr = 0
        while curr < length:
            print(nums, curr, first_zero)
            if nums[curr] == 0:
                if first_zero == length:
                    first_zero = curr
            else:
                if first_zero < curr:
                    nums[first_zero], nums[curr] = nums[curr], nums[first_zero]
                    first_zero += 1
            curr += 1


#  end_marker
class OldSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        length = len(nums)
        zeros = 0
        while i < length:
            if nums[i] == 0:
                del nums[i]
                zeros += 1
                length -= 1
            else:
                i += 1
        for _ in range(zeros):
            nums.append(0)


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input_ = [0, 1, 0, 3, 12]
        output = [1, 3, 12, 0, 0]
        Solution().moveZeroes(input_)
        self.assertEqual(input_, output)

    def test_case_2(self):
        input_ = [0]
        output = [0]
        Solution().moveZeroes(input_)
        self.assertEqual(input_, output)

    def test_case_3(self):
        input_ = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        output = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Solution().moveZeroes(input_)
        self.assertEqual(input_, output)

    def test_case_4(self):
        input_ = [1, 2, 0, 4, 0, 6, 7, 8, 9, 0]
        output = [1, 2, 4, 6, 7, 8, 9, 0, 0, 0]
        Solution().moveZeroes(input_)
        self.assertEqual(input_, output)

    def test_case_5(self):
        input_ = [0, 0, 0, 1, 2, 3, 0, 0, 0, 0]
        output = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]
        Solution().moveZeroes(input_)
        self.assertEqual(input_, output)


if __name__ == "__main__":
    unittest.main()
