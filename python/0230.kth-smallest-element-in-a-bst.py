#  Category: algorithms
#  Level: Medium
#  Percent: 71.99244%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
#
#  Example 1:
#
#  Input: root = [3,1,4,null,2], k = 1
#  Output: 1
#
#
#  Example 2:
#
#  Input: root = [5,3,6,2,4,null,null,1], k = 3
#  Output: 3
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is n.
#  	1 <= k <= n <= 10⁴
#  	0 <= Node.val <= 10⁴
#
#
#
#  Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import unittest
from typing import Optional

from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list


#  start_marker
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def nodes_in_tree(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return nodes_in_tree(node.left) + 1 + nodes_in_tree(node.right)

        if root is None:
            return -1

        def return_if_nth(node: TreeNode, n: int) -> TreeNode:
            nodes_in_left = nodes_in_tree(node.left)
            if nodes_in_left == n - 1:
                return node
            if nodes_in_left >= n:
                return return_if_nth(node.left, n)
            return return_if_nth(node.right, n - (1 + nodes_in_left))

        node = return_if_nth(root, k)
        if node:
            return node.val
        return node

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = list_to_tree([3, 1, 4, None, 2])
        root.pp()
        k = 1
        expected = 1
        result = Solution().kthSmallest(root, k)
        self.assertEqual(result, expected)

    def test_case_2(self):
        root = list_to_tree([5, 3, 6, 2, 4, None, None, 1, None])
        root.pp()
        k = 3
        expected = 3
        result = Solution().kthSmallest(root, k)
        self.assertEqual(result, expected)

    def test_case_3(self):
        root = list_to_tree([1])
        root.pp()
        k = 1
        expected = 1
        result = Solution().kthSmallest(root, k)
        self.assertEqual(result, expected)

    def test_case_4(self):
        root = list_to_tree([2, 1, None])
        root.pp()
        k = 1
        expected = 1
        result = Solution().kthSmallest(root, k)
        self.assertEqual(result, expected)

    def test_case_5(self):
        root = list_to_tree([2, 1, None])
        root.pp()
        k = 2
        expected = 2
        result = Solution().kthSmallest(root, k)
        self.assertEqual(result, expected)

    def test_case_6(self):
        root = list_to_tree([3, 1, 4, None, 2, None, 5])
        root.pp()
        k = 4
        expected = 4
        result = Solution().kthSmallest(root, k)
        self.assertEqual(result, expected)

    def test_case_7(self):
        root = list_to_tree(
            [7, 5, 11, 3, 6, 9, 12, 2, 4, None, None, 8, 10, None, None, 1, None]
        )
        root.pp()
        k = 10
        expected = 10
        result = Solution().kthSmallest(root, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
    # root = list_to_tree([5, 3, 6, 2, 4, None, None, 1, None])
    # root.pp()
    # k = 3
    # expected = 3
    # result = Solution().kthSmallest(root, k)
    # print(result, expected)
