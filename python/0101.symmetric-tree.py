#  Category: algorithms
#  Level: Easy
#  Percent: 55.941277%
# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
# pylint: disable=invalid-name,line-too-long,too-few-public-methods,too-many-arguments


#  Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
#
#  Example 1:
#
#  Input: root = [1,2,2,3,4,4,3]
#  Output: true
#
#
#  Example 2:
#
#  Input: root = [1,2,2,null,3,null,3]
#  Output: false
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [1, 1000].
#  	-100 <= Node.val <= 100
#
#
#
#  Follow up: Could you solve it both recursively and iteratively?


import unittest
from typing import Optional

from conversions import TreeNode, liststr_to_tree


#  start_marker
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            mirrorLR = is_mirror(left.left, right.right)
            mirrorRL = is_mirror(left.right, right.left)
            return mirrorLR and mirrorRL

        if root is None:
            return True
        return is_mirror(root.left, root.right)


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = liststr_to_tree("[1,2,2,3,4,4,3]")
        self.assertEqual(Solution().isSymmetric(root), True)

    def test_case_2(self):
        root = liststr_to_tree("[1,2,2,null,3,null,3]")
        self.assertEqual(Solution().isSymmetric(root), False)

    def test_case_3(self):
        root = liststr_to_tree("[]")
        self.assertEqual(Solution().isSymmetric(root), True)


if __name__ == "__main__":
    unittest.main()
