# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods, protected-access, too-many-locals
import unittest
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

from ppbtree import print_tree


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

    def __iter__(self):
        yield self.val
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right

    def _display_aux(self) -> Tuple[List[str], int, int, int]:
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f"{self.val}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None and self.left is not None:
            lines, n, p, x = self.left._display_aux()
            s = f"{self.val}"
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None and self.right is not None:
            lines, n, p, x = self.right._display_aux()
            s = f"{self.val}"
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Only need the check to make type checker happy...
        if self.left is not None and self.right is not None:
            # Two children.
            left, n, p, x = self.left._display_aux()
            right, m, q, y = self.right._display_aux()
            s = f"{self.val}"
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
            second_line = (
                x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
            )
            if p < q:
                left += [n * " "] * (q - p)
            elif q < p:
                right += [m * " "] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [
                a + u * " " + b for a, b in zipped_lines
            ]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
        return [], 0, 0, 0

    # from https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(self) -> None:
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def pp(self) -> None:
        print_tree(self, nameattr="val", left_child="left", right_child="right")

    def __repr__(self):
        return f"TreeNode({self.val})"


# convert to list without placeholders
def tree_to_simple_list_preorder(root):
    """Convert tree to list in preorder without placeholders."""
    if root is None:
        return []
    return (
        [root.val]
        + tree_to_simple_list_preorder(root.left)
        + tree_to_simple_list_preorder(root.right)
    )


def tree_to_simple_list_inorder(root):
    """Convert tree to list in inorder without placeholders."""
    if root is None:
        return []
    return (
        tree_to_simple_list_inorder(root.left)
        + [root.val]
        + tree_to_simple_list_inorder(root.right)
    )


def tree_to_simple_list_postorder(root):
    """Convert tree to list in postorder without placeholders."""
    if root is None:
        return []
    return (
        tree_to_simple_list_postorder(root.left)
        + tree_to_simple_list_postorder(root.right)
        + [root.val]
    )


def tree_to_simple_list_levelorder(root):
    """Convert tree to list in levelorder without placeholders."""
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# pylint: disable-next=line-too-long
# per https://leetcode.com/problems/recover-binary-search-tree/solutions/32539/Tree-Deserializer-and-Visualizer-for-Python/
def liststr_to_tree(string):
    """Convert list string to tree (uses 'null' for placeholders)."""
    if string in ["{}", "[]"]:
        return None
    nodes = [
        None if val == "null" else TreeNode(int(val))
        for val in string.strip("[]{}").split(",")
    ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def tree_to_liststr(root: Optional[TreeNode]) -> str:
    """Convert tree to list string (uses 'null' for placeholders)."""
    if not root:
        return "[]"
    result: List[int | str] = []
    queue: List[Optional[TreeNode]] = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    while result[-1] == "null":
        result.pop()
    return f"[{','.join([str(x) for x in result])}]"


def pretty_print_tree(root: TreeNode) -> None:
    if not root:
        print("Empty tree")
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


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


def list_to_tree_preorder(lst: List[Optional[int]]) -> Optional[TreeNode]:
    if not lst or lst[0] is None:
        return None
    root = TreeNode(lst[0])
    stack = [root]
    for i in range(1, len(lst)):
        val = lst[i]
        if val is not None:
            node = TreeNode(val)
            stack[-1].left = node
            stack.append(node)
        else:
            stack.pop()
            if stack:
                stack[-1].right = None
    return root


optional_int = Union[int, None]


def tree_to_list(root: Optional[TreeNode]) -> List[optional_int]:
    if not root:
        return []
    queue: List[Optional[TreeNode]] = [root]
    lis: List[optional_int] = []
    while queue:
        node = queue.pop(0)
        if node:
            lis.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            lis.append(None)
    while lis[-1] is None:
        lis.pop()
    return lis


class TestSerDeTree(unittest.TestCase):
    def test_case_1(self):
        root = liststr_to_tree("[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]")
        self.assertEqual(tree_to_liststr(root), "[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]")

    def test_case_2(self):
        root = liststr_to_tree("[1,2,3,null,null,4,5]")
        self.assertEqual(tree_to_liststr(root), "[1,2,3,null,null,4,5]")

    def test_case_3(self):
        root = liststr_to_tree("[1,2,3,null,null,4,null,null,5]")
        self.assertEqual(tree_to_liststr(root), "[1,2,3,null,null,4,null,null,5]")

    def test_case_4(self):
        root = list_to_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        assert root is not None
        self.assertEqual(
            tree_to_list(root), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        )

    def test_case_5(self):
        root = list_to_tree([1, 2, 3, None, None, 4, 5])
        assert root is not None
        self.assertEqual(tree_to_list(root), [1, 2, 3, None, None, 4, 5])

    def test_case_6(self):
        root = list_to_tree([1, 2, 3, None, None, 4, None, None, 5])
        assert root is not None
        self.assertEqual(tree_to_list(root), [1, 2, 3, None, None, 4, None, None, 5])

    def test_case_7(self):
        root = list_to_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        assert root is not None
        self.assertEqual(tree_to_list(root), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_all_trees_with_2_nodes(self):
        # test all trees with 2 nodes
        trees = [[1, 2, None], [1, None, 2]]
        preorders = [[1, 2], [1, 2]]
        inorders = [[2, 1], [1, 2]]

        for tree, preorder, inorder in zip(trees, preorders, inorders):
            root = list_to_tree(tree)
            while tree[-1] is None:
                tree.pop()
            self.assertEqual(tree_to_list(root), tree)
            self.assertEqual(preorder, tree_to_simple_list_preorder(root))
            self.assertEqual(inorder, tree_to_simple_list_inorder(root))

    def test_all_trees_with_3_nodes(self):
        # test all trees with 3 nodes
        trees = [
            [1, 2, 3],
            [1, 2, None, 3, None],
            [1, 2, None, None, 3],
            [1, None, 2, 3, None],
            [1, None, 2, None, 3],
        ]
        preorders = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
        inorders = [[2, 1, 3], [3, 2, 1], [2, 3, 1], [1, 3, 2], [1, 2, 3]]

        for tree, preorder, inorder in zip(trees, preorders, inorders):
            root = list_to_tree(tree)
            while tree[-1] is None:
                tree.pop()
            self.assertEqual(tree_to_list(root), tree)
            self.assertEqual(preorder, tree_to_simple_list_preorder(root))
            self.assertEqual(inorder, tree_to_simple_list_inorder(root))

    def test_all_trees_with_4_nodes(self):
        # test all trees with 4 nodes
        trees = [
            [1, 2, 3, 4, None],  # ............  1
            [1, 2, 3, None, 4],  # ............  2
            [1, 2, 3, None, None, 4, None],  #   3
            [1, 2, 3, None, None, None, 4],  #   4
            [1, 2, None, 3, 4],  # ............  5
            [1, None, 2, 3, 4],  # ............  6
            [1, 2, None, 3, None, 4, None],  #   7
            [1, 2, None, 3, None, None, 4],  #   8
            [1, 2, None, None, 3, 4, None],  #   9
            [1, 2, None, None, 3, None, 4],  #   10
            [1, None, 2, 3, None, 4, None],  #   11
            [1, None, 2, 3, None, None, 4],  #   12
            [1, None, 2, None, 3, 4, None],  #   13
            [1, None, 2, None, 3, None, 4],  #   14
        ]
        preorders = [
            [1, 2, 4, 3],  # ..................  1
            [1, 2, 4, 3],  # ..................  2
            [1, 2, 3, 4],  # ..................  3
            [1, 2, 3, 4],  # ..................  4
            [1, 2, 3, 4],  # ..................  5
            [1, 2, 3, 4],  # ..................  6
            [1, 2, 3, 4],  # ..................  7
            [1, 2, 3, 4],  # ..................  8
            [1, 2, 3, 4],  # ..................  9
            [1, 2, 3, 4],  # ..................  10
            [1, 2, 3, 4],  # ..................  11
            [1, 2, 3, 4],  # ..................  12
            [1, 2, 3, 4],  # ..................  13
            [1, 2, 3, 4],  # ..................  14
        ]

        inorders = [
            [4, 2, 1, 3],  # ..................  1
            [2, 4, 1, 3],  # ..................  2
            [2, 1, 4, 3],  # ..................  3
            [2, 1, 3, 4],  # ..................  4
            [3, 2, 4, 1],  # ..................  5
            [1, 3, 2, 4],  # ..................  6
            [4, 3, 2, 1],  # ..................  7
            [3, 4, 2, 1],  # ..................  8
            [2, 4, 3, 1],  # ..................  9
            [2, 3, 4, 1],  # .................. 10
            [1, 4, 3, 2],  # .................. 11
            [1, 3, 4, 2],  # .................. 12
            [1, 2, 4, 3],  # .................. 13
            [1, 2, 3, 4],  # .................. 14
        ]
        for tree, preorder, inorder in zip(trees, preorders, inorders):
            root = list_to_tree(tree)
            while tree[-1] is None:
                tree.pop()
            level_order = [1, 2, 3, 4]
            self.assertEqual(tree_to_list(root), tree)
            self.assertEqual(preorder, tree_to_simple_list_preorder(root))
            self.assertEqual(inorder, tree_to_simple_list_inorder(root))
            self.assertEqual(tree_to_simple_list_levelorder(root), level_order)


if __name__ == "__main__":
    unittest.main()
