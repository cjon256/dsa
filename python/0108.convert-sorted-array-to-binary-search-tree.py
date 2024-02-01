#  Category: algorithms
#  Level: Easy
#  Percent: 71.23578%
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable= missing-class-docstring, missing-function-docstring, missing-module-docstring

#  Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
#
#
#  Example 1:
#
#  Input: nums = [-10,-3,0,5,9]
#  Output: [0,-3,9,-10,null,5]
#  Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
#
#
#  Example 2:
#
#  Input: nums = [1,3]
#  Output: [3,1]
#  Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁴
#  	-10⁴ <= nums[i] <= 10⁴
#  	nums is sorted in a strictly increasing order.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import unittest
from typing import List, Optional

from conversions import TreeNode, tree_to_liststr


#  start_marker
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def split_and_insert(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = split_and_insert(nums[:mid])
            root.right = split_and_insert(nums[mid + 1 :])
            return root

        return split_and_insert(nums)


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [-10, -3, 0, 5, 9]
        expected_result1 = "[0,-3,9,-10,null,5]"
        expected_result2 = "[0,-10,5,null,-3,null,9]"
        self.assertIn(
            tree_to_liststr(Solution().sortedArrayToBST(nums)),
            [expected_result1, expected_result2],
        )

    def test_case_2(self):
        nums = [1, 3]
        expected_result1 = "[3,1]"
        expected_result2 = "[1,null,3]"
        self.assertIn(
            tree_to_liststr(Solution().sortedArrayToBST(nums)),
            [expected_result1, expected_result2],
        )

    def test_case_3(self):
        nums = []
        expected_result = "[]"
        self.assertEqual(
            tree_to_liststr(Solution().sortedArrayToBST(nums)), expected_result
        )

    def test_case_4(self):
        nums = [1]
        expected_result = "[1]"
        self.assertEqual(
            tree_to_liststr(Solution().sortedArrayToBST(nums)), expected_result
        )

    def test_case_5(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        expected_result = "[4,2,6,1,3,5,7]"
        self.assertEqual(
            tree_to_liststr(Solution().sortedArrayToBST(nums)), expected_result
        )


if __name__ == "__main__":
    unittest.main()
