import unittest
from dataclasses import dataclass
from typing import Optional, Self


@dataclass
class ListNode:
    val: int
    next: Optional[Self] = None


class Solution:
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

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow_ptr, fast_ptr = head, head.next
        while True:
            if fast_ptr is None or fast_ptr.next is None:
                return False
            if slow_ptr == fast_ptr:
                return True
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

class TestSolution(unittest.TestCase):
    def test1(self):
        end_node = ListNode(-4)
        head = ListNode(3, ListNode(2, ListNode(0, end_node)))
        end_node.next = head.next
        self.assertEqual(True, Solution().hasCycle(head))

    def test2(self):
        end_node = ListNode(2)
        head = ListNode(1, end_node)
        end_node.next = head
        self.assertEqual(True, Solution().hasCycle(head))

    def test3(self):
        head = ListNode(1)
        self.assertEqual(False, Solution().hasCycle(head))

    def test4(self):
        head = None
        self.assertEqual(False, Solution().hasCycle(head))

    # description says nothing about node values being unique
    def test5(self):
        end_node = ListNode(2)
        head = ListNode(1, ListNode(1, end_node))
        end_node.next = head
        self.assertEqual(True, Solution().hasCycle(head))


if __name__ == "__main__":
    unittest.main()
