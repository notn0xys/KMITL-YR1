def isAnagram(s1:str,s2:str):
    nyan1 = dict()
    nyan2 = dict()
    for i in s1:
        if i not in nyan1:
            nyan1[i] = 1
        else:
            nyan1[i] += 1
    for i in s2:
        if i not in nyan2:
         nyan2[i] = 1
        else:
         nyan2[i] += 1
    if nyan1 != nyan2:
       return False
    else:
       return True
print(isAnagram("silent","listen"))