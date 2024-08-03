from turtle import *
import math

x1, y1 = map(int, input("Enter p1: ").split(","))
x2 , y2 = eval(input("Enter P2 "))
x3 , y3 = eval(input("Enter P3 "))

distance_1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
distance_2 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
distance_3 = math.sqrt((x1-x3)**2 + (y1-y3)**2)

s = (distance_1 + distance_2 + distance_3) / 2
area = math.sqrt(s*(s-distance_1)*(s-distance_2)*(s-distance_3))
area_formatted = format(area, ".2f")
penup()
goto(x1,y1)
pendown()
goto(x2,y2)
goto(x3,y3)
goto(x1,y1)
penup()
goto(min([x1,x2,x3]),min([y1,y2,y3]) - 20)
pendown()
write(area_formatted, font=("Arial", 12, "normal"))
done()
