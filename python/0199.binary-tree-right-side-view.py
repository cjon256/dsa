#  Category: algorithms
#  Level: Medium
#  Percent: 62.71127%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
#
#  Example 1:
#
#  Input: root = [1,2,3,null,5,null,4]
#  Output: [1,3,4]
#
#
#  Example 2:
#
#  Input: root = [1,null,3]
#  Output: [1,3]
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
#  	The number of nodes in the tree is in the range [0, 100].
#  	-100 <= Node.val <= 100
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

from leetopenlib.tree import TreeNode, list_to_tree


#  start_marker
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        current_queue: deque[TreeNode] = deque([root])
        rightmost_list = []
        while True:
            rightmost = -101
            next_queue: deque[TreeNode] = deque()
            while current_queue:
                node = current_queue.popleft()
                rightmost = node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            rightmost_list.append(rightmost)
            if not next_queue:
                break
            current_queue = next_queue
        return rightmost_list
        #  end_marker

    def rightSideView_stinkers(self, root: Optional[TreeNode]) -> List[int]:
        """description really stinks"""
        res: List[int] = []
        if not root:
            return res
        node: Optional[TreeNode] = root
        while node:
            res.append(node.val)
            node = node.right
        return res


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = list_to_tree([1, 2, 3, None, 5, None, 4])
        expected = [1, 3, 4]
        self.assertListEqual(Solution().rightSideView(root), expected)

    def test_case_2(self):
        root = list_to_tree([1, None, 3])
        expected = [1, 3]
        self.assertListEqual(Solution().rightSideView(root), expected)

    def test_case_3(self):
        root = list_to_tree([])
        expected = []
        self.assertListEqual(Solution().rightSideView(root), expected)

    def test_case_4(self):
        root = list_to_tree([1, 2, None])
        expected = [1, 2]
        self.assertListEqual(Solution().rightSideView(root), expected)


if __name__ == "__main__":
    unittest.main()
