from turtle import *
while True:
    n = input("Enter an Integer: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
    print("Wrong input Try agian")
lenght = 100/n
for i in range(n):
    for i in range(n):
        for i in range(4):
            pendown()
            forward(lenght)
            left(90)
        forward(lenght)
    penup()
    backward(lenght * n)
    right(90)
    forward(lenght)
    left(90)
left(90)
forward(lenght)
right(90)
done()
