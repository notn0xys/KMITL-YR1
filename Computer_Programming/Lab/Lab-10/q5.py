def merge(l1:list,l2:list):
    list3 = l1 + l2
    l4= []
    for i in range(len(list3)):
        a = min(list3)
        list3.remove(a)
        l4.append(a)
    return l4
x = merge([2,3,4,5,1,2,1222,3,2,3,2,321,213,213,13123213,3213123,6,8,9,75,5,343], [6,4,5,6,77,89,5])
print(x)