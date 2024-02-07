#  Category: algorithms
#  Level: Easy
#  Percent: 76.47033%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the root of a binary tree, invert the tree, and return its root.
#
#
#  Example 1:
#
#  Input: root = [4,2,7,1,3,6,9]
#  Output: [4,7,2,9,6,3,1]
#
#
#  Example 2:
#
#  Input: root = [2,1,3]
#  Output: [2,3,1]
#
#
#  Example 3:
#
#  Input: root = []
#  Output: []
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [0, 100].
#  	-100 <= Node.val <= 100
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import unittest
from typing import Optional

from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list


#  start_marker
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left
            )
        return root


#  end_marker
class TestSolution(unittest.TestCase):
    def test_invertTree_1(self):
        root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
        expected = [4, 7, 2, 9, 6, 3, 1]
        result = Solution().invertTree(root)
        self.assertEqual(tree_to_list(result), expected)

    def test_invertTree_2(self):
        root = list_to_tree([2, 1, 3])
        expected = [2, 3, 1]
        result = Solution().invertTree(root)
        self.assertEqual(tree_to_list(result), expected)

    def test_invertTree_3(self):
        root = list_to_tree([])
        expected = []
        result = Solution().invertTree(root)
        self.assertEqual(tree_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
