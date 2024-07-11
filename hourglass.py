height = int(input("Type your height: "))
amount = 1
x = 0
while amount <= height:
    print(" " * (amount-1 ), end="")
    while x < ((height - (amount-1)) * 2 - 1):
        if amount % 2 == 0:
            print("*",end="")
        else:
            print("#",end="")
        x += 1
    print("")
    x = 0
    amount +=1
amount = 2
x = 0
while amount <= height:
    print(" " * (height- amount),end="")
    while x < (amount * 2) - 1:
        if amount % 2 == 1:
            print("*",end="")
        else:
            print("#",end="")
        x += 1
    print("")
    x = 0
    amount +=1
    