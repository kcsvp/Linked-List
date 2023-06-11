# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1)

        curr = head

        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            else:
                curr.next = ListNode(list1.val)
                list1 = list1.next

            curr = curr.next

        while list1 is not None:
            curr.next = ListNode(list1.val)
            list1 = list1.next
            curr = curr.next

        while list2 is not None:
            curr.next = ListNode(list2.val)
            list2 = list2.next
            curr = curr.next

        return head.next

        





        

        