def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    Given a string, find the length of the longest substring without repeating characters.

    >>> "abcabcbb"
    3

    >>> "bbbbb"
    1
    
    """

    anag = set()
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            anag.add(s[i:j+1])
    
    longest = 0
    for a in list(anag):
        unique_num = len(set(a))
        if unique_num == len(a):
            if len(a) > longest:
                longest = len(a)
                
    return longest


    
def lengthOfLongestSubstring(self, s):

    dic, start, res = {}, 0, 0

    for i, ch in enumerate(s):
        if ch in dic:
            res = max(res, i - start)
            start = max(start, dic[ch] + 1)
        dic[ch] = i
    
    return max(res, len(s) - start)