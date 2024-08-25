from turtle import *
def draw(x):
    for i in range(4):
        forward(x)
        left(90)
def controll(u):
    for i in range(4):
        for j  in range(4): draw(u * (j + 1))
        left(90)
controll(50)
done()