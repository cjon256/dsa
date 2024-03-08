#  Category: algorithms
#  Level: Medium
#  Percent: 37.5%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Given the head of a linked list, rotate the list to the right by k places.
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
# Example 2:
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
#
# Constraints:
#
#     The number of nodes in the list is in the range [0, 500].
#     -100 <= Node.val <= 100
#     0 <= k <= 2 * 109
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
