# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        if curr != None:
            n = 1
        while curr.next != None:
            n += 1
            curr = curr.next
        fast = head # for k from end (n-k)
        slow = head # for k from head (k-1)
        while n-k > 0:
            fast = fast.next
            n -= 1
        while k-1 > 0:
            slow = slow.next
            k -= 1
        fast.val, slow.val = slow.val, fast.val
        return head