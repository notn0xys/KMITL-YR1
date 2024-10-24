def find_common(list1,list2):
    return_list = []
    for i in list1:
        if i in list2 and i not in return_list:
            return_list.append(i)
    return return_list
print(find_common([1, 2, 3, 4], [9, 8, 5, 6]))