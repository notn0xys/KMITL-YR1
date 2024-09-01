import turtle
def draw_tri(x):
    for i in range(3):
        turtle.forward(x)
        turtle.left(120)
def draw_rest(l , n):
    for i in range(n):
        draw_tri(l / (2**i))
        turtle.forward(l / ((2**i) * 2))
        turtle.left(60)

draw_rest(200,4)
turtle.done()
        