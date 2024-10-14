def list_reverse(x:list,stop = 0):
    if stop >= len(x)/2:
        return x
    else:
        l = x[0 + stop] 
        k = x[len(x) - 1 - stop]
        x[0 + stop] = k
        x[len(x) - 1 - stop] = l
        stop += 1
        return(list_reverse(x,stop))
print(list_reverse([1,2,3,4]))