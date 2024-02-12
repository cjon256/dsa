#  Category: algorithms
#  Level: Medium
#  Percent: 77.8535%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#
#  Example 1:
#  Input: nums = [1,2,3]
#  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  Example 2:
#  Input: nums = [0,1]
#  Output: [[0,1],[1,0]]
#  Example 3:
#  Input: nums = [1]
#  Output: [[1]]
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 6
#  	-10 <= nums[i] <= 10
#  	All the integers of nums are unique.
#


import unittest
from itertools import permutations
from typing import List


def compare_permutations(l1, l2):
    if len(l1) != len(l2):
        return False
    for a in l1:
        if a not in l2:
            return False
    return True


#  start_marker
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[nums[0]]]
        for i in range(1, len(nums)):
            new_perms = []
            for old in perms:
                for pos in range(len(old) + 1):
                    new_perms.append(old[:pos] + [nums[i]] + old[pos:])
            perms = new_perms
        return perms

    #  end_marker
    def permute_easy(self, nums: List[int]) -> List[List[int]]:
        # the obvious solution
        return [list(perm) for perm in permutations(nums)]


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        result = Solution().permute(nums)
        self.assertTrue(compare_permutations(result, expected))

    def test_case_2(self):
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        result = Solution().permute(nums)
        self.assertTrue(compare_permutations(result, expected))

    def test_case_3(self):
        nums = [1]
        expected = [[1]]
        result = Solution().permute(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
