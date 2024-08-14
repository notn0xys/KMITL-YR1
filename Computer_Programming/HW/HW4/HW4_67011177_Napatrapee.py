#Hw4-1
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


#HW4-2
from turtle import *
x1 = int(input("Enter the x coordinates of the center for Rectangle 1: "))
y1 = int(input("Enter the y coordinates of the center for Rectangle 1: "))
l1 = int(input("Enter the Lenght for Rectangle 1: "))
w1 = int(input("Enter the Width for Rectangle 1: "))
x2 = int(input("Enter the x coordinates of the center for Rectangle 2: "))
y2 = int(input("Enter the y coordinates of the center for Rectangle 2: "))
l2 = int(input("Enter the Lenght for Rectangle 2: "))
w2 = int(input("Enter the Width for Rectangle 2: "))
left1 = (x1 - l1/2)
top1 = (y1 + w1/2)
right1 = (x1 + l1/2)
bottom1 = (y1 - w1/2)
left2 = (x2 - l2/2)
top2 = (y2 + w2/2)
right2 = (x2 + l2/2)
bottom_2 = (y2 - w2/2)

if right1 == left2 or left1 == right2 or top1 == bottom_2 or bottom1 == top2:
    print("It does not overlap")
else:
    if right1 > right2 and left1 < left2 and top1 > top2 and bottom1 < bottom_2:
        print("It is inside")
    elif right2 > right1 and left2 < left1 and top2 > top1 and bottom_2 < bottom1:
        print("It is inside")
    elif right1 < left2 or top1 < bottom_2 or left1 > right2 or bottom1 > top2:
        print("It does not overlap") 
    else:
        print("it overlaps")
penup()
goto(x1,y1)
pendown()
circle(1)
penup()
p = pos()
write(p)
goto(left1,top1)
pendown()
goto(right1,top1)
goto(right1,bottom1)
goto(left1,bottom1)
goto(left1,top1)
penup()
goto(x2,y2)
pendown()
circle(1)
penup()
p = pos()
write(p)
goto(left2,top2)
pendown()
goto(right2,top2)
goto(right2,bottom_2)
goto(left2,bottom_2)
goto(left2,top2)
done()
