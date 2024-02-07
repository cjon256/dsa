#  Category: algorithms
#  Level: Easy
#  Percent: 75.53116%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#
#  Example 1:
#
#  Input: head = [1,2,3,4,5]
#  Output: [5,4,3,2,1]
#
#
#  Example 2:
#
#  Input: head = [1,2]
#  Output: [2,1]
#
#
#  Example 3:
#
#  Input: head = []
#  Output: []
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the list is the range [0, 5000].
#  	-5000 <= Node.val <= 5000
#
#
#
#  Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import unittest
from typing import Optional

from leetopenlib.linked_list import ListNode, linked_list_to_list, list_to_linked_list


#  start_marker
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
        #  end_marker


class OldSolution:
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_r(prev: ListNode, curr: ListNode) -> ListNode:
            if curr is None:
                return prev
            curr_next = curr.next
            curr.next = prev
            return reverse_list_r(curr, curr_next)

        if head is None:
            return head
        child = head.next
        if child is None:
            return head
        head.next = None
        child_next = child.next
        child.next = head
        return reverse_list_r(child, child_next)

    def reverseList_iter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            child = curr.next
            curr.next = prev
            prev = curr
            curr = child
        return prev


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        head = list_to_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(linked_list_to_list(s.reverseList(head)), [5, 4, 3, 2, 1])

    def test_2(self):
        s = Solution()
        head = list_to_linked_list([1, 2])
        self.assertEqual(linked_list_to_list(s.reverseList(head)), [2, 1])

    def test_3(self):
        s = Solution()
        head = list_to_linked_list([])
        self.assertEqual(linked_list_to_list(s.reverseList(head)), [])

    def test_4(self):
        s = Solution()
        head = list_to_linked_list([1])
        self.assertEqual(linked_list_to_list(s.reverseList(head)), [1])


if __name__ == "__main__":
    unittest.main()
