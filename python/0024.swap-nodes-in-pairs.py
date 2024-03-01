#  Category: algorithms
#  Level: Medium
#  Percent: 63.79193%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
#
#  Example 1:
#
#  Input: head = [1,2,3,4]
#  Output: [2,1,4,3]
#
#
#  Example 2:
#
#  Input: head = []
#  Output: []
#
#
#  Example 3:
#
#  Input: head = [1]
#  Output: [1]
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the list is in the range [0, 100].
#  	0 <= Node.val <= 100
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=head)
        prev = dummy
        while True:
            if not prev.next or not prev.next.next:
                break
            first = prev.next
            second = prev.next.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
        return dummy.next

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        head = list_to_linked_list([1, 2, 3, 4])
        expected = [2, 1, 4, 3]
        result = Solution().swapPairs(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_case_2(self):
        head = list_to_linked_list([])
        expected = []
        result = Solution().swapPairs(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_case_3(self):
        head = list_to_linked_list([1])
        expected = [1]
        result = Solution().swapPairs(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_case_4(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        expected = [2, 1, 4, 3, 5]
        result = Solution().swapPairs(head)
        self.assertEqual(linked_list_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
