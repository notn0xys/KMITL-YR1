from turtle import *
i = 1
j = 0
k = 0
sq = 0
lenght  = 35
width = 20
left(90)
penup()
forward(300)
right(90)
pendown()
while i <= 12:
    j = 0
    while j < 7:
        if j == 0:
            forward(lenght * 7)
            right(90)
            forward(width)
            right(90)
            forward(lenght * 7)
            p = pos()
            x1 , y1 = p
            right(90)
            forward(width)
            right(90)
            penup()
            goto(x1 + 10 , y1)
            write("Month#" + str(i) , font=("Arial", 10, "normal"))
            backward(x1 + 10)
            right(90)
            pendown()
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
                forward(lenght)
                m += 1
            k  += 1
            backward(lenght * 7)
            right(90)
            if j != 6:
                forward(width)
                left(90)
        j += 1
    penup()
    forward(20)
    left(90)
    pendown()
    i += 1

done()
