from turtle import *
speed(0)
def cross(l,d):
    if d == 0:
        dot()
        return
    else:
        for i in range(4):
            forward(l)
            cross(l/2,d-1)
            backward(l)
            right(90)
cross(200,6)
done()