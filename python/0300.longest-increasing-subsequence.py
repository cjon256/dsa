#  Category: algorithms
#  Level: Medium
#  Percent: 54.87034%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
#
#  Example 1:
#
#  Input: nums = [10,9,2,5,3,7,101,18]
#  Output: 4
#  Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
#
#  Example 2:
#
#  Input: nums = [0,1,0,3,2,3]
#  Output: 4
#
#
#  Example 3:
#
#  Input: nums = [7,7,7,7,7,7,7]
#  Output: 1
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 2500
#  	-10⁴ <= nums[i] <= 10⁴
#
#
#
#  Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


import unittest
from bisect import bisect_left
from typing import List


#  start_marker
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack: List[int] = [nums[0]]

        def push_mono(n: int) -> None:
            if n > stack[-1]:
                stack.append(n)
                print(stack)
                return
            index = len(stack) - 1
            while index > 0 and n <= stack[index - 1]:
                index -= 1
            stack[index] = n
            print(f"stack: {stack}")
            return

        for n in nums[1:]:
            push_mono(n)
        return len(stack)
        #  end_marker

    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        """short and sweet DP, not mine though"""
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS_bisect(self, nums: List[int]) -> int:
        """this one is really neat, not mine though"""
        lst: List[int] = []
        for num in nums:
            i = bisect_left(lst, num)

            if i == len(lst):
                lst.append(num)

            else:
                lst[i] = num

        return len(lst)


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        expected = 4
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        expected = 1
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_4(self):
        nums = [1, 7, 8, 2, 9, 10]
        expected = 5
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_5(self):
        nums = [1, 7, 8, 2, 3, 4]
        expected = 4
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_6(self):
        nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
        expected = 6
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_7(self):
        nums = [1]
        expected = 1
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_8(self):
        nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
        expected = 6
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_9(self):
        # fmt: off
        nums = [-813,82,-728,-82,-432,887,-551,324,-315,306,-164,-499,-873,-613,932,177,61,52,1000,-710,372,-306,-584,-332,-500,407,399,-648,290,-866,222,562,993,-338,-590,303,-16,-134,226,-648,909,582,177,899,-343,55,629,248,333,1,-921,143,629,981,-435,681,844,349,613,457,797,695,485,15,710,-450,-775,961,-445,-905,466,942,995,-289,-397,434,-14,34,-903,314,862,-441,507,-966,525,624,-706,39,152,536,874,-364,747,-35,446,-608,-554,-411,987,-354,-700,-34,395,-977,544,-330,596,335,-612,28,586,228,-664,-841,-999,-100,-620,718,489,346,450,772,941,952,-560,58,999,-879,396,-101,897,-1000,-566,-296,-555,938,941,475,-260,-52,193,379,866,226,-611,-177,507,910,-594,-856,156,71,-946,-660,-716,-295,-927,148,620,201,706,570,-659,174,637,-293,736,-735,377,-687,-962,768,430,576,160,577,-329,175,51,699,-113,950,-364,383,5,748,-250,-644,-576,-227,603,832,-483,-237,235,893,-336,452,-526,372,-418,356,325,-180,134,-698]
        # nums = [n for n in range(0, 25)]
        # fmt: on
        expected = 25
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_10(self):
        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = 1
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
