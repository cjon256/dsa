#  Category: algorithms
#  Level: Medium
#  Percent: 42.882057%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the root of a binary tree, return the maximum width of the given tree.
#
#  The maximum width of a tree is the maximum width among all levels.
#
#  The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
#
#  It is guaranteed that the answer will in the range of a 32-bit signed integer.
#
#
#  Example 1:
#
#  Input: root = [1,3,2,5,3,null,9]
#  Output: 4
#  Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
#
#
#  Example 2:
#
#  Input: root = [1,3,2,5,null,null,9,6,null,7]
#  Output: 7
#  Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
#
#
#  Example 3:
#
#  Input: root = [1,3,2,5]
#  Output: 2
#  Explanation: The maximum width exists in the second level with length 2 (3,2).
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [1, 3000].
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

from leetopenlib.tree import TreeNode, list_to_tree


#  start_marker
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_table: list[int] = []
        min_table: list[int] = []

        def recur(node: TreeNode, lvl: int, n: int) -> None:
            if len(max_table) <= lvl:
                max_table.append(n)
                min_table.append(n)
            else:
                max_table[lvl] = max(max_table[lvl], n)
                min_table[lvl] = min(min_table[lvl], n)
            recur(node.left, lvl + 1, 2 * n - 1) if node.left else []
            recur(node.right, lvl + 1, 2 * n) if node.right else []

        recur(root, 0, 1)
        return max(map(lambda n: n[1] - n[0] + 1, zip(min_table, max_table)))
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = list_to_tree([1, 3, 2, 5, 3, None, 9])
        expected = 4
        result = Solution().widthOfBinaryTree(root)
        self.assertEqual(expected, result)

    def test_case_2(self):
        root = list_to_tree([1, 3, 2, 5, None, None, 9, 6, None, 7, None])
        expected = 7
        result = Solution().widthOfBinaryTree(root)
        self.assertEqual(expected, result)

    def test_case_3(self):
        root = list_to_tree([1, 3, 2, 5, None])
        expected = 2
        result = Solution().widthOfBinaryTree(root)
        self.assertEqual(expected, result)

    def test_case_4(self):
        root = list_to_tree([1, 3, 2, 5, 3, None, 9, 6, None, None, 7, None, 18])
        expected = 8
        result = Solution().widthOfBinaryTree(root)
        self.assertEqual(expected, result)

    def test_case_5(self):
        root = list_to_tree(
            [1, 2, 3, 4, None, None, 9, 6, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        )
        expected = 16
        result = Solution().widthOfBinaryTree(root)
        self.assertEqual(expected, result)

    def test_case_6(self):
        root = list_to_tree([3, 2, 4, None, None, 1, None])
        expected = 2
        result = Solution().widthOfBinaryTree(root)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
