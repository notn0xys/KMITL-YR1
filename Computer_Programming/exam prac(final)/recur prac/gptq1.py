def sum_of_nested(nested,acc = 0):
    if len(nested) == 0:
        return acc
    else:
        x = nested.pop()
        if type(x) == list:
            acc = sum_of_nested(x,acc)
        else:
            acc += x
        return sum_of_nested(nested,acc)
nested_list = [1, [2, 3], [[4], 5], 6]
print(sum_of_nested(nested_list))