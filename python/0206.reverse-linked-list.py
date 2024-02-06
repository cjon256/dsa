# pylint: disable=invalid-name, missing-class-docstring, missing-function-docstring, missing-module-docstring
# pylint: disable=too-few-public-methods
import unittest
from dataclasses import dataclass
from typing import Optional, Self

from leetopenlib.linked_list import linked_list_to_list, list_to_linked_list


@dataclass
class ListNode:
    val: int
    next: Optional[Self] = None


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
