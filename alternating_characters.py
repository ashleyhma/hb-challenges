def alternatingCharacters(s):
    """Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.

    alternatingCharacters has the following parameter(s):

    s: a string"""
    
    count = 0

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1 
    
    return count