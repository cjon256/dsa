# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods, protected-access, too-many-locals
import unittest
from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


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
