import unittest
from typing import Optional
from dataclasses import dataclass

# Definition for a binary tree node.


@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
        return root


"""
Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
"""


class TestSolution(unittest.TestCase):
    def test_invertTree_1(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                        TreeNode(7, TreeNode(6), TreeNode(9)))
        expected = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)),
                            TreeNode(2, TreeNode(3), TreeNode(1)))
        self.assertEqual(Solution().invertTree(root), expected)

    def test_invertTree_2(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        expected = TreeNode(2, TreeNode(3), TreeNode(1))
        self.assertEqual(Solution().invertTree(root), expected)

    def test_invertTree_3(self):
        root = None
        expected = None
        self.assertEqual(Solution().invertTree(root), expected)


if __name__ == '__main__':
    unittest.main()
