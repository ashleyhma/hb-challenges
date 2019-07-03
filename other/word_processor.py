def word_processor(phrase):
    words = phrase.split()
    count = 0
    
    line = ''
    for word in words:
        count += len(word)
        
        if count <= 10:
            line += word + ' '
            count += 1
        elif count == 11:
            line += word
        else:
            print(line)
            count = len(word) + 1
            line = word + ' '
    print(line)