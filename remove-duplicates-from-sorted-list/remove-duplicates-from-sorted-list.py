# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

\
        prev = head
        curr = head.next

        while curr is not None:
            if curr.val == prev.val:
                prev.next = curr.next
                curr = prev.next
                continue
            prev = curr
            curr = curr.next                

        return head
