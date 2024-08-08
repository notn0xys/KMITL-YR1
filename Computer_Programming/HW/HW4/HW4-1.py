from turtle import *
print("Point1")
x1 = float(input("Enter x1"))
y1 = float(input("Enter xy"))
print("Point2")
x2 = float(input("Enter x2"))
y2 = float(input("Enter y2"))
print("Point 3")
x3 = float(input("Enter x3"))
y3 = float(input("Enter y3"))
slope = (y2-y1)/(x2-x1)
c = y1 - (slope * x1)

if y2 == (slope * x2) + c:
    print("point 2 is on the line between point 1 and 3")


penup()
goto(x1,y1)
write(x1,y1)
pendown()
done()
