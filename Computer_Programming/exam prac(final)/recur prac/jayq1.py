def count_unique(l:list,count = 0, tracker = []):
    if len(l) == 0:
        return count
    else:
        x = l.pop()
        if type(x) == int and x not in tracker:
            count += 1
            tracker.append(x)
        elif type(x) == list:
            count = count_unique(x,count,tracker)
        return count_unique(l,count,tracker)
print(count_unique([1, 2, 3, [4, 5], [1, 2]]))