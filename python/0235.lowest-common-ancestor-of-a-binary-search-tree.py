#  Category: algorithms
#  Level: Medium
#  Percent: 63.982697%


#  Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
#  According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#
#  Example 1:
#
#  Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#  Output: 6
#  Explanation: The LCA of nodes 2 and 8 is 6.
#
#
#  Example 2:
#
#  Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#  Output: 2
#  Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
#
#
#  Example 3:
#
#  Input: root = [2,1], p = 2, q = 1
#  Output: 2
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [2, 10⁵].
#  	-10⁹ <= Node.val <= 10⁹
#  	All Node.val are unique.
#  	p != q
#  	p and q will exist in the BST.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import unittest

from conversions import TreeNode, liststr_to_tree


#  start_marker
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def find_last_node_with_both(curr: "TreeNode") -> "TreeNode":
            if q.val < curr.val and p.val < curr.val:
                return find_last_node_with_both(curr.left)
            elif q.val > curr.val and p.val > curr.val:
                return find_last_node_with_both(curr.right)
            return curr

        return find_last_node_with_both(root)


#  end_marker
class TestSolution(unittest.TestCase):
    def test1(self):
        root = liststr_to_tree("[6,2,8,0,4,7,9,null,null,3,5]")
        p = root.left
        q = root.right
        self.assertEqual(Solution().lowestCommonAncestor(root, p, q).val, 6)

    def test2(self):
        root = liststr_to_tree("[6,2,8,0,4,7,9,null,null,3,5]")
        p = root.left
        q = root.left.right
        self.assertEqual(Solution().lowestCommonAncestor(root, p, q).val, 2)

    def test3(self):
        root = liststr_to_tree("[2,1]")
        p = root
        q = root.left
        self.assertEqual(Solution().lowestCommonAncestor(root, p, q).val, 2)


if __name__ == "__main__":
    unittest.main()
