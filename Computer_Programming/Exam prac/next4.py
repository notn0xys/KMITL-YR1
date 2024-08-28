import turtle
def draw_sq(n):
    for i in range(4):
        turtle.forward(n)
        turtle.left(90)
def spiral_sq(s):
    turtle.penup()
    turtle.backward(s/2)
    turtle.right(90)
    turtle.forward(s/2)
    turtle.left(90)
    while s >= 5:
        turtle.pendown()
        draw_sq(s)
        turtle.penup()
        turtle.forward(s/2)
        turtle.left(90)
        turtle.forward(s/2)
        turtle.right(90)
        turtle.left(10)
        s *= 0.75
        turtle.backward(s/2)
        turtle.right(90)
        turtle.forward(s/2)
        turtle.left(90)

spiral_sq(150)
turtle.done()
    
