#  Category: algorithms
#  Level: Medium
#  Percent: 34.052654%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#  Notice that the solution set must not contain duplicate triplets.
#
#
#  Example 1:
#
#  Input: nums = [-1,0,1,2,-1,-4]
#  Output: [[-1,-1,2],[-1,0,1]]
#  Explanation:
#  nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#  nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#  nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#  The distinct triplets are [-1,0,1] and [-1,-1,2].
#  Notice that the order of the output and the order of the triplets does not matter.
#
#
#  Example 2:
#
#  Input: nums = [0,1,1]
#  Output: []
#  Explanation: The only possible triplet does not sum up to 0.
#
#
#  Example 3:
#
#  Input: nums = [0,0,0]
#  Output: [[0,0,0]]
#  Explanation: The only possible triplet sums up to 0.
#
#
#
#  Constraints:
#
#
#  	3 <= nums.length <= 3000
#  	-10⁵ <= nums[i] <= 10⁵
#

import unittest

#  start_marker
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        triplets = []
        nums.sort()
        seen = set()
        i = 0
        while nums[i] <= 0 and i < len(nums) - 2:
            a = nums[i]
            if a in seen:
                i += 1
                continue
            seen.add(a)
            left = i + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                if a + b + c == 0:
                    triplet = [a, b, c]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    left += 1
                    right -= 1
                elif a + b + c < 0:
                    left += 1
                else:
                    right -= 1
            i += 1
        return triplets
        #  end_marker


def order_independent_comparison_of_lists_of_lists(a, b):
    sa = sorted([sorted(x) for x in a])
    sb = sorted([sorted(x) for x in b])
    return sa == sb


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_2(self):
        nums = [0, 1, 1]
        expected = []
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_3(self):
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_4(self):
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_5(self):
        nums = [0, 0, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_6(self):
        nums = [0, 0, 0, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_7(self):
        nums = [0, -3, 0, 1, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_8(self):
        nums = [-2, -3, 0, 1, 2, -1, 3]
        expected = [[-3, 1, 2], [-2, 0, 2], [-2, -1, 3], [-3, 0, 3], [-1, 0, 1]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )


if __name__ == "__main__":
    unittest.main()
