#  Category: algorithms
#  Level: Medium
#  Percent: 66.55395%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
#
#  Example 1:
#
#  Input: root = [3,9,20,null,null,15,7]
#  Output: [[3],[9,20],[15,7]]
#
#
#  Example 2:
#
#  Input: root = [1]
#  Output: [[1]]
#
#
#  Example 3:
#
#  Input: root = []
#  Output: []
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the tree is in the range [0, 2000].
#  	-1000 <= Node.val <= 1000
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import unittest
from collections import deque
from typing import List, Optional

from conversions import TreeNode, tree_to_liststr


#  start_marker
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        current_queue: deque[TreeNode] = deque([root])
        levels_list = []
        while True:
            curr_list = []
            next_queue: deque[TreeNode] = deque()
            while current_queue:
                node = current_queue.popleft()
                curr_list.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            levels_list.append(curr_list)
            if not next_queue:
                break
            current_queue = next_queue
        return levels_list


#  end_marker
def liststr_to_list(s: str) -> List[Optional[int]]:
    return list(map(lambda x: int(x) if x != "null" else None, s[1:-1].split(",")))


def list_to_tree(lis: List[Optional[int]]) -> Optional[TreeNode]:
    if not lis or lis[0] is None:
        return None
    root = TreeNode(lis[0])
    queue = [root]
    i = 1
    while i < len(lis):
        node = queue.pop(0)
        left = lis[i]
        if left is not None:
            node.left = TreeNode(left)
            queue.append(node.left)
        i += 1
        right = lis[i]
        if i < len(lis) and right is not None:
            node.right = TreeNode(right)
            queue.append(node.right)
        i += 1
    return root


# def tree_to_list(root: TreeNode) -> List[Optional(int)]:
#     if not root:
#         return []
#     queue = [root]
#     lis = []
#     while queue:
#         node = queue.pop(0)
#         if node:
#             lis.append(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         else:
#             lis.append(None)
#     return lis


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = list_to_tree([3, 9, 20, None, None, 15, 7])
        expected = [[3], [9, 20], [15, 7]]
        self.assertEqual(Solution().levelOrder(root), expected)

    def test_case_2(self):
        root = list_to_tree([1])
        expected = [[1]]
        self.assertEqual(Solution().levelOrder(root), expected)

    def test_case_3(self):
        root = list_to_tree([])
        expected = []
        self.assertEqual(Solution().levelOrder(root), expected)

    def test_case_4(self):
        root = list_to_tree([1, 2, None])
        expected = [[1], [2]]
        self.assertEqual(Solution().levelOrder(root), expected)


if __name__ == "__main__":
    unittest.main()
