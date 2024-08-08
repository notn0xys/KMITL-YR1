while True:
    a = input("Enter a single character: ")
    if len(a) == 1:
        break
    print("Not a single character")
l = int(ord(a))
owo = int(ord("0"))
uwu = int(ord("9"))
if l in range(owo, uwu + 1):
    print(f"{a} is a Numeric Character")
elif l in range(int(ord("a")) , int(ord("z")) + 1):
    b = a.upper()
    print(f"{a} is a Small case letter and the Capitol letter is {b}")
elif l in range(int(ord("A")) , int(ord("Z")) + 1 ):
    b = a.lower()
    print(f"{a} is a Capital Letter and the Small case letter is {b}")
else:
    print(f"{a} is a Special Character")
