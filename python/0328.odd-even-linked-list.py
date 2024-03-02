#  Category: algorithms
#  Level: Medium
#  Percent: 61.374622%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
#
#  The first node is considered odd, and the second node is even, and so on.
#
#  Note that the relative order inside both the even and odd groups should remain as it was in the input.
#
#  You must solve the problem in O(1) extra space complexity and O(n) time complexity.
#
#
#  Example 1:
#
#  Input: head = [1,2,3,4,5]
#  Output: [1,3,5,2,4]
#
#
#  Example 2:
#
#  Input: head = [2,1,3,5,6,4,7]
#  Output: [2,3,6,7,1,5,4]
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the linked list is in the range [0, 10⁴].
#  	-10⁶ <= Node.val <= 10⁶
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        even_tail = even = ListNode(None)  # type: ignore
        odd_tail = odd = ListNode(None)  # type: ignore
        curr: Optional[ListNode] = head
        n = 1
        while curr:
            if n % 2 == 0:
                even_tail.next = curr
                even_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = curr
            curr = curr.next
            n += 1

        even_tail.next = None
        odd_tail.next = even.next
        return odd.next
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        expected = [1, 3, 5, 2, 4]
        result = Solution().oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_case_2(self):
        head = list_to_linked_list([1, 2, 3, 4])
        expected = [1, 3, 2, 4]
        result = Solution().oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_case_3(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7])
        expected = [1, 3, 5, 7, 2, 4, 6]
        result = Solution().oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_case_4(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6])
        expected = [1, 3, 5, 2, 4, 6]
        result = Solution().oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_case_5(self):
        head = list_to_linked_list([2, 1, 3, 5, 6, 4, 7])
        expected = [2, 3, 6, 7, 1, 5, 4]
        result = Solution().oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
