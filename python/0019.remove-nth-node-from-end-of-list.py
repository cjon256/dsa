# Definition for singly-linked list.
from dataclasses import dataclass
from typing import Optional, List, Any, Self
import unittest


@dataclass
class ListNode:
    val: int = 0
    next: Optional[Self] = None


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        if head is None:
            return None
        if head.next is None and n == 1:
            return None
        curr = head
        for _ in range(n):
            print(f"curr: {curr.val}")
            print("----------------------")
            curr = curr.next
        if curr is None:
            return head.next
        print(f"head: {head.val} curr: {curr.val}")
        print("----------------------")
        print("----------------------")
        curr_minus_n = head
        while curr.next:
            print(f"curr_minus_n: {curr_minus_n.val} ... curr: {curr.val}")
            print("----------------------")
            curr = curr.next
            curr_minus_n = curr_minus_n.next
        print(f"done: curr_minus_n: {curr_minus_n.val} ... curr: {curr.val}")
        curr_minus_n.next = curr_minus_n.next.next
        return head


def constructTreeTestAndReturnList(nums: List[Any], n: int) -> List[Any]:
    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next
    head = Solution().removeNthFromEnd(head, n)
    print(f"head after: {head}")
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


class TestSolution:  # (unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_1(self) -> None:
        # Input: head = [1,2,3,4,5], n = 2
        # Output: [1,2,3,5]
        nums = [1, 2, 3, 4, 5]
        n = 2
        print("==================================")
        print(f"running test_1: {nums}, {n}")
        print("==================================")
        # self.assertEqual(constructTreeTestAndReturnList(nums, n), [1, 2, 3, 5])
        nums = constructTreeTestAndReturnList(nums, n)
        print(nums)

    def test_2(self) -> None:
        # Input: head = [1], n = 1
        # Output: []
        nums = [1]
        n = 1
        print("==================================")
        print(f"running test_2: {nums}, {n}")
        print("==================================")
        # self.assertEqual(constructTreeTestAndReturnList(nums, n), [])
        nums = constructTreeTestAndReturnList(nums, n)
        print(nums)

    def test_3(self) -> None:
        # Input: head = [1,2], n = 1
        # Output: [1]
        nums = [1, 2]
        n = 2
        print("==================================")
        print(f"running test_3: {nums}, {n}")
        print("==================================")
        # self.assertEqual(constructTreeTestAndReturnList(nums, n), [2])
        nums = constructTreeTestAndReturnList(nums, n)
        print(nums)


if __name__ == '__main__':
    # unittest.main()
    ts = TestSolution()
    ts.test_1()
    ts.test_2()
    ts.test_3()
