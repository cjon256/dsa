# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods
import unittest
from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

    def __repr__(self):
        return f"TreeNode({self.val})"


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


# pylint: disable-next=line-too-long
# per https://leetcode.com/problems/recover-binary-search-tree/solutions/32539/Tree-Deserializer-and-Visualizer-for-Python/
def liststr_to_tree(string):
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


def tree_to_liststr(root):
    if not root:
        return "[]"
    result = []
    queue = [root]
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


def list_to_linked_list(list_):
    if not list_:
        return None
    head = ListNode(list_[0])
    node = head
    for i in list_[1:]:
        node.next = ListNode(i)
        node = node.next
    return head


def linked_list_to_list(head):
    if not head:
        return []
    list_ = []
    node = head
    while node:
        list_.append(node.val)
        node = node.next
    return list_


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


class TestSerdeList(unittest.TestCase):
    def test_case_1(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(linked_list_to_list(list_to_linked_list(lst)), lst)

    def test_case_2(self):
        lst = []
        self.assertEqual(linked_list_to_list(list_to_linked_list(lst)), lst)

    def test_case_3(self):
        lst = [1]
        self.assertEqual(linked_list_to_list(list_to_linked_list(lst)), lst)


if __name__ == "__main__":
    unittest.main()
