def reverse(list_of_chars):

    # Reverse the input list of chars in place


    i = 0 
    while i < len(list_of_chars) // 2:
        list_of_chars[i], list_of_chars[-1-i] = list_of_chars[-1-i], list_of_chars[i]
        i += 1 
    return list_of_chars