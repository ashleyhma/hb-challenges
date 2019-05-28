"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""
    counter = {}
    result = set()
    max = None

    for num in nums:
        if num not in counter:
            counter[num] = 1 
        else:
            counter[num] += 1 
    
    for v in counter.values():
        if max is None or v > max:
            max = v
    
    for k, v in counter.items():
        if v == max:
            result.add(k)
            
    return result



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
