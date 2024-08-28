from turtle import *
def square(l):
    for i in range(4):
        forward(l)
        left(90)
def minor(l,n):
    for i in range(n):
        square(l/((2**0.5)**i))
        forward(l/(((2 ** 0.5)**i) * 2))
        left(45)
minor(300,4)
done()