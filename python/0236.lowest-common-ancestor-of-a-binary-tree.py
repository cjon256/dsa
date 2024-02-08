#  Category: algorithms
#  Level: Medium
#  Percent: 61.335575%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
#  According to the definition of LCA on Wikipedia: “The lowest common ancestor
#  is defined between two nodes p and q as the lowest node in T that has both p
#  and q as descendants (where we allow a node to be a descendant of itself).”
#
#
#  Example 1:
#
#  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#  Output: 3
#  Explanation: The LCA of nodes 5 and 1 is 3.
#
#
#  Example 2:
#
#  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#  Output: 5
#  Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
#  of itself according to the LCA definition.
#
#
#  Example 3:
#
#  Input: root = [1,2], p = 1, q = 2
#  Output: 1
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
#  	p and q will exist in the tree.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import unittest
from typing import List, Optional

from leetopenlib.tree import TreeNode, list_to_tree


#  start_marker
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def lca(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            if node == p or node == q:
                return node
            left = lca(node.left)
            right = lca(node.right)
            if left is None:
                return right
            if right is None:
                return left
            return node

        retval = lca(root)
        if retval is None:
            raise ValueError("retval is None")
        return retval

    # end_marker
    def lowestCommonAncestor_dumb(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def find_path_to_node(
            node: Optional[TreeNode], target: TreeNode, path: List[TreeNode]
        ) -> List[TreeNode]:
            if node is None:
                return []
            if node.val == target.val:
                return path
            if node.left:
                left = find_path_to_node(node.left, target, path + [node.left])
                if left:
                    return left
            if node.right:
                right = find_path_to_node(node.right, target, path + [node.right])
                if right:
                    return right
            return []

        path_to_p = find_path_to_node(root, p, [root])
        path_to_q = find_path_to_node(root, q, [root])
        if not path_to_p or not path_to_q:
            raise ValueError("path_to_p or path_to_q is None")
        for node in reversed(path_to_p):
            if node in path_to_q:
                return node
        raise ValueError("no common ancestor found")


# def this_would_work_if_the_trees_were_bsts...(self, root, p, q):
#     def recur(node: Optional[TreeNode], min: int, max: int) -> Optional[TreeNode]:
#         if node is None:
#             return None
#         if node.val > max:
#             return recur(node.left, min, max)
#         if node.val < min:
#             return recur(node.right, min, max)
#         return node
#
#     if p.val > q.val:
#         min, max = q.val, p.val
#     else:
#         min, max = p.val, q.val
#     result = recur(root, min, max)
#     if result is None:
#         raise ValueError("result is None")
#     return result


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left is not None:
        return left
    return find_node(root.right, val)  # type: ignore


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 5)
        q = find_node(root, 1)
        expected = 3
        if root is None or p is None or q is None:
            self.fail("p or q is None")
        else:
            result = Solution().lowestCommonAncestor(root, p, q)
            self.assertEqual(result.val, expected)

    def test_case_2(self):
        root = list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 5)
        q = find_node(root, 4)
        expected = 5
        if root is None or p is None or q is None:
            self.fail("p or q is None")
        else:
            result = Solution().lowestCommonAncestor(root, p, q)
            self.assertEqual(result.val, expected)

    def test_case_3(self):
        root = list_to_tree([1, 2, None])
        p = find_node(root, 1)
        q = find_node(root, 2)
        expected = 1
        if root is None or p is None or q is None:
            self.fail("p or q is None")
        else:
            result = Solution().lowestCommonAncestor(root, p, q)
            self.assertEqual(result.val, expected)


if __name__ == "__main__":
    unittest.main()
