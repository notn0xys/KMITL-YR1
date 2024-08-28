while True:
    while True:
        i = input("Enter a single character: ")
        if len(i) == 1:
            break
    if int(ord(".")) == int(ord(i)):
        print("good bye")
        break
    elif int(ord(i)) in range(int(ord("0")), int(ord("9")) + 1):
        print("It is a numeric character")
    elif int(ord(i)) in range(int(ord("A")), int(ord("Z")) + 1):
        print("It is a capitol letter")
    elif int(ord(i)) in range(int(ord("a")), int(ord("z")) + 1):
        print("it is a small case letter")
    else:
        print("it is a special character")