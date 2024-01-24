# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods
import unittest
from typing import List, Optional

#  Category: algorithms
#  Level: Hard
#  Percent: 37.618618%
#  Given an unsorted integer array nums, return the smallest missing positive integer.
#
#  You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#
#
#  Example 1:
#
#  Input: nums = [1,2,0]
#  Output: 3
#  Explanation: The numbers in the range [1,2] are all in the array.
#
#
#  Example 2:
#
#  Input: nums = [3,4,-1,1]
#  Output: 2
#  Explanation: 1 is in the array but 2 is missing.
#
#
#  Example 3:
#
#  Input: nums = [7,8,9,11,12]
#  Output: 1
#  Explanation: The smallest positive integer 1 is missing.
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁵
#  	-2³¹ <= nums[i] <= 2³¹ - 1
#


#  start_marker
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        def find_first_positive_index(lis: List[int]) -> Optional[int]:
            """Returns the index of the first positive value in the list"""
            for idx, val in enumerate(lis):
                if val > 0:
                    return idx
            return None

        def fix_nonpositives(lis: list[int], replacement: int) -> None:
            """Replaces all non-positive values with the replacement value"""
            for idx, val in enumerate(lis):
                if val <= 0:
                    lis[idx] = replacement

        first_pos_idx = find_first_positive_index(nums)
        if first_pos_idx is None:
            return 1
        fix_nonpositives(nums, nums[first_pos_idx])

        # if a value is present, make equivalent index negative
        for v in nums:
            abs_v_less_one = abs(v) - 1
            if abs_v_less_one < len(nums):
                nums[abs_v_less_one] = -abs(nums[abs_v_less_one])

        # then just find the first positive index and that plus one is the answer
        idx = find_first_positive_index(nums)
        if idx is None:
            # unless there is none
            return len(nums) + 1
        return idx + 1


#  end_marker
class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().firstMissingPositive([1, 2, 0]), 3)

    def test_2(self):
        self.assertEqual(Solution().firstMissingPositive([3, 4, -1, 1]), 2)

    def test_3(self):
        self.assertEqual(Solution().firstMissingPositive([7, 8, 9, 11, 12]), 1)

    def test_4(self):
        self.assertEqual(Solution().firstMissingPositive([1, 1]), 2)

    def test_5(self):
        self.assertEqual(Solution().firstMissingPositive([]), 1)

    def test_6(self):
        self.assertEqual(Solution().firstMissingPositive([-12, -23, -3, -2, -44]), 1)

    def test_7(self):
        self.assertEqual(Solution().firstMissingPositive([1, 2, 3]), 4)


if __name__ == "__main__":
    unittest.main()
