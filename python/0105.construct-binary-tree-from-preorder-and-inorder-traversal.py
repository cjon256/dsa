#  Category: algorithms
#  Level: Medium
#  Percent: 63.333332%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
#
#
#  Example 1:
#
#  Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#  Output: [3,9,20,null,null,15,7]
#
#
#  Example 2:
#
#  Input: preorder = [-1], inorder = [-1]
#  Output: [-1]
#
#
#
#  Constraints:
#
#
#  	1 <= preorder.length <= 3000
#  	inorder.length == preorder.length
#  	-3000 <= preorder[i], inorder[i] <= 3000
#  	preorder and inorder consist of unique values.
#  	Each value of inorder also appears in preorder.
#  	preorder is guaranteed to be the preorder traversal of the tree.
#  	inorder is guaranteed to be the inorder traversal of the tree.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import unittest
from typing import List, Optional

from leetopenlib.tree import (
    TreeNode,
    list_to_tree,
    tree_to_list,
    tree_to_simple_list_inorder,
    tree_to_simple_list_preorder,
)
from rich import print as rprint

DEBUG = 1


#  start_marker
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # print(f"buildTree (preorder: {preorder}, inorder: {inorder})")
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        inorder_index = {}
        for i, val in enumerate(inorder):
            inorder_index[val] = i

        # print(f"inorder_index: {inorder_index}")
        preorder_curr = 1

        def build_tree(
            node: TreeNode, left: int, mid: int, right: int
        ) -> Optional[TreeNode]:
            nonlocal preorder_curr
            if preorder_curr >= len(preorder):
                return node

            # print(tree_to_list(root))
            # print("--------------------------------")
            # print(f"node: {node.val}, left: {left}, mid: {mid}, right: {right}")
            # print(f"preorder_curr: {preorder_curr}")
            if left == right:
                # print("left == right")
                return node

            next_val = preorder[preorder_curr]
            inorder_index_next_val = inorder_index[next_val]
            # print(
            #     f"next_val: {next_val}, inorder_index_next_val: {inorder_index_next_val}"
            # )
            if inorder_index_next_val >= left and inorder_index_next_val < mid:
                # print("--- ")
                # print("going to left")
                left_val = preorder[preorder_curr]
                # print(f"Node: {node.val}, left_val: {left_val}")
                node.left = TreeNode(left_val)
                # print(f"node.left: {node.left.val}")
                preorder_curr += 1
                build_tree(
                    node.left,
                    left,
                    inorder_index[left_val],
                    mid,
                )

            if preorder_curr >= len(preorder):
                return node
            next_val = preorder[preorder_curr]
            inorder_index_next_val = inorder_index[next_val]
            if inorder_index_next_val >= mid + 1 and inorder_index_next_val < right:
                # print("---")
                # print("going to right")
                right_val = preorder[preorder_curr]
                # print(f"Node: {node.val}, right_val: {right_val}")
                node.right = TreeNode(right_val)
                preorder_curr += 1
                build_tree(node.right, mid + 1, inorder_index[right_val], right)
            return node

        return build_tree(root, 0, inorder_index[root.val], len(inorder))
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        expected = [3, 9, 20, None, None, 15, 7]
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_2(self):
        expected = [-1]
        preorder = [-1]
        inorder = [-1]
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_3(self):
        expected = []
        preorder = []
        inorder = []
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_4(self):
        expected = [1, 2]
        preorder = [1, 2]
        inorder = [2, 1]
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_5(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_6(self):
        expected = [1, 2, 3, 4, None, 6, 7]
        preorder = [1, 2, 4, 3, 6, 7]
        inorder = [4, 2, 1, 6, 3, 7]
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_7(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_8(self):
        expected = [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7]
        preorder = [1, 2, 3, 4, 5, 6, 7]
        inorder = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_9(self):
        expected = [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7]
        preorder = [1, 2, 3, 4, 5, 6, 7]
        inorder = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_10(self):
        expected = [1, 2, 3, None, None, None, 4, None, 5, None, 6, None, 7]
        preorder = [1, 2, 3, 4, 5, 6, 7]
        inorder = [2, 1, 3, 4, 5, 6, 7]
        self.assertEqual(
            tree_to_list(Solution().buildTree(preorder, inorder)), expected
        )
        self.assertEqual(
            tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
            preorder,
        )
        self.assertEqual(
            tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
            inorder,
        )

    def test_case_11(self):
        # test all trees with 2 nodes
        trees = [[1, 2], [1, None, 2]]
        for tree in trees:
            preorder = tree
            inorder = tree
            # self.assertEqual(
            #     tree_to_list(Solution().buildTree(preorder, inorder)), tree
            # )
            self.assertEqual(
                tree_to_simple_list_preorder(Solution().buildTree(preorder, inorder)),
                preorder,
            )
            self.assertEqual(
                tree_to_simple_list_inorder(Solution().buildTree(preorder, inorder)),
                inorder,
            )


if __name__ == "__main__":
    unittest.main()
