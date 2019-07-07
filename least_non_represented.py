def least_non_represented(a):
    """ Write a function that prints the least integer that is not present in a given list and cannot be represented by the summation of the sub-elements of the list.

    E.g. For a = [1,2,5,7] the least integer not represented by the list or a slice of the list is 4, and if a = [1,2,2,5,7] then the least non-representable integer is 18. """

    pos_sums = []

    for i in range(len(a)):
        for j in range(i, len(a)):
            if i != j:
                pos_sums.append(a[i]+a[j])
    
    
    pos_sums.extend(a)
    b = list(set(pos_sums))
    b.sort()

    for i in range(1, b[-1]):
        if i not in b:
            return i 