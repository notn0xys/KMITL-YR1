def count_operands(x:tuple,count = 0):
    if len(x) == 0:
        return count
    else:
        lot = list(x)
        y = lot.pop()
        if type(y) == int:
            count += 1
        elif type(y) == tuple:
            count =  count_operands(y,count)
        return count_operands(tuple(lot),count)
print(count_operands( ((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4)) ))