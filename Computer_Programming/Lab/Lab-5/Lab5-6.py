import math
while True:
    n = input("Enter an Integer: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
    print("Wrong input Try agian")
peak = math.ceil(n / 2)
unpeak = math.floor(n / 2)
for i in range(peak):
    for j in range(i + 1):
        print(2 ** (i - j), end="")
    print("")
for i in range(unpeak):
    for j in range(0, unpeak - i):
        print(2 ** ((unpeak - i) - (j + 1)), end="")
    print("")
