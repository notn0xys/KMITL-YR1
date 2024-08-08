num = float(input("Enter a number: "))
isInt = num == int(num)
if isInt == False:
    num = float(num)
    a = int(input("Do you want to display in (1)floating point or (2)scitific format"))
    if a == 1:
        print(f"Your number is {num:.2f}")
    else:
        print(f"Your number is {num:.2E}")
else:
    num = int(num)
    a = int(input("Do you want to display in (1)binary or (2)octal (3) hexadecimal (4) decimal format"))
    if a == 1:
        num = bin(num)
        print(num)
    elif a == 2:
        num = oct(num)
        print(num)
    elif a == 3:
        num = hex(num)
        print(num)
    elif a == 4:
        print(num)
    else:
        print("Wrong input nyah")




