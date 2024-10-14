def list_member(meow:int,nyah:list):
    if len(nyah) == 0:
        return False
    elif meow == nyah[0]:
        return True
    else:
        nyah.pop(0)
        return list_member(meow,nyah)
print(list_member(2,[1,3,4,5]))
