from turtle import *
def collect(le:list):
    speed(0)
    le.sort()
    l = 20
    meow = dict()
    for i in le:
        if i in meow:
            meow[i] += 1
        else:
            meow[i] = 1
    e = list(meow.values())
    moew1= max(e)
    left(90)
    forward(moew1 * l)
    pu()
    forward(10)
    write("Y")
    backward(10)
    pd()
    backward(moew1 * l)
    right(90)
    forward(l)
    fillcolor("blue") 
    begin_fill() 
    for i in meow:
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
            forward(20)
            right(90)
        right(90)
        forward(20)
    end_fill()
    forward(l)
    pu()
    forward(10)
    write("X")
    backward(10)
    pd()
    hideturtle()
    done()


collect([1,2,3,4,5,6,2,3,4,5,6,1,2,5,6,2,3,3,3,3,3,3,3,3,3,3,4,5,6,3,4,5,6,1,8])