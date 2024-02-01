#  Category: algorithms
#  Level: Easy
#  Percent: 64.94763%
# pylint: enable=useless-suppression
# pylint: disable=line-too-long, missing-module-docstring, missing-function-docstring, missing-class-docstring
# pylint: disable=invalid-name, too-few-public-methods, consider-using-enumerate


#  Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#
#
#  Example 1:
#
#  Input: nums = [3,0,1]
#  Output: 2
#  Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
#
#
#  Example 2:
#
#  Input: nums = [0,1]
#  Output: 2
#  Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
#
#
#  Example 3:
#
#  Input: nums = [9,6,4,2,3,5,7,0,1]
#  Output: 8
#  Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
#
#
#
#  Constraints:
#
#
#  	n == nums.length
#  	1 <= n <= 10⁴
#  	0 <= nums[i] <= n
#  	All the numbers of nums are unique.
#
#
#
#  Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

import unittest
from typing import List, Optional


#  start_marker
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

    #  end_marker
    def missingNumber_pos(self, nums: List[int]) -> int:
        def find_first_positive_index(nums: List[int]) -> Optional[int]:
            for idx in range(len(nums)):
                if nums[idx] > 0:
                    return idx
            return None

        for idx in range(len(nums)):
            nums[idx] += 1
        for val in nums:
            idz = abs(val) - 1
            if idz < len(nums):
                nums[idz] = -abs(nums[idz])
        retval = find_first_positive_index(nums)
        if retval is None:
            return len(nums)
        return retval


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [3, 0, 1]
        expected_result = 2
        self.assertEqual(Solution().missingNumber(nums), expected_result)

    def test_case_2(self):
        nums = [0, 1]
        expected_result = 2
        self.assertEqual(Solution().missingNumber(nums), expected_result)

    def test_case_3(self):
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        expected_result = 8
        self.assertEqual(Solution().missingNumber(nums), expected_result)

    def test_case_4(self):
        nums = [0]
        expected_result = 1
        self.assertEqual(Solution().missingNumber(nums), expected_result)

    def test_case_5(self):
        nums = [2]
        expected_result = 0
        self.assertEqual(Solution().missingNumber(nums), expected_result)

    def test_case_6(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        expected_result = 10
        self.assertEqual(Solution().missingNumber(nums), expected_result)

    def test_case_7(self):
        nums = []
        expected_result = 0
        self.assertEqual(Solution().missingNumber(nums), expected_result)

    def test_case_8(self):
        nums = [2, 0]
        expected_result = 1
        self.assertEqual(Solution().missingNumber(nums), expected_result)


if __name__ == "__main__":
    unittest.main()
