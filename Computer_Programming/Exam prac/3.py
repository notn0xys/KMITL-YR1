import turtle
def draw_square(n):
    for i in range(4):
        turtle.forward(n)
        turtle.left(90)
def draw_nested_squares(s,g):
    while s >= 20:
        print(s)
        turtle.pendown()
        draw_square(s)
        turtle.penup()
        turtle.forward(g)
        turtle.left(90)
        turtle.forward(g)
        turtle.right(90)
        s -= 2 * g
draw_nested_squares(200,20)
turtle.done()