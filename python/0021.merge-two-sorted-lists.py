#  Category: algorithms
#  Level: Easy
#  Percent: 63.77107%
import unittest
from typing import Optional

from leetopenlib.linked_list import ListNode, linked_list_to_list, list_to_linked_list

#  You are given the heads of two sorted linked lists list1 and list2.
#
#  Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
#  Return the head of the merged linked list.
#
#
#  Example 1:
#
#  Input: list1 = [1,2,4], list2 = [1,3,4]
#  Output: [1,1,2,3,4,4]
#
#
#  Example 2:
#
#  Input: list1 = [], list2 = []
#  Output: []
#
#
#  Example 3:
#
#  Input: list1 = [], list2 = [0]
#  Output: [0]
#
#
#
#  Constraints:
#
#
#  	The number of nodes in both lists is in the range [0, 50].
#  	-100 <= Node.val <= 100
#  	Both list1 and list2 are sorted in non-decreasing order.
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#  start_marker
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list2.val < list1.val:
            head = list2
            curr1 = list1
            curr2 = list2.next
        else:
            head = list1
            curr1 = list1.next
            curr2 = list2
        curr_addpoint = head
        while True:
            if curr1 is None:
                curr_addpoint.next = curr2
                break
            if curr2 is None:
                curr_addpoint.next = curr1
                break
            if curr2.val < curr1.val:
                curr_addpoint.next = curr2
                curr2 = curr2.next
                curr_addpoint = curr_addpoint.next
            else:
                curr_addpoint.next = curr1
                curr1 = curr1.next
                curr_addpoint = curr_addpoint.next
        return head


#  end_marker
class TestSolution(unittest.TestCase):
    def test_0(self):
        list1 = [1, 2, 4]
        list2 = [1, 3, 4]
        expected = [1, 1, 2, 3, 4, 4]
        list1 = list_to_linked_list(list1)
        list2 = list_to_linked_list(list2)
        actual = Solution().mergeTwoLists(list1, list2)
        actual = linked_list_to_list(actual)
        self.assertEqual(expected, actual)

    def test_1(self):
        list1 = []
        list2 = []
        expected = []
        list1 = list_to_linked_list(list1)
        list2 = list_to_linked_list(list2)
        actual = Solution().mergeTwoLists(list1, list2)
        actual = linked_list_to_list(actual)
        self.assertEqual(expected, actual)

    def test_2(self):
        list1 = []
        list2 = [0]
        expected = [0]
        list1 = list_to_linked_list(list1)
        list2 = list_to_linked_list(list2)
        actual = Solution().mergeTwoLists(list1, list2)
        actual = linked_list_to_list(actual)
        self.assertEqual(expected, actual)

    def test_3(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        expected = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        list1 = list_to_linked_list(list1)
        list2 = list_to_linked_list(list2)
        actual = Solution().mergeTwoLists(list1, list2)
        actual = linked_list_to_list(actual)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
