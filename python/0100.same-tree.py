#  Category: algorithms
#  Level: Easy
#  Percent: 60.534817%


#  Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
#  Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
#
#  Example 1:
#
#  Input: p = [1,2,3], q = [1,2,3]
#  Output: true
#
#
#  Example 2:
#
#  Input: p = [1,2], q = [1,null,2]
#  Output: false
#
#
#  Example 3:
#
#  Input: p = [1,2,1], q = [1,1,2]
#  Output: false
#
#
#
#  Constraints:
#
#
#  	The number of nodes in both trees is in the range [0, 100].
#  	-10⁴ <= Node.val <= 10⁴
#


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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same_r(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            return same_r(t1.left, t2.left) and same_r(t1.right, t2.right)

        return same_r(p, q)


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        p = liststr_to_tree("[1,2,3]")
        q = liststr_to_tree("[1,2,3]")
        self.assertEqual(Solution().isSameTree(p, q), True)

    def test_case_2(self):
        p = liststr_to_tree("[1,2]")
        q = liststr_to_tree("[1,null,2]")
        self.assertEqual(Solution().isSameTree(p, q), False)

    def test_case_3(self):
        p = liststr_to_tree("[1,2,1]")
        q = liststr_to_tree("[1,1,2]")
        self.assertEqual(Solution().isSameTree(p, q), False)


if __name__ == "__main__":
    unittest.main()
