#  Category: algorithms
#  Level: Easy
#  Percent: 51.2947%


#  Given a binary tree, determine if it is height-balanced.
#
#
#  Example 1:
#
#  Input: root = [3,9,20,null,null,15,7]
#  Output: true
#
#
#  Example 2:
#
#  Input: root = [1,2,2,3,3,null,null,4,4]
#  Output: false
#
#
#  Example 3:
#
#  Input: root = []
#  Output: true
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [0, 5000].
#  	-10⁴ <= Node.val <= 10⁴
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import unittest
from dataclasses import dataclass
from typing import Optional, Tuple

from conversions import liststr_to_tree


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


#  start_marker
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
            balanced = l_balanced and r_balanced and difference < 2
            return balanced, height + 1

        return balanced_r(root)[0]


#  end_marker


class TestSolution(unittest.TestCase):
    def test1(self):
        root = liststr_to_tree("[3,9,20,null,null,15,7]")
        expected = True
        self.assertEqual(Solution().isBalanced(root), expected)

    def test2(self):
        root = liststr_to_tree("[1,2,2,3,3,null,null,4,4]")
        expected = False
        self.assertEqual(Solution().isBalanced(root), expected)

    def test3(self):
        root = None
        expected = True
        self.assertEqual(Solution().isBalanced(root), expected)


if __name__ == "__main__":
    # TestSolution().test2()
    unittest.main()
