#  Category: algorithms
#  Level: Medium
#  Percent: 42.137493%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
#  You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
#  Example 1:
#
#  Input: l1 = [2,4,3], l2 = [5,6,4]
#  Output: [7,0,8]
#  Explanation: 342 + 465 = 807.
#
#
#  Example 2:
#
#  Input: l1 = [0], l2 = [0]
#  Output: [0]
#
#
#  Example 3:
#
#  Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#  Output: [8,9,9,9,0,0,0,1]
#
#
#
#  Constraints:
#
#
#  	The number of nodes in each linked list is in the range [1, 100].
#  	0 <= Node.val <= 9
#  	It is guaranteed that the list represents a number that does not have leading zeros.
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
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        head = curr = ListNode(0)
        while True:
            if not l1 and not l2:
                break
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        expected_result = [7, 0, 8]
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), expected_result)

    def test_case_2(self):
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        expected_result = [0]
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), expected_result)

    def test_case_3(self):
        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([9, 9, 9, 9])
        expected_result = [8, 9, 9, 9, 0, 0, 0, 1]
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), expected_result)

    def test_case_4(self):
        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([1])
        expected_result = [0, 0, 0, 0, 0, 0, 0, 1]
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), expected_result)


if __name__ == "__main__":
    unittest.main()
