l1 = input("Enter List 1: ").split()
l2 = input("Enter list 2: ").split()
amount = len(l1)
z = 0
if len(l1) == len(l2):
    for i in range(amount):
        temp = 0
        temp = l1[0]
        del l1[0]
        l1.append(temp)
        if l1 == l2:
            z = 1
            print("yes")
    if z != 1:
        print("no")
