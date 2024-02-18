#  Category: algorithms
#  Level: Medium
#  Percent: 50.772552%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are a professional robber planning to rob houses along a street. Each
#  house has a certain amount of money stashed, the only constraint stopping
#  you from robbing each of them is that adjacent houses have security systems
#  connected and it will automatically contact the police if two adjacent
#  houses were broken into on the same night.
#
#  Given an integer array nums representing the amount of money of each house,
#  return the maximum amount of money you can rob tonight without alerting the
#  police.
#
#
#  Example 1:
#
#  Input: nums = [1,2,3,1]
#  Output: 4
#  Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#  Total amount you can rob = 1 + 3 = 4.
#
#
#  Example 2:
#
#  Input: nums = [2,7,9,3,1]
#  Output: 12
#  Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#  Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 100
#  	0 <= nums[i] <= 400
#


import unittest

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List


#  start_marker
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # make an array that takes into account
        # the costs as well as the benefits of
        # robbing the current house at index i
        values = [nums[0]]
        for i, val in enumerate(nums[1:]):
            values.append(max(val, values[i - 1]))

        # then do a typical two-pointer approach
        # with max values (poor man's dp, basically)
        first_max = nums[0]
        alter_max = nums[1]
        for i, val in enumerate(nums[2:]):
            alter_max = max(alter_max, first_max)
            first_max, alter_max = alter_max, first_max + val

        return max(first_max, alter_max)
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 1]
        expected = 4
        result = Solution().rob(nums)
        self.assertEqual(result, expected)

    def test_case_2(self):
        nums = [2, 7, 9, 3, 1]
        expected = 12
        result = Solution().rob(nums)
        self.assertEqual(result, expected)

    def test_case_3(self):
        nums = [2, 1, 1, 2]
        expected = 4
        result = Solution().rob(nums)
        self.assertEqual(result, expected)

    def test_case_4(self):
        nums = [1, 3, 1, 3, 100]
        expected = 103
        result = Solution().rob(nums)
        self.assertEqual(result, expected)

    def test_case_5(self):
        nums = [1, 300, 1, 3, 100, 1]
        expected = 400
        result = Solution().rob(nums)
        self.assertEqual(result, expected)

    def test_case_6(self):
        nums = [1, 300, 1, 3, 1, 3, 100, 1, 1]
        expected = 404
        result = Solution().rob(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
