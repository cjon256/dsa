#  Category: algorithms
#  Level: Medium
#  Percent: 61.429386%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
#  We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
#  You must solve this problem without using the library's sort function.
#
#
#  Example 1:
#
#  Input: nums = [2,0,2,1,1,0]
#  Output: [0,0,1,1,2,2]
#
#
#  Example 2:
#
#  Input: nums = [2,0,1]
#  Output: [0,1,2]
#
#
#
#  Constraints:
#
#
#  	n == nums.length
#  	1 <= n <= 300
#  	nums[i] is either 0, 1, or 2.
#
#
#
#  Follow up: Could you come up with a one-pass algorithm using only constant extra space?


import unittest
from typing import List


#  start_marker
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        ones = 0
        twos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[ones], nums[i] = nums[i], nums[ones]
                nums[zero], nums[ones] = nums[ones], nums[zero]
                zero += 1
                ones += 1
                twos += 1
            elif nums[i] == 1:
                nums[ones], nums[i] = nums[i], nums[ones]
                ones += 1
                twos += 1
            else:
                nums[twos], nums[i] = nums[i], nums[twos]
                twos += 1
        if nums[-1] == 1:
            nums[-1], nums[ones - 1] = nums[ones - 1], nums[-1]

    #  end_marker

    def sortColors_sort(self, nums: List[int]) -> None:
        nums.sort()


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        expected = [0, 0, 1, 1, 2, 2]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)

    def test_case_2(self):
        nums = [2, 0, 1]
        expected = [0, 1, 2]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)

    def test_case_3(self):
        nums = [0]
        expected = [0]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)

    def test_case_4(self):
        nums = [1]
        expected = [1]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)

    def test_case_5(self):
        nums = [2]
        expected = [2]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)

    def test_case_6(self):
        nums = [2, 2, 2, 2, 2, 2]
        expected = [2, 2, 2, 2, 2, 2]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)

    def test_case_7(self):
        nums = [1, 1, 1, 1, 1, 1]
        expected = [1, 1, 1, 1, 1, 1]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)

    def test_case_8(self):
        nums = [0, 0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0, 0]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)

    def test_case_9(self):
        nums = [2, 1, 2, 1, 2, 1]
        expected = [1, 1, 1, 2, 2, 2]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)

    def test_case_10(self):
        nums = [2, 0, 2, 0, 0, 0]
        expected = [0, 0, 0, 0, 2, 2]
        Solution().sortColors_sort(nums)
        self.assertEqual(nums, expected)

    def test_case_11(self):
        nums = [1, 2, 2, 2, 2, 0, 0, 0, 1, 1]
        expected = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
