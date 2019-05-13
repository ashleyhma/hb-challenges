def sherlockAndAnagrams(s):
    """Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

    For example , the list of all anagrammatic pairs is  at positions respectively."""

    dic = {}

    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings = sorted(list(s[i:j]))
            joined_ss = ''.join(substrings)
            if joined_ss != '':
                if joined_ss in dic:
                    count += dic[joined_ss]
                    dic[joined_ss] += 1
                else:
                    dic[joined_ss] = 1 
    print(dic)
    return count