def sum_of_digits(n:int):
    try:
        x = str(n)
        return int(x[-1]) + sum_of_digits(int(x[:-1]))
    except:
        return 0
print(sum_of_digits(123))
