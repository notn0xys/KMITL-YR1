def inverse(x:dict):
    return_dict = dict()
    for key , val in x.items():
        if val not in return_dict.keys():
            return_dict[val] = set(key)
        else:
            return_dict[val].add(key)
    return return_dict
dict1 = {'a' : 1,'b' : 2,'c' : 1,'d' : 3,'e' : 1,'f' : 2}
print(inverse(dict1))