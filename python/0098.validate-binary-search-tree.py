#  Category: algorithms
#  Level: Medium
#  Percent: 32.660217%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
#  A valid BST is defined as follows:
#
#
#  	The left subtree of a node contains only nodes with keys less than the node's key.
#  	The right subtree of a node contains only nodes with keys greater than the node's key.
#  	Both the left and right subtrees must also be binary search trees.
#
#
#
#  Example 1:
#
#  Input: root = [2,1,3]
#  Output: true
#
#
#  Example 2:
#
#  Input: root = [5,1,4,null,null,3,6]
#  Output: false
#  Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [1, 10⁴].
#  	-2³¹ <= Node.val <= 2³¹ - 1
#

import unittest
from typing import Optional

from leetopenlib.tree import TreeNode, list_to_tree


#  start_marker
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        MIN = -(2**32)
        MAX = 2**32

        def valid_r(root, min_val=MIN, max_val=MAX):
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return valid_r(root.left, min_val, root.val) and valid_r(
                root.right, root.val, max_val
            )

        return valid_r(root)


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = list_to_tree([2, 1, 3])
        expected = True
        self.assertEqual(Solution().isValidBST(root), expected)

    def test_case_2(self):
        root = list_to_tree([5, 1, 4, None, None, 3, 6])
        expected = False
        self.assertEqual(Solution().isValidBST(root), expected)

    def test_case_3(self):
        root = list_to_tree([5, 4, 6, None, None, 3, 7])
        expected = False
        self.assertEqual(Solution().isValidBST(root), expected)

    def test_case_4(self):
        root = list_to_tree([-2147483648])
        expected = True
        self.assertEqual(Solution().isValidBST(root), expected)


if __name__ == "__main__":
    unittest.main()
