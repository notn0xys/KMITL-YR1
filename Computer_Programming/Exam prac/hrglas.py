i = 0
n = 6
row = 0
while i < n:
    print(" " * i, end="")
    if row % 2 == 0:
        print("*" * (((n - i) * 2) - 1))
    else:
        print("#" * (((n - i) * 2) - 1))
    row += 1
    i += 1
i = 1
while i < n:
    print(" " * (n-(i + 1)), end="")
    if row % 2 == 0:
        print("*" * (((i + 1) * 2) - 1))
    else: 
        print("#" * (((i + 1) * 2) - 1))
    i += 1
    row += 1
