from dataclasses import dataclass
import unittest
from typing import Optional, Tuple


@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def balanced_r(node: TreeNode) -> Tuple[bool, int]:
            if node is None:
                return True, 0
            l_balanced, left_height = balanced_r(node.left)
            r_balanced, right_height = balanced_r(node.right)
            difference = abs(left_height - right_height)
            height = max(left_height, right_height)
            balanced = (l_balanced and r_balanced and difference < 2)
            return balanced, height + 1
        return balanced_r(root)[0]


"""
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""


class TestSolution(unittest.TestCase):
    def test1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(
            20, TreeNode(15), TreeNode(7)))
        self.assertTrue(Solution().isBalanced(root))

    def test2(self):
        root = TreeNode(1, TreeNode(2, TreeNode(
            3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
        self.assertFalse(Solution().isBalanced(root))

    def test3(self):
        root = None
        self.assertTrue(Solution().isBalanced(root))


if __name__ == '__main__':
    # TestSolution().test2()
    unittest.main()
