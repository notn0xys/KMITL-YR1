def binary(n):
    meow = []
    return_str = ""
    while n > 0:
        meow.insert(0,(n%2))
        n //= 2
    for i in meow:
        return_str += str(i)
    return return_str
def integer(n):
    reversed_str = n[::-1]
    result = 0
    for i in range(len(reversed_str)):
       result += int(reversed_str[i]) * 2**i
    return result
while True:
    n = input("Enter your number: ")
    if n.isdigit():
        n = int(n)
        break
    print("Try agian")
if n == 0:
    print("Value = 0")
else:
    print(binary(n))
    print(integer(binary(n)))