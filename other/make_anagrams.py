def makeAnagram(a, b):
    """Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.

    makeAnagram has the following parameter(s):

    a: a string
    b: a string"""

    dic = {}

    for ch in a:
        if ch not in dic:
            dic[ch] = 0
        dic[ch] += 1 
    
    for ch in b:
        if ch not in dic:
            dic[ch] = 0
        dic[ch] -= 1

    result = 0
    for n in dic.values():
        result += abs(n)
    print(dic)
    return result 