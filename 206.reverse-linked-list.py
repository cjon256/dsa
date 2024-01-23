# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods
import unittest
from dataclasses import dataclass
from typing import Optional, Self

# @dataclass
# class ListNode:
#     val: int
#     next: Optional[Self] = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        head = head.next
        curr.next = None
        while head.next is not None:
            tmp = head.next
            head.next = curr
            curr = head
            head = tmp
        head.next = curr
        return head


class TestSolution(unittest.TestCase):
    def list_to_listnode(self, list_):
        if not list_:
            return None
        head = ListNode(list_[0])
        node = head
        for i in list_[1:]:
            node.next = ListNode(i)
            node = node.next
        return head

    def listnode_to_list(self, head):
        if not head:
            return []
        list_ = []
        node = head
        while node:
            list_.append(node.val)
            node = node.next
        return list_

    def test_1(self):
        s = Solution()
        head = self.list_to_listnode([1, 2, 3, 4, 5])
        self.assertEqual(self.listnode_to_list(s.reverseList(head)), [5, 4, 3, 2, 1])

    def test_2(self):
        s = Solution()
        head = self.list_to_listnode([1, 2])
        self.assertEqual(self.listnode_to_list(s.reverseList(head)), [2, 1])

    def test_3(self):
        s = Solution()
        head = self.list_to_listnode([])
        self.assertEqual(self.listnode_to_list(s.reverseList(head)), [])

    def test_4(self):
        s = Solution()
        head = self.list_to_listnode([1])
        self.assertEqual(self.listnode_to_list(s.reverseList(head)), [1])


# if __name__ == "__main__":
#     unittest.main()
