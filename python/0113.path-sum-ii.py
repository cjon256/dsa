#  Category: algorithms
#  Level: Medium
#  Percent: 58.096207%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring
#
#
#  Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
#
#  A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
#
#
#  Example 1:
#
#  Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
#  Output: [[5,4,11,2],[5,8,4,5]]
#  Explanation: There are two paths whose sum equals targetSum:
#  5 + 4 + 11 + 2 = 22
#  5 + 8 + 4 + 5 = 22
#
#
#  Example 2:
#
#  Input: root = [1,2,3], targetSum = 5
#  Output: []
#
#
#  Example 3:
#
#  Input: root = [1,2], targetSum = 0
#  Output: []
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [0, 5000].
#  	-1000 <= Node.val <= 1000
#  	-1000 <= targetSum <= 1000
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import unittest
from typing import List, Optional

from leetopenlib.tree import TreeNode, list_to_tree


#  start_marker
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res: List[List[int]] = []
        if not root:
            return res

        def recur(node: TreeNode, lis: List[int]) -> None:
            lis.append(node.val)
            if node.left is None and node.right is None:
                if sum(lis) == targetSum:
                    res.append(lis)
                return
            if node.left is not None:
                recur(node.left, lis.copy())
            if node.right is not None:
                recur(node.right, lis)

        recur(root, [])
        return res
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_0(self):
        root = list_to_tree([])
        targetSum = 0
        expected = []
        result = Solution().pathSum(root, targetSum)
        self.assertEqual(result, expected)

    def test_case_1(self):
        root = list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        targetSum = 22
        expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
        result = Solution().pathSum(root, targetSum)
        self.assertEqual(result, expected)

    def test_case_2(self):
        root = list_to_tree([1, 2, 3, None, None, None, None])
        targetSum = 5
        expected = []
        result = Solution().pathSum(root, targetSum)
        self.assertEqual(result, expected)

    def test_case_3(self):
        root = list_to_tree([1, 2, None])
        targetSum = 0
        expected = []
        result = Solution().pathSum(root, targetSum)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
