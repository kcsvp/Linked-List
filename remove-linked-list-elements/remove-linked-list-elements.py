# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head:
            curr = head.next
            prev = head
        else:
            return head

        while curr != None:

            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        if head.val == val:
            return head.next
        return head

            

