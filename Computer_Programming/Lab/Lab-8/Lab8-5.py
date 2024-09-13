def LCS(s1,s2):
    return_val = []
    temp = ""
    for i in range(len(s1)):
        if s1[i] in s2:
           temp = s1[i]
        else:
            continue
        j = 1
        while True:
            if i + j >= len(s1):
                break
            if temp + s1[i + j] in s2:
                temp += s1[i + j]
            else:
                break
            j += 1
        return_val.append(temp)
    if len(return_val) == 0:
        return "''"
    else:
        return max(return_val, key=len)
        
           
print(LCS("ingenious","intelligent"))
print(LCS("philosophically","zoophilous"))
print(LCS("Love","War"))
print(LCS("Condition","Fictional"))
print(LCS("smart","meter"))
print(LCS("back-end","front-end"))