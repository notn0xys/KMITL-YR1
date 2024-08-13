from turtle import *
def get_coords(points):
    print(points)
    x = float(input(f"Enter {points} x: "))
    y = float(input(f"Enter {points} y: "))
    return x,y
x1 , y1 = get_coords("Point 1")
x2 , y2 = get_coords("Point 2")
x3 , y3 = get_coords("Point 3")

if x3 - x1 != 0:
    slope = (y3-y1)/(x3-x1)
    c = y1 - (slope * x1)
    if y2 == (slope * x2) + c:
        print("point 2 is on the line")
    elif slope >= 0:
        if y2 > (slope * x2) + c:
            print("Point 2 is on the left")
        else:
            print("Point 2 is on the Right")
    else:
        if y2 > (slope * x2) + c:
            print("Point 2 is on the Right")
        else:
            print("Point 2 is on the Left")
else:
    if x2 > x3:
        print("Point 2 is on the right")
    else:
        print("Point 2 is on the left")
#Drawing the lines and coordinates.
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
