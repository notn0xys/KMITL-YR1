while True:
    n = input("Enter an Integer: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
    print("Wrong input Try agian")

