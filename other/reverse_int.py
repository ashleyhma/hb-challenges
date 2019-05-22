def reverse(x):
    """
    Given a 32-bit signed integer, reverse digits of an integer.
    >>> 123
    321

    >>> -123
    -321
    """
    res = ''
    
    if str(x)[0] == "-":
        res += '-'
        rest = str(x)[:0:-1]
        res += rest
    else:
        rest = str(x)[::-1]
        res += rest
    
    if abs(int(res)) >= (2**31):
        return 0
    else:
        return int(res)

