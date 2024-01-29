# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods, line-too-long

#  Category: algorithms
#  Level: Easy
#  Percent: 58.635796%


#  Given the root of a binary tree, return the length of the diameter of the tree.
#
#  The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
#  The length of a path between two nodes is represented by the number of edges between them.
#
#
#  Example 1:
#
#  Input: root = [1,2,3,4,5]
#  Output: 3
#  Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#
#
#  Example 2:
#
#  Input: root = [1,2]
#  Output: 1
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [1, 10⁴].
#  	-100 <= Node.val <= 100
#

import unittest
from dataclasses import dataclass
from typing import Optional

from conversions import liststr_to_tree


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]


#  start_marker
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recurse_max_heights(node: Optional[TreeNode]) -> int:
            if not node:
                return 0, 0
            left_height, left_max_diameter = recurse_max_heights(node.left)
            right_height, right_max_diameter = recurse_max_heights(node.right)
            max_depth = max(left_height, right_height) + 1
            max_diameter_at_node = max(
                left_max_diameter, right_max_diameter, left_height + right_height
            )
            return (max_depth, max_diameter_at_node)

        _, max_diameter = recurse_max_heights(root)
        return max_diameter


#  end_marker


class TestSolution(unittest.TestCase):
    def test_case_0(self):
        sol = Solution()
        root = liststr_to_tree("[]")
        expected = 0
        self.assertEqual(sol.diameterOfBinaryTree(root), expected)

    def test_case_1(self):
        sol = Solution()
        root = liststr_to_tree("[1, 2, 3, 4, 5]")
        expected = 3
        self.assertEqual(sol.diameterOfBinaryTree(root), expected)

    def test_case_2(self):
        sol = Solution()
        root = liststr_to_tree("[1, 2]")
        expected = 1
        self.assertEqual(sol.diameterOfBinaryTree(root), expected)

    def test_case_3(self):
        sol = Solution()
        root = liststr_to_tree("[1]")
        expected = 0
        self.assertEqual(sol.diameterOfBinaryTree(root), expected)


if __name__ == "__main__":
    unittest.main()
