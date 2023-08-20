# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        count = 1
        curr = head
        while curr.next != None:
            curr = curr.next
            count += 1
        if count == n:
            return head.next
        curr = head
        while count - n > 1:
            curr = curr.next
            count -= 1
        curr.next = curr.next.next
        return head