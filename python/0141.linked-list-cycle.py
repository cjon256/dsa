#  Category: algorithms
#  Level: Easy
#  Percent: 49.341053%


#  Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
#  There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
#  Return true if there is a cycle in the linked list. Otherwise, return false.
#
#
#  Example 1:
#
#  Input: head = [3,2,0,-4], pos = 1
#  Output: true
#  Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#
#
#  Example 2:
#
#  Input: head = [1,2], pos = 0
#  Output: true
#  Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
#
#
#  Example 3:
#
#  Input: head = [1], pos = -1
#  Output: false
#  Explanation: There is no cycle in the linked list.
#
#
#
#  Constraints:
#
#
#  	The number of the nodes in the list is in the range [0, 10⁴].
#  	-10⁵ <= Node.val <= 10⁵
#  	pos is -1 or a valid index in the linked-list.
#
#
#
#  Follow up: Can you solve it using O(1) (i.e. constant) memory?
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


import unittest
from typing import Optional

from conversions import ListNode, list_to_linked_list


def list_to_looped_linked_list(nums, pos):
    head = list_to_linked_list(nums)
    if pos == -1:
        return head
    tail = head
    for i in range(pos):
        tail = tail.next
    node = head
    while node.next:
        node = node.next
    node.next = tail
    return head


#  start_marker


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast or slow == fast.next:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

    def hasCycle_hash(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        node_dict = {}
        curr = head
        while curr is not None:
            if curr.val in node_dict:
                if curr in node_dict[curr.val]:
                    return True
                else:
                    node_dict[curr.val].append(curr)
            else:
                node_dict[curr.val] = [curr]
            curr = curr.next
        return False


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        vals = [3, 2, 0, -4]
        pos = 1
        head = list_to_looped_linked_list(vals, pos)
        expected_result = True
        self.assertEqual(Solution().hasCycle(head), expected_result)

    def test_case_2(self):
        vals = [1, 2]
        pos = 0
        head = list_to_looped_linked_list(vals, pos)
        expected_result = True
        self.assertEqual(Solution().hasCycle(head), expected_result)

    def test_case_3(self):
        vals = [1]
        pos = -1
        head = list_to_looped_linked_list(vals, pos)
        expected_result = False
        self.assertEqual(Solution().hasCycle(head), expected_result)

    def test_case_4(self):
        head = ListNode(1)
        self.assertEqual(False, Solution().hasCycle(head))

    def test_case_5(self):
        head = None
        self.assertEqual(False, Solution().hasCycle(head))

    # description says nothing about node values being unique
    def test_case_6(self):
        vals = [1, 1, 2]
        pos = 0
        head = list_to_looped_linked_list(vals, pos)
        self.assertEqual(True, Solution().hasCycle(head))


if __name__ == "__main__":
    unittest.main()
