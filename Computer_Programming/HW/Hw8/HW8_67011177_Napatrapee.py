#Q1
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
#Q2
character = input("Enter character: ").strip()
meow = dict()
for i in character:
    if i in meow:
        meow[i] += 1
    else:
        meow[i] = 1
if " " in meow:
  del meow[" "]
adjusted_length = len(character.replace(" ", ""))
for i in meow:
    print(f"Char {i} percent {meow[i]/adjusted_length:.2%}")
#Q3
from turtle import *
l = 20
def draw_arrow(l=10):
    fillcolor("black")
    left(90)
    backward(l/2)
    begin_fill()
    for i in range(3):
        forward(l)
        right(120)
    end_fill()
    forward(l/2)
    right(90)

character = input("Enter character: ").strip()
meow = dict()
for i in character:
    if i in meow:
        meow[i] += 1
    else:
        meow[i] = 1
if " " in meow:
  del meow[" "]
adjusted_length = len(character.replace(" ", ""))
max_val = max(meow.values())
print(meow)
left(90)
forward(l * max_val)
draw_arrow()
backward(l * max_val)
right(90)
for i in meow:
    forward(l)
    right(90)
    pu()
    forward(20)
    write(i)
    backward(20)
    pd()
    left(90)
    left(90)
    for j in range(2):
        forward(l * meow[i])
        right(90)
        forward(10)
        right(90)
    right(90)
    forward(10)

forward(l)
draw_arrow()
hideturtle()
done()
#Q4
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