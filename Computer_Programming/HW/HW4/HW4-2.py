from turtle import *
x1 = int(input("Enter the x coordinates of the center for square 1: "))
y1 = int(input("Enter the y coordinates of the center for square 1: "))
l1 = int(input("Enter the Lenght for square 1: "))
w1 = int(input("Enter the Width for square 1: "))
x2 = int(input("Enter the x coordinates of the center for square 2: "))
y2 = int(input("Enter the y coordinates of the center for square 2: "))
l2 = int(input("Enter the Lenght for square 2: "))
w2 = int(input("Enter the Width for square 2: "))
overlap = False
amount = 0
top_left1x = (x1 - l1/2)
top_left1y = (y1 + w1/2)
top_right1x = (x1 + l1/2)
top_right1y = (y1 + w1/2)
bottom_left1x = (x1 - l1/2)
bottom_left1y = (y1 - w1/2)
bottem_right1x = (x1 + l1/2)              
bottom_right1y =(y1 - w1/2)
top_left2x = (x2 - l2/2)
top_left2y = (y2 + w2/2)
top_right2x = (x2 + l2/2)
top_right2y = (y2 + w2/2)
bottom_left2x = (x2 - l2/2)
bottom_left2y = (y2 - w2/2)
bottem_right2x = (x2 + l2/2)              
bottom_right2y =(y2 - w2/2)
squ2 = [[top_left2x,top_left2y],[top_right2x,top_right2y],[bottom_left2x,bottom_left2y],[bottem_right2x,bottom_right2y]]
squ1 = [[top_left1x,top_left1y],[top_right1x,top_right1y],[bottom_left1x,bottom_left1y],[bottem_right1x,bottom_right1y]]
for i in squ1:
    if i[0] in range(int(top_left2x),int(top_right2x) + 1):
        if i[1] in range(int(bottom_left2y),int(top_left2y) + 1):
            overlap = True
            amount += 1
for i in squ2:
    if i[0] in range(int(top_left1x),int(top_right1x) + 1):
        if i[1] in range(int(bottom_left1y),int(top_left1y) + 1):
            overlap = True
            amount += 1

if overlap:
    print("It overlaps") 
elif overlap and amount == 4:
    print("it is inside")
penup()
goto(x1,y1)
pendown()
circle(1)
penup()
p = pos()
write(p)
goto(top_left1x,top_left1y)
pendown()
goto(top_right1x,top_right1y)
goto(bottem_right1x,bottom_right1y)
goto(bottom_left1x,bottom_left1y)
goto(top_left1x,top_right1y)
penup()
goto(x2,y2)
pendown()
circle(1)
penup()
p = pos()
write(p)
goto(top_left2x,top_left2y)
pendown()
goto(top_right2x,top_right2y)
goto(bottem_right2x,bottom_right2y)
goto(bottom_left2x,bottom_left2y)
goto(top_left2x,top_right2y)
done()
