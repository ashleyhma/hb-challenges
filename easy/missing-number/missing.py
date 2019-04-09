"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """

    #O(n)
    # sum = 0
    # for i in range(max_num+1):
    #     sum += i 

    # array_sum = 0
    # for num in nums:
    #     array_sum += num

    # return sum - array_sum

    #############################
    num_lst = set(nums)

    for i in range(1, max_num+1):
        if i not in num_lst:
            return i
    
    



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
