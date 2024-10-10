def find_dupe(x:dict):
    store = {}
    dupe_list = []
    return_dict = {}
    for i in x.values():
        if i not in store:
            store[i] = 1
        else:
            store[i] += 1
    for i in store:
        if store[i] > 1:
            dupe_list.append(i)
    for i in x:
        if x[i] in dupe_list:
            return_dict[i] = x[i]
    return return_dict
my_dict = {'s5301':"Fred",'s5302':"Fred",'s5303':"Jom",'s5304':"Harry",'s5305':"Harry"}
print(find_dupe(my_dict))
