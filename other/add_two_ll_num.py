class ListNode(object):
    def __init__(self, x, y=None):
        self.val = x
        self.next = y

class Solution(object):
    """You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list."""
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lst1 = []
        lst2 = []
        
        c1 = l1
        c2 = l2
        
        while c1:
            lst1.append(str(c1.val))
            c1 = c1.next
        
        while c2:
            lst2.append(str(c2.val))
            c2 = c2.next
        
        num1 = int(''.join(lst1[::-1]))
        num2 = int(''.join(lst2[::-1]))
        summ = str(num1+num2)
        print(num1 + num2)
        
        return self.list_to_link(summ)
            
    def list_to_link(self, lst):
        if len(lst) == 1:
            return ListNode(lst[-1])
        return ListNode(lst[-1], self.list_to_link(lst[:-1]))