def checkMagazine(magazine, note):
    """Complete the checkMagazine function in the editor below. It must print  if the note can be formed using the magazine, or .

    checkMagazine has the following parameters:

    magazine: an array of strings, each a word in the magazine
    note: an array of strings, each a word in the ransom note"""
    
    words = {}

    for word in magazine:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
            
    result = []
    for w in note:
        if w in words:
            if words[w] != 0:
                words[w] -= 1
                result.append(w)
            else:
                break
        else:
            break
    
    if len(note) == len(result):
        print("Yes")
    else:
        print("No")