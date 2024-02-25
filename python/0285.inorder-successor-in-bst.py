#  Category: algorithms
#  Level: Medium
#  Percent: 49.483143%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.
#
#  The successor of a node p is the node with the smallest key greater than p.val.
#
#
#  Example 1:
#
#  Input: root = [2,1,3], p = 1
#  Output: 2
#  Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
#
#
#  Example 2:
#
#  Input: root = [5,3,6,2,4,null,null,1], p = 6
#  Output: null
#  Explanation: There is no in-order successor of the current node, so the answer is null.
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [1, 10⁴].
#  	-10⁵ <= Node.val <= 10⁵
#  	All Nodes will have unique values.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import unittest
from typing import Optional

from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list


#  start_marker
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def smallest_child(node: TreeNode) -> Optional[TreeNode]:
            if node.left is None:
                return None
            child = node.left
            while child.left is not None:
                child = child.left
            return child

        def find_parent(val: int, node: TreeNode) -> Optional[TreeNode]:
            if val == node.val:
                return None
            elif val < node.val:
                if node.left.val == val:
                    return node
                return find_parent(val, node.left)
            else:
                if node.right.val == val:
                    return node
                return find_parent(val, node.right)

        def get_upleftmost(node: TreeNode) -> Optional[TreeNode]:
            """just keep going up and to the left"""
            curr = node
            parent = find_parent(curr.val, root)
            if parent is None:
                return None
            while parent.right == curr:
                parent = find_parent(curr.val, root)
                if parent is None:
                    return None
                curr = parent
            return curr

        if p.right is None:
            parent = find_parent(p.val, root)
            if parent is None:
                return None
            elif p == parent.left:
                return parent
            else:
                nw_parent = get_upleftmost(parent)
                if nw_parent is None:
                    return None
                return find_parent(nw_parent.val, root)
        elif p.right.left is None:
            return p.right
        return smallest_child(p.right)


#  end_marker
null = None


def find_node_in_bst(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if node is None:
        return None
    if node.val == val:
        return node
    if val < node.val:
        return find_node_in_bst(node.left, val)
    return find_node_in_bst(node.right, val)


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root: TreeNode = list_to_tree([2, 1, 3])
        p = find_node_in_bst(root, 1)
        expected = 2
        result = Solution().inorderSuccessor(root, p)
        self.assertEqual(result.val, expected)

    def test_case_2(self):
        root = list_to_tree([5, 3, 6, 2, 4, null, null, 1, None])
        p = find_node_in_bst(root, 6)
        expected = None
        result = Solution().inorderSuccessor(root, p)
        self.assertEqual(result, expected)

    def test_case_3(self):
        root = list_to_tree([0])
        p = find_node_in_bst(root, 0)
        expected = None
        result = Solution().inorderSuccessor(root, p)
        self.assertEqual(result, expected)

    def test_case_4(self):
        root = list_to_tree([5, 3, 6, 1, 4, null, null, null, 2])
        p = find_node_in_bst(root, 4)
        expected = 5
        result = Solution().inorderSuccessor(root, p)
        self.assertEqual(result.val, expected)

    def test_case_5(self):
        # fmt: off
        root = list_to_tree([41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23])
        # fmt: on
        print(root.pp())
        p = find_node_in_bst(root, 40)
        expected = 41
        result = Solution().inorderSuccessor(root, p)
        self.assertEqual(result.val, expected)


if __name__ == "__main__":
    unittest.main()
