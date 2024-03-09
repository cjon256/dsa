#  Category: algorithms
#  Level: Medium
#  Percent: 56.1%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
#
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
# Example 2:
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
#
# Constraints:
#
#     The number of nodes in the list is in the range [1, 5 * 104].
#     1 <= Node.val <= 1000
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        prev = None
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast is not None:
            prev = slow
            slow = slow.next

        def reverse_list(prev, head):
            if head is None:
                return prev
            next = head.next
            head.next = prev
            return reverse_list(head, next)

        prev.next = None
        second_head = slow
        second_head = reverse_list(None, second_head)

        def zip_lists(h1, h2):
            if h1 is None or h2 is None:
                return
            n1 = h1.next
            n2 = h2.next
            h1.next = h2
            h2.next = n1 if n1 is not None else n2
            zip_lists(n1, n2)

        zip_lists(head, second_head)
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        head = list_to_linked_list([1, 2, 3, 4])
        expected = [1, 4, 2, 3]
        Solution().reorderList(head)
        result = linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_case_2(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        expected = [1, 5, 2, 4, 3]
        Solution().reorderList(head)
        result = linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_case_3(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6])
        expected = [1, 6, 2, 5, 3, 4]
        Solution().reorderList(head)
        result = linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_case_4(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7])
        expected = [1, 7, 2, 6, 3, 5, 4]
        Solution().reorderList(head)
        result = linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_case_5(self):
        head = list_to_linked_list([1])
        expected = [1]
        Solution().reorderList(head)
        result = linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_case_6(self):
        head = list_to_linked_list([])
        expected = []
        Solution().reorderList(head)
        result = linked_list_to_list(head)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
