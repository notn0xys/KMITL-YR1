def find_word_pos(s:str,L:list):
    return_list = []
    for i in range(len(L)):
        if s.lower == L[i].lower():
            return_list.append(i)
    if len(return_list) == 0:
        return 0
    else:
        return return_list
