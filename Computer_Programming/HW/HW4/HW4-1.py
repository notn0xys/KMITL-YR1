from turtle import *
print("Point1")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
print("Point2")
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
print("Point 3")
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))
if x3 - x1 != 0:
    slope = (y3-y1)/(x3-x1)
    c = y1 - (slope * x1)
    if y2 == (slope * x2) + c:
        print("point 2 is on the line between point 1 and 3")
    else:
        if slope > 0:
            if y2 > (slope * x2) + c:
                print("Point 2 is on the left")
            else:
                print("Point 2 is on the Right")
        elif slope < 0:
            if y2 > (slope * x2) + c:
                print("Point 2 is on the Right")
            else:
                print("Point 2 is on the Left")
        else:
            if y2 > y1:
                print("Point 2 is on the left")
            else:
                print("Point 2 is on the Right")
else:
    if x2 > x3:
        print("Point 2 is on the right")
    else:
        print("Point 2 is on the left")


penup()
goto(x1,y1)
p = pos()
write(p)
pendown()
goto(x3,y3)
p = pos()
write(p)
penup()
goto(x2,y2)
pendown()
p = pos()
write(p)
done()
