def my_union(l1:list,l2:list) -> list:
    l3 = l1 + l2
    l4 = []
    for i in l3:
        if i not in l4:
            l4.append(i)
        else:
            continue
    return l4
def my_intersec(l1:list,l2:list) -> list:
    l3 = [i for i in l1 if i in l2]
    return l3
def my_diff(l1:list,l2:list) -> list:
    l3 = [i for i in l1 if i not in l2]
    return l3
list1 = [3,1,2,4,7]
list2 = [4,1,2,5,7]
print(my_union(list1,list2))
print(my_intersec(list1,list2))
print(my_diff(list1,list2))
