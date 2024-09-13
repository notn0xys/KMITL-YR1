height = 5
for i in range(5):
    print(" " *i, end="")
    print("*" * ((5 - i) * 2 - 1))
for i in range(1,5):
    print(" " * (5 - (i+1)) ,end="")
    print("*" * ((i + 1) * 2 - 1))