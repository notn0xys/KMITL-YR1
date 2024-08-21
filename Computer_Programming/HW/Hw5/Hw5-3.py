while True:
    n = input("Enter an integer that is greater than or equal to 1: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
        print("More than 0")
    else:
        print("Enter a positive int")
print(f"Input: {n}")
print("")
for i in range(n):
    l = n - i
    if i == 0 or i == n - 1:
        for i in range(l):
            print("*" * (i + 1))
        for i in range(l - 1):
            print("*" * (l - (i + 1)))
    else:
        for i in range(1,l):
            print("*" * (i + 1))
        for i in range(l - 1):
            print("*" * (l - (i + 1)))