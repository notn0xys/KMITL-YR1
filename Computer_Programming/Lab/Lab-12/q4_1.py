def is_subset(s:set,s2:set):
    is_sub = True
    for i in s:
        if i not in s2:
            is_sub = False
            break
    return is_sub
sup = set([1,2,3,4])
sub = set([1,2,3])
meow = set([1,2,5])
print(is_subset(sub,sup))
print(is_subset(meow,sup))