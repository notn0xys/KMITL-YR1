import turtle
def draw_triangle(l):
    for i in range(3):
        turtle.forward(l)
        turtle.left(120)
def control(times = 2, lenght = 200):
    for i in range(times):
        draw_triangle(lenght/(2**i))
        turtle.forward(lenght/(2*(2**i)))
        turtle.left(60)

control(5,350)
turtle.done()