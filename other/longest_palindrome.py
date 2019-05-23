def longestPalindrome(self, s):
    """
    Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

    This is case sensitive, for example "Aa" is not considered a palindrome here.
    """

    count = {}
    
    for ch in s:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] += 1
    
    counts = 0
    for x in count.values():
        if x % 2 != 0:
            counts += 1 
            
    if counts == 0:
        return len(s)
    else:
        return len(s) - counts + 1