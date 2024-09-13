num = ""
result = 0
while True:
    num = input("Enter the first 9 digit of your ISBN-10 number: ")
    if num.isdigit() and len(num) == 9:
        break
    else:
        print("Try agiam")
for i in range(1,len(num) + 1):
    result += int(num[i - 1]) * i
check_sum = "0"
if result % 11 == 10:
    check_sum = "X"
else:
    check_sum = str(result%11)
print(f"Your ISBN-10 Number is {num + check_sum}")