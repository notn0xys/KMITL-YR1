from turtle import *
import turtle
import math

r = int(input("Type the radius of the circle: "))
x = int(input("Enter Coordinate x: "))
y = int(input("Enter coordinate Y: "))

area = pow(r,2) * math.pi
penup()
goto(x,y)
pendown()
write(area)
penup()
goto(x,y-r)
pendown()
circle(r)
turtle.Screen().exitonclick()

