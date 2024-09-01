for i in range(49,0,-1):
    if i % 3 != 0 and i % 5 != 0:
        print(i, end="")
        if i == 1:
            print(".")
        else:
            print("," ,end="")