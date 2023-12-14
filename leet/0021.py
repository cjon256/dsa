# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
