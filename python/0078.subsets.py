#  Category: algorithms
#  Level: Medium
#  Percent: 76.905334%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums of unique elements, return all possible subsets (the power set).
#
#  The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
#  Example 1:
#
#  Input: nums = [1,2,3]
#  Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
#  Example 2:
#
#  Input: nums = [0]
#  Output: [[],[0]]
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10
#  	-10 <= nums[i] <= 10
#  	All the numbers of nums are unique.
#


import unittest
from typing import List


#  start_marker
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _combs(lis, length):
            if length == 0:
                return [[]]
            if length == 1:
                return [[i] for i in lis]
            res = []
            for i in range(len(lis)):
                for j in _combs(lis[i + 1 :], length - 1):
                    res.append([lis[i]] + j)
            return res

        res: List[List[int]] = [[]]
        for i in range(1, len(nums) + 1):
            res.extend(_combs(nums, i))
        return res
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3]
        ans = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertCountEqual(Solution().subsets(nums), ans)

    def test_case_2(self):
        nums = [0]
        ans = [[], [0]]
        self.assertCountEqual(Solution().subsets(nums), ans)

    def test_case_3(self):
        nums = [1, 2, 3, 4]
        # fmt: off
        ans = [ [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4],
                [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4], ]
        self.assertCountEqual(Solution().subsets(nums), ans)

    def test_case_4(self):
        nums = [1, 2]
        ans = [[], [1], [2], [1, 2]]
        self.assertCountEqual(Solution().subsets(nums), ans)


if __name__ == "__main__":
    unittest.main()
