def count_operands(x:tuple):
    if len(x) == 0:
        return 0
    else:
        count = 0
        lot = list(x)
        y = lot.pop()
        if type(y) == int:
            count = 1
        elif type(y) == tuple:
            count += count_operands(y)
        return count + count_operands(tuple(lot))
print(count_operands((((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4)))))
