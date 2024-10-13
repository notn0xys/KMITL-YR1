def powerset(s:set):
    return_set = {frozenset({})}
    meow = set()
    for i in s:
        return_set.add(frozenset({i}))
        meow.add(i)
    return_set.add(frozenset(meow))
    try:
        for k in s:
            for i in range(len(s) - 2):
                
                nyah = s.copy()
                nyah.remove(k)
                return_set.add(frozenset(nyah))           
    except:
        pass
    return return_set
print(powerset({1,2,3}))
        


