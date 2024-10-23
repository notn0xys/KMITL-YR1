def count_operands(x:tuple,count = 0,tracker = []):
    if len(x) == 0:
        return count
    else:
        lot = list(x)
        y = lot.pop()
        if type(y) == int and y not in tracker:
            tracker.append(y)
            count += 1
        elif type(y) == tuple:
            count =  count_operands(y,count,tracker)
        return count_operands(tuple(lot),count,tracker)
print(count_operands((3, '/',3)))
