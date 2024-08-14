from turtle import *
def get_coords(points):
    print(points)
    x = float(input(f"Enter {points} x: "))
    y = float(input(f"Enter {points} y: "))
    return x,y
x0 , y0 = get_coords("Point 0")
x1 , y1 = get_coords("Point 1")
x2 , y2 = get_coords("Point 2")

if x1 - x0 != 0:
    slope = (y1-y0)/(x1-x0)
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
    if x2 > x1:
        print("Point 2 is on the right")
    else:
        print("Point 2 is on the left")
penup()
goto(x0,y0)
p = pos()
write(p)
pendown()
goto(x1,y1)
p = pos()
write(p)
penup()
goto(x2,y2)
pendown()
p = pos()
write(p)
done()
