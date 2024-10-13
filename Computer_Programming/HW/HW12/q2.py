def composit(x:dict,y:dict):
    return_dict = {}
    for nyan,meow in x.items():
        for nyah , muah in y.items():
            if meow == nyah:
                return_dict[nyan] = muah
    return return_dict
dict1 = {'a': "p",'b': "r",'c': "q",'d': "p",'e': "n",}
dict2 = {'p': "1",'q': "2",'r': "3"}
print(composit(dict1,dict2))