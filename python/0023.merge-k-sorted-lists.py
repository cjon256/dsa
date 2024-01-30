#  Category: algorithms
#  Level: Hard
#  Percent: 51.878803%


#  You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
#  Merge all the linked-lists into one sorted linked-list and return it.
#
#
#  Example 1:
#
#  Input: lists = [[1,4,5],[1,3,4],[2,6]]
#  Output: [1,1,2,3,4,4,5,6]
#  Explanation: The linked-lists are:
#  [
#    1->4->5,
#    1->3->4,
#    2->6
#  ]
#  merging them into one sorted list:
#  1->1->2->3->4->4->5->6
#
#
#  Example 2:
#
#  Input: lists = []
#  Output: []
#
#
#  Example 3:
#
#  Input: lists = [[]]
#  Output: []
#
#
#
#  Constraints:
#
#
#  	k == lists.length
#  	0 <= k <= 10⁴
#  	0 <= lists[i].length <= 500
#  	-10⁴ <= lists[i][j] <= 10⁴
#  	lists[i] is sorted in ascending order.
#  	The sum of lists[i].length will not exceed 10⁴.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import unittest
from typing import List, Optional

from conversions import ListNode, linked_list_to_list, list_to_linked_list


#  start_marker
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def get_index_of_min(lists):
            min_index = 0
            for i in range(1, len(lists)):
                if not lists[i]:
                    continue
                if lists[i].val < lists[min_index].val:
                    min_index = i
            return min_index

        currs = [e for e in lists if e]
        head = ListNode(None)
        curr = head
        while currs:
            min_index = get_index_of_min(currs)
            curr.next = ListNode(currs[min_index].val)
            currs[min_index] = currs[min_index].next
            if not currs[min_index]:
                del currs[min_index]
            curr = curr.next
        return head.next


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        lists = [
            list_to_linked_list([1, 4, 5]),
            list_to_linked_list([1, 3, 4]),
            list_to_linked_list([2, 6]),
        ]
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_case_2(self):
        lists = []
        expected = []
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_case_3(self):
        lists = [[]]
        expected = []
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_case_4(self):
        lists = [None]
        expected = []
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_case_5(self):
        lists = [list_to_linked_list([1])]
        expected = [1]
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_case_6(self):
        lists = [list_to_linked_list([1]), list_to_linked_list([0])]
        expected = [0, 1]
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_case_7(self):
        lists = [list_to_linked_list([1]), list_to_linked_list([0, 2])]
        expected = [0, 1, 2]
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_case_8(self):
        lists = [
            list_to_linked_list([1]),
            list_to_linked_list([0, 2]),
            list_to_linked_list([3]),
        ]
        expected = [0, 1, 2, 3]
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_case_9(self):
        lists = [
            list_to_linked_list([1]),
            list_to_linked_list([0, 2]),
            list_to_linked_list([3]),
            list_to_linked_list([4]),
        ]
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_case_10(self):
        lists = [
            list_to_linked_list([1]),
            list_to_linked_list([0, 2]),
            list_to_linked_list([3]),
            list_to_linked_list([4]),
            list_to_linked_list([5]),
        ]
        expected = [0, 1, 2, 3, 4, 5]
        self.assertEqual(linked_list_to_list(Solution().mergeKLists(lists)), expected)


if __name__ == "__main__":
    unittest.main()
