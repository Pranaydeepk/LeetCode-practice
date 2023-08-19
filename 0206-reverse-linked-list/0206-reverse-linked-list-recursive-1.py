def reverseList(head):
    if head == None:
        return head

    if head.next == None:
        return head

    rest_head = reverseList(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None

    return rest_head