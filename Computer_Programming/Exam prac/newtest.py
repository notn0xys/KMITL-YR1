import turtle
def draw_sq(x):
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)
def control(l,n):
    for i in range(n):
        draw_sq(l/((2**0.5) ** i) )
        turtle.forward(l/(((2**0.5) ** i) * 2))
        turtle.left(45)
control(250,8)
turtle.done()