import unittest
from dataclasses import dataclass

# Definition for a binary tree node.


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_last_node_with_both(curr: 'TreeNode') -> 'TreeNode':
            if q.val < curr.val and p.val < curr.val:
                return find_last_node_with_both(curr.left)
            elif q.val > curr.val and p.val > curr.val:
                return find_last_node_with_both(curr.right)
            return curr
        return find_last_node_with_both(root)


"""
Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
of itself according to the LCA definition.

"""


class TestSolution(unittest.TestCase):
    def test1(self):
        root = TreeNode(6,
                        TreeNode(2,
                                 TreeNode(0),
                                 TreeNode(4,
                                          TreeNode(3),
                                          TreeNode(5))),
                        TreeNode(8,
                                 TreeNode(7),
                                 TreeNode(9)))
        p = root.left
        q = root.right
        self.assertEqual(Solution().lowestCommonAncestor(root, p, q).val, 6)

    def test2(self):
        root = TreeNode(6,
                        TreeNode(2,
                                 TreeNode(0),
                                 TreeNode(4,
                                          TreeNode(3),
                                          TreeNode(5))),
                        TreeNode(8,
                                 TreeNode(7),
                                 TreeNode(9)))
        p = root.left
        q = root.left.right
        self.assertEqual(Solution().lowestCommonAncestor(root, p, q).val, 2)


if __name__ == '__main__':
    unittest.main()
