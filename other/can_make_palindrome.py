def make_palindrome(s):
    """determine whether a given string can be rearranged into a palindrome. If it is possible, return YES, otherwise return NO."""
    
    # chcount = {}
    
    # for ch in s:
    #     if ch not in chcount:
    #         chcount[ch] = 1
    #     else:
    #         chcount[ch] += 1 
    # print(chcount)
    # count = 0
    # for num in chcount.values():
    #     count += num % 2
    # print(count)
    # if count > 1:
    #     return "NO"
    # else:
    #     return "YES"

    letters = set() 

    for ch in s:
        if ch not in letters:
            letters.add(ch)
        else:
            letters.remove(ch)

    if len(letters) > 1:
        return "NO"
    else:
        return "YES"