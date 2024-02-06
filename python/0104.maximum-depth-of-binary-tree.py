#  Category: algorithms
#  Level: Easy
#  Percent: 74.931244%
# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods
import unittest
from typing import Optional, Self

from leetopenlib.tree import TreeNode, liststr_to_tree

#  Given the root of a binary tree, return its maximum depth.
#
#  A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
#
#  Example 1:
#
#  Input: root = [3,9,20,null,null,15,7]
#  Output: 3
#
#
#  Example 2:
#
#  Input: root = [1,null,2]
#  Output: 2
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [0, 10⁴].
#  	-100 <= Node.val <= 100
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#  start_marker
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth_r(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(depth_r(node.left), depth_r(node.right)) + 1

        return depth_r(root)


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = liststr_to_tree("[3,9,20,null,null,15,7]")
        self.assertEqual(Solution().maxDepth(root), 3)

    def test_case_2(self):
        root = liststr_to_tree("[1,null,2]")
        self.assertEqual(Solution().maxDepth(root), 2)

    def test_case_3(self):
        root = liststr_to_tree("[]")
        self.assertEqual(Solution().maxDepth(root), 0)

    def test_case_4(self):
        root = liststr_to_tree("[0]")
        self.assertEqual(Solution().maxDepth(root), 1)

    def test_case_5(self):
        root = None
        self.assertEqual(Solution().maxDepth(root), 0)


if __name__ == "__main__":
    unittest.main()
