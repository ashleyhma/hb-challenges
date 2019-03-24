"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    """
    if len(word) == 1:
        return True
    elif len(word) == 2:
        return False
    
    count = {}
    keys = []

    for ch in word:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] += 1
    
    for k, v in count.items():
        if v != 2:
            keys.append(k)
    
    if len(keys) == 1:
        return True
    
    return False
    """

    seen = {}

    for ch in word:
        count = seen.get(ch, 0)
        seen[ch] = count + 1 
    
    seen_odd = False
    for count in seen.values():
        if count % 2 != 0:
            if seen_odd:
                return False
            seen_odd = True

    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
