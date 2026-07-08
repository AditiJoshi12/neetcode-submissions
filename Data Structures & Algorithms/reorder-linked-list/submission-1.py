# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 

        # now slow is at the midpoint
        # we need to reverse slow 

        prev, curr = None, slow.next
        slow.next = None

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # now slow is reversed and we need to interleave head and slow

        first, second = head, prev

        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next

        