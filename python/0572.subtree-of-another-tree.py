#  Level: Easy
#  Percent: 47.4768%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
#  with the same structure and node values of subRoot and false otherwise.
#
#  A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's
#  descendants. The tree tree could also be considered as a subtree of itself.
#
#
#  Example 1:
#
#  Input: root = [3,4,5,1,2], subRoot = [4,1,2]
#  Output: true
#
#
#  Example 2:
#
#  Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#  Output: false
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the root tree is in the range [1, 2000].
#  	The number of nodes in the subRoot tree is in the range [1, 1000].
#  	-10⁴ <= root.val <= 10⁴
#  	-10⁴ <= subRoot.val <= 10⁴
#


import unittest
from typing import List, Optional

from leetopenlib.tree import TreeNode, liststr_to_tree


#  start_marker
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def trees_match(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            return (
                tree1.val == tree2.val
                and trees_match(tree1.left, tree2.left)
                and trees_match(tree1.right, tree2.right)
            )

        def find_all_matches(tree: Optional[TreeNode], val: int) -> List[TreeNode]:
            if tree is None:
                return []
            matches = []

            def dfs(node: Optional[TreeNode]) -> None:
                if node is None:
                    return
                if node.val == val:
                    matches.append(node)
                dfs(node.left)
                dfs(node.right)

            dfs(tree)
            return matches

        if subRoot is None:
            return True
        if root is None:
            return subRoot is None

        matches = find_all_matches(root, subRoot.val)
        for match in matches:
            if trees_match(match, subRoot):
                return True
        return False


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = liststr_to_tree("[3,4,5,1,2]")
        subRoot = liststr_to_tree("[4,1,2]")
        expected_result = True
        self.assertEqual(Solution().isSubtree(root, subRoot), expected_result)

    def test_case_2(self):
        root = liststr_to_tree("[3,4,5,1,2,null,null,null,null,0]")
        subRoot = liststr_to_tree("[4,1,2]")
        expected_result = False
        self.assertEqual(Solution().isSubtree(root, subRoot), expected_result)

    def test_case_3(self):
        root = liststr_to_tree("[1,1]")
        subRoot = liststr_to_tree("[1]")
        expected_result = True
        self.assertEqual(Solution().isSubtree(root, subRoot), expected_result)

    def test_case_4(self):
        root = liststr_to_tree("[3,4,5,1,2,null,null,0]")
        subRoot = liststr_to_tree("[4,1,2]")
        expected_result = False
        self.assertEqual(Solution().isSubtree(root, subRoot), expected_result)

    def test_case_5(self):
        root = liststr_to_tree("[1,1]")
        subRoot = liststr_to_tree("[]")
        expected_result = True
        self.assertEqual(Solution().isSubtree(root, subRoot), expected_result)

    def test_case_6(self):
        root = liststr_to_tree("[1]")
        subRoot = liststr_to_tree("[1]")
        expected_result = True
        self.assertEqual(Solution().isSubtree(root, subRoot), expected_result)

    def test_case_7(self):
        root = liststr_to_tree("[1,2,3]")
        subRoot = liststr_to_tree("[2,3]")
        expected_result = False
        self.assertEqual(Solution().isSubtree(root, subRoot), expected_result)

    def test_case_8(self):
        root = liststr_to_tree("[]")
        subRoot = liststr_to_tree("[4,1,2]")
        expected_result = False
        self.assertEqual(Solution().isSubtree(root, subRoot), expected_result)

    def test_case_9(self):
        root = liststr_to_tree("[]")
        subRoot = liststr_to_tree("[]")
        expected_result = True
        self.assertEqual(Solution().isSubtree(root, subRoot), expected_result)


if __name__ == "__main__":
    unittest.main()
