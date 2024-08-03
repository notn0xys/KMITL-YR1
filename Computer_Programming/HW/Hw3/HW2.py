while True:
    x = input("Enter Your input: ")
    if len(x) == 4:
        if x.isdigit():
            x = "".join(reversed(x))
            x = int(x)
            break
        print("Not an integer")
    print("Not 4 characters long")
print(x)

