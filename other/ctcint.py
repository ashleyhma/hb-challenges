def is_unique(words):
    """Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?"""

    new_str = ''

    for ch in words:
        if ch not in new_str:
            new_str += ch
    
    if len(new_str) < len(words):
        return False
    return True

def check_permutation(str1, str2):
    """Given two strings,write a method to decide if one is a permutation of the
    other."""
    
    sorted1 = sorted(str1)
    sorted2 = sorted(str2)

    for idx, ch in enumerate(str1):
        if sorted1[idx] != sorted2[idx]:
            return False
    
    return True


def urlify(s, num):
    """"Write a method to replace all spaces in a string with '%20  You may assume that the string has suf cient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)"""
    
    new_s = ''

    for ch in s:
        if ch == " ":
            new_s += "%20"
        else:
            new_s += ch

    if len(s) != num:
        new_s += ("%20" * (num-len(s)))

    return new_s

def palindrome_permutation(s):
    """ Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same  rwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words."""
    ch_count = {}

    for ch in s:
        if ch not in ch_count:
            ch_count[ch] = 1
        else:
            ch_count[ch] += 1
    
    count = 0
    for num in ch_count.values():
        if num % 2 != 0:
            count += 1
    
    if count > 1:
        return False
    return True


def one_away(s):
    """There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away."""

    

