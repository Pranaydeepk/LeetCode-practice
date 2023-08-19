def reverseList(curr,prev = None):
    if curr == None:
        return prev

    next = curr.next
    curr.next = prev

    return reverseList(next,curr)