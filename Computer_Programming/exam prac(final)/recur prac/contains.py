def contains(l:list,x:int,count = 0,index = []):
    if count == len(l):
        return index
    if l[count] == x:
        index.append(count)
    count += 1
    return contains(l,x,count,index)
            
print(contains([1,2,34,5,2,6,2],2))