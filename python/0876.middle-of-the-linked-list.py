#  Category: algorithms
#  Level: Easy
#  Percent: 77.092995%

# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods
import unittest
from typing import Optional, Self

from leetopenlib.linked_list import ListNode, linked_list_to_list, list_to_linked_list

#  Given the head of a singly linked list, return the middle node of the linked list.
#
#  If there are two middle nodes, return the second middle node.
#
#
#  Example 1:
#
#  Input: head = [1,2,3,4,5]
#  Output: [3,4,5]
#  Explanation: The middle node of the list is node 3.
#
#
#  Example 2:
#
#  Input: head = [1,2,3,4,5,6]
#  Output: [4,5,6]
#  Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#
#
#
#  Constraints:
#
#
#  	The number of nodes in the list is in the range [1, 100].
#  	1 <= Node.val <= 100
#


#  start_marker
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            print(f"before fast: {fast.val}, slow: {slow.val}")
            fast = fast.next.next
            slow = slow.next
        if fast:
            return slow.next
        return slow


#  end_marker
class TestSolution(unittest.TestCase):
    def test_0(self):
        head = list_to_linked_list([])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [])

    def test_1(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [3, 4, 5])

    def test_2(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [4, 5, 6])

    def test_3(self):
        head = list_to_linked_list([1])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [1])

    def test_4(self):
        head = list_to_linked_list([1, 2])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [2])

    def test_5(self):
        head = list_to_linked_list([1, 2, 3])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [2, 3])

    def test_6(self):
        head = list_to_linked_list([1, 2, 3, 4])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [3, 4])

    def test_7(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [4, 5, 6, 7])

    def test_8(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [5, 6, 7, 8])

    def test_9(self):
        head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        output = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(output), [5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
