def get_diff(l1:list,l2:list) -> list:
    l1 = list(set(l1))
    l2 = list(set(l2))
    l3 = []
    for i in l1:
        if i not in l2:
            l3.append(i)
    for i in l2:
        if i not in l1:
            l3.append(i)
    return list(set(l3))
x = get_diff([3,1,1,1,2,7],[4,1,1,2,2,5])
print(x)