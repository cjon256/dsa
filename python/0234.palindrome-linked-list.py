#  Category: algorithms
#  Level: Easy
#  Percent: 51.542915%
#
#
#  Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#
#
#  Example 1:
#
#  Input: head = [1,2,2,1]
#  Output: true
#
#
#  Example 2:
#
#  Input: head = [1,2]
#  Output: false
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the list is in the range [1, 10⁵].
#  	0 <= Node.val <= 9
#
#
#
#  Follow up: Could you do it in O(n) time and O(1) space?
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import unittest
from typing import Optional

from conversions import ListNode, list_to_linked_list


#  start_marker
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_linked_list(node):
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev

        # find middle of the list
        list_is_of_odd_length = False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            list_is_of_odd_length = True
        else:
            list_is_of_odd_length = False

        second_head = slow
        # reverse the first half
        prev = None
        current = head
        while current != second_head:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        # drop the middle node if the list is of odd length
        if list_is_of_odd_length:
            second_head = second_head.next

        # compare the two halves
        while head and second_head:
            if head.val != second_head.val:
                return False
            head = head.next
            second_head = second_head.next
        return True


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        head = list_to_linked_list([1, 2, 2, 1])
        expected_output = True
        result = Solution().isPalindrome(head)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        head = list_to_linked_list([1, 2])
        expected_output = False
        result = Solution().isPalindrome(head)
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        head = list_to_linked_list([1, 2, 3, 2, 1])
        expected_output = True
        result = Solution().isPalindrome(head)
        self.assertEqual(result, expected_output)

    def test_case_4(self):
        head = list_to_linked_list([1])
        expected_output = True
        result = Solution().isPalindrome(head)
        self.assertEqual(result, expected_output)

    def test_case_5(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        expected_output = False
        result = Solution().isPalindrome(head)
        self.assertEqual(result, expected_output)

    def test_case_6(self):
        head = list_to_linked_list(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 8, 7, 6, 5, 4, 3, 2, 1]
        )
        expected_output = False
        result = Solution().isPalindrome(head)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
