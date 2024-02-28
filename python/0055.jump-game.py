#  Category: algorithms
#  Level: Medium
#  Percent: 38.529556%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
#
#  Return true if you can reach the last index, or false otherwise.
#
#
#  Example 1:
#
#  Input: nums = [2,3,1,1,4]
#  Output: true
#  Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
#  Example 2:
#
#  Input: nums = [3,2,1,0,4]
#  Output: false
#  Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁴
#  	0 <= nums[i] <= 10⁵
#


import unittest

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List


#  start_marker
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = max_reach = 0
        while True:
            max_reach = max(curr + nums[curr], max_reach)
            if max_reach >= len(nums) - 1:
                return True
            curr += 1
            if curr > max_reach:
                return False

    def canJump_initial_try(self, nums: List[int]) -> bool:

        reachable = [False] * len(nums)
        reachable[0] = True
        for i, n in enumerate(nums):
            if not reachable[i]:
                continue
            for j in range(n):
                idx = i + j + 1
                if idx < len(reachable):
                    reachable[idx] = True
            if reachable[-1]:
                return True
        return reachable[-1]


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 3, 1, 1, 4]
        expected_result = True
        result = Solution().canJump(nums)
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        nums = [3, 2, 1, 0, 4]
        expected_result = False
        result = Solution().canJump(nums)
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        nums = [0]
        expected_result = True
        result = Solution().canJump(nums)
        self.assertEqual(result, expected_result)

    def test_case_4(self):
        nums = [2, 0, 0]
        expected_result = True
        result = Solution().canJump(nums)
        self.assertEqual(result, expected_result)

    def test_case_5(self):
        nums = [2, 0]
        expected_result = True
        result = Solution().canJump(nums)
        self.assertEqual(result, expected_result)

    def test_case_6(self):
        nums = [1, 1, 1, 1, 1]
        expected_result = True
        result = Solution().canJump(nums)
        self.assertEqual(result, expected_result)

    def test_case_7(self):
        nums = [3, 2, 1, 0, 1, 4]
        expected_result = False
        result = Solution().canJump(nums)
        self.assertEqual(result, expected_result)

    def test_case_8(self):
        nums = [10, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        expected_result = True
        result = Solution().canJump(nums)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
