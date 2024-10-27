def count_operands(x:tuple):
    return count_operands_helper(x)
def count_operands_helper(x:tuple,counter = 0):
    if len(x) == 0:
        return counter
    else:
        lot = list(x)
        y = lot.pop()
        if type(y) == int:
            counter += 1
        elif type(y) == tuple:
            counter = count_operands_helper(y,counter)
        return count_operands_helper(tuple(lot),counter)
print(count_operands((((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4)))))
