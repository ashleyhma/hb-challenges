def add_linked_lists(l1, l2): 
    head = None 
    tail = None 
    c1 = l1 
    c2 = l2 
    while c1 is not None and c2 is not None: 
        sum = 0 
        sum += c1.data  
        sum += c2.data 
        n = Node(sum) 
        if head is None and tail is None: 
            head = n 
            tail = n 
        elif tail is not None: 
            tail.next = n 
            tail = n
        c1 = c1.next
        c2 = c2.next 