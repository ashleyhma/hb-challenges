"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    alpha = set()

    lower_sent = sentence.lower()

    for ch in lower_sent:
        if ch.isalpha() and (ch not in alpha):
            alpha.add(ch)
    
    if len(alpha) != 26:
        return False
    return True

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
