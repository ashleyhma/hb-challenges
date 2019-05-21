def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    curr = head
    prev = None
    
    while curr:
        temp = curr.next
        curr.next = prev
        
        prev = curr
        curr = temp
    return prev