#HW5-1
while True:
    n = input("Enter a positive number: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
        else:
            print("Not 0")
    else:
        print("Try agian")
guess = n / 2
time5 = 0
time6 = 0
time7 = 0
square_root = n ** (1/2)
for i in range(7):
    temp = n / guess
    guess = (guess + temp) / 2
    if i == 4:
        time5 = guess
    if i == 5:
        time6 = guess
    if i == 6:
        time7 = guess
print(f"When done 5 times you get {time5:.3f} actual square root is {square_root:.3f}")
print(f"When done 6 times you get {time6:.3f} actual square root is {square_root:.3f} ")
print(f"When done 7 times you get {time7:.3f} actual square root is {square_root:.3f} ")

#HW5-2
from turtle import *
i = 1
j = 0
temp_days = 1
counter = 0
last_date = 2
amount_of_days = 0
list_of_days = ["Su","Mo","Tu","We","Th","Fr","Sa"]
lenght  = 35
width = 20
left(90)
penup()
forward(350)
right(90)
speed("fastest")
meow = pos()
meow1 , meow2 = meow
pendown()
while i <= 12:
    if i == 5:
        penup()
        goto(meow1 - (lenght * 7) - 25 ,meow2)
        pendown()
    if i == 9:
        penup()
        goto(meow1 - ( ((lenght * 7) - 25 ) * 2 ) - 100 ,meow2)
        pendown()
    if i == 3 or i == 6:
        extra = 8
    else:
        extra = 7
    if i == 4 or i == 6 or i == 9 or i == 11:
        amount_of_days = 30
    elif i == 2:
        amount_of_days = 29
    else: 
        amount_of_days = 31
    j = 0
    while j < extra:
        if j == 0:
            forward(lenght * 7)
            right(90)
            forward(width)
            right(90)
            forward(lenght * 7)
            right(90)
            forward(width)
            right(90)
            penup()
            right(90)
            pendown()
            forward(width)
            left(90)
            forward(10)
            write("Month#" + str(i) , font=("Arial", 10, "normal"))
            backward(10)
            right(90)
            forward(width)
            left(90)

        elif j == 1:
            m = 0
            while m < 7:
                l = 0
                while l < 2:
                    forward(lenght)
                    left(90)
                    forward(width)
                    left(90)
                    l += 1
                forward(lenght * (1/4))
                write(list_of_days[m],font=("Arial", 10, "normal"))
                forward(lenght * (3/4))
                m += 1
            backward(lenght * 7)
            right(90)
            if j != 6:
                forward(width)
                left(90)
        elif j == 2:
            m = 0
            while m < 7:
                l = 0
                while l < 2:
                    forward(lenght)
                    left(90)
                    forward(width)
                    left(90)
                    l += 1
                forward(lenght * (1/4))
                if m >= last_date - 1:
                    write(temp_days,font=("Arial", 10, "normal"))
                    temp_days += 1
                forward(lenght * (3/4))
                m += 1
            backward(lenght * 7)
            right(90)
            if j != 6:
                forward(width)
                left(90)
        else:
            m = 0
            while m < 7:
                l = 0
                while l < 2:
                    forward(lenght)
                    left(90)
                    forward(width)
                    left(90)
                    l += 1
                counter += 1
                forward(lenght * (1/4))
                if temp_days <= amount_of_days:
                    write(temp_days,font=("Arial", 10, "normal"))
                    if temp_days == amount_of_days:
                        last_date = counter
                        if last_date == 8:
                            last_date = 1
                    temp_days += 1
                forward(lenght * (3/4))
                m += 1
            counter = 1
            backward(lenght * 7)
            right(90)
            if j != extra - 1:
                forward(width)
                left(90)
        j += 1
    penup()
    forward(25)
    left(90)
    pendown()
    temp_days = 1
    i += 1
hideturtle()
done()

#HW5-3
while True:
    n = input("Enter an integer that is greater than or equal to 1: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
        print("More than 0")
    else:
        print("Enter a positive int")
print(f"Input: {n}")
print("")
for i in range(n):
    l = n - i
    if i == 0 or i == n - 1:
        for i in range(l):
            print("*" * (i + 1))
        for i in range(l - 1):
            print("*" * (l - (i + 1)))
    else:
        for i in range(1,l):
            print("*" * (i + 1))
        for i in range(l - 1):
            print("*" * (l - (i + 1)))