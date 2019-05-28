class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    

def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool

    Given a singly linked list, determine if it is a palindrome.
    """
    
    nums = []
    cur = head
    
    while cur != None:
        nums.append(cur.val)
        cur = cur.next
    return nums == nums[::-1]