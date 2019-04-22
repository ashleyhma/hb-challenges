def possible_passwords(corrupted, possible):
    result = []

    letter_dict = {}
    for idx, ch in enumerate(corrupted):
        if ch.isalpha():
            letter_dict[idx] = ch 

    poss_str = ''
    for word in possible:
        if len(corrupted) == len(word):
            for idx, ch in enumerate(word):
                if idx not in letter_dict:
                    poss_str += ch 
                if idx in letter_dict:
                    if ch == letter_dict[idx]:
                        poss_str += ch
            if len(poss_str) == len(corrupted):
                result.append(word)
            poss_str = ''
    
    return result

possible_passwords('_w_l_o', ['twilio', 'awelto', 'ashley', 'cat', '@3$,p', '#w8,to', '9w3l4o'])



# def possible_passwords(corrupted, possible):
#     result = []

#     letter_dict = {}
#     for idx, ch in enumerate(corrupted):
#         if ch.isalpha():
#             letter_dict[idx] = ch 


#     for word in possible:
#         print('word', word)
#         if len(corrupted) == len(word):
#             for idx, ch in enumerate(word):
#                 if idx in letter_dict:
#                     if ch == letter_dict[idx]:
#                         print('continue', ch)
#                         if idx == (len(word)-1):
#                             result.append(word)
#                         continue
#                     else:
#                         print('break', ch)
#                         break
  
#     return result
