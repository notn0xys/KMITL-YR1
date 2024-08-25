from turtle import *
def draw_poly(x,y,sides = 4,size = 100):
    penup()
    goto(x,y)
    pendown()
    for i in range(sides):
        forward(size)
        left(360/sides)

draw_poly(0,0)
draw_poly(10,10,5)
draw_poly(10,10,5,200)
done()