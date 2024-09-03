while True:
    n = input("Enter a number: ")
    if n.isdigit():
        n = int(n)
        if n >= 0 and n <= 999:
            break
    print("I dont know")
    break
list_of_digits = ["one","two","three","four","five","six","seven","eight","nine"]
list_of_tens = ["eleven","twelve","thriteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
list_of_tys = ["ten","twenty","thrity","forty","fifty","sixty","seventy","eighty","ninety"]
hundread = n//100
n = n - (hundread * 100)
tens = n//10
n = n - (tens * 10)

if hundread > 0:
    print(f"{list_of_digits[hundread-1]} hundred ",end="")
    if tens > 0 or n > 0:
        print("and " , end="")
if tens == 1:
    if n > 0:
        print(f"{list_of_tens[n-1]} ")
    else:
        print(f" {list_of_tys[0]} ")
else: 
    if tens > 1:
        print(f"{list_of_tys[tens-1]}" , end="")
        if n > 0:
            print("-",end="")
    if n > 0:
        print(f"{list_of_digits[n-1]} ")
