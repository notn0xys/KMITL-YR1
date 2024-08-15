while True:
    while True:
        a = input("Enter a Character: ")
        if len(a) == 1:
            break
        print("Try agian")
    meow = int(ord(a))
    if meow == 9:
        break
    if meow in range(int(ord("0")), int(ord("9")) + 1):
        print("it is a numeric Character")
    elif meow in range(int(ord("a")) , int(ord("z")) + 1):
        b = a.upper()
        print(f"{a} is a Small case letter and the Capitol letter is {b}")
    elif meow in range(int(ord("A")) , int(ord("Z")) + 1 ):
        b = a.lower()
        print(f"{a} is a Capital Letter and the Small case letter is {b}")
    else:
        print(f"{a} is a Special Character")