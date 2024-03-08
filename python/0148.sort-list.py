#  Category: algorithms
#  Level: Medium
#  Percent: 57.5%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Given the head of a linked list, return the list after sorting it in ascending order.
#
#
#
# Example 1:
#
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
# Example 2:
#
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
# Example 3:
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#     The number of nodes in the list is in the range [0, 5 * 104].
#     -105 <= Node.val <= 105
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
