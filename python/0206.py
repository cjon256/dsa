# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList_r(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_r(prev: ListNode, curr: ListNode) -> ListNode:
            if curr is None:
                return prev
            curr_next = curr.next
            curr.next = prev
            return reverse_list_r(curr, curr_next)
        
        if head is None:
            return head
        child = head.next
        if child is None:
            return head
        head.next = None
        child_next = child.next
        child.next = head
        return reverse_list_r(child, child_next)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            child = curr.next
            curr.next = prev
            prev = curr
            curr = child
        return prev
        