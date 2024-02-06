#  Category: algorithms
#  Level: Medium
#  Percent: 43.63228%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#  Example 1:
#
#  Input: head = [1,2,3,4,5], n = 2
#  Output: [1,2,3,5]
#
#
#  Example 2:
#
#  Input: head = [1], n = 1
#  Output: []
#
#
#  Example 3:
#
#  Input: head = [1,2], n = 1
#  Output: [1]
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the list is sz.
#  	1 <= sz <= 30
#  	0 <= Node.val <= 100
#  	1 <= n <= sz
#
#
#  Follow up: Could you do this in one pass?
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import unittest
from typing import Any, List, Optional

from leetopenlib.linked_list import ListNode, linked_list_to_list, list_to_linked_list


#  start_marker
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None and n == 1:
            return None
        curr: Any = head
        for _ in range(n):
            curr = curr.next
        if curr is None:
            return head.next
        curr_minus_n: Any = head
        while curr.next:
            curr = curr.next
            curr_minus_n = curr_minus_n.next
        curr_minus_n.next = curr_minus_n.next.next
        return head


#  end_marker
class TestSolution(unittest.TestCase):
    def test_1(self) -> None:
        head = list_to_linked_list([1, 2, 3, 4, 5])
        n = 2
        expected = [1, 2, 3, 5]
        self.assertEqual(
            linked_list_to_list(Solution().removeNthFromEnd(head, n)), expected
        )

    def test_2(self) -> None:
        head = list_to_linked_list([1])
        n = 1
        expected: List = []
        self.assertEqual(
            linked_list_to_list(Solution().removeNthFromEnd(head, n)), expected
        )

    def test_3(self) -> None:
        head = list_to_linked_list([1, 2])
        n = 1
        expected = [1]
        self.assertEqual(
            linked_list_to_list(Solution().removeNthFromEnd(head, n)), expected
        )

    def test_4(self) -> None:
        head = list_to_linked_list([1, 2])
        n = 2
        expected = [2]
        self.assertEqual(
            linked_list_to_list(Solution().removeNthFromEnd(head, n)), expected
        )

    def test_5(self) -> None:
        head = list_to_linked_list([1, 2, 3])
        n = 3
        expected = [2, 3]
        self.assertEqual(
            linked_list_to_list(Solution().removeNthFromEnd(head, n)), expected
        )


if __name__ == "__main__":
    unittest.main()
