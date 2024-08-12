import turtle as t
length1 = int(input("Enter length of rectangle 1: "))
height1 = int(input("Enter height of rectangle 1: "))
x1 = int(input("Enter x position for rectangle 1: "))
y1 = int(input("Enter y position for rectangle 1: "))

length2 = int(input("Enter length of rectangle 2: "))
height2 = int(input("Enter height of rectangle 2: "))
x2 = int(input("Enter x position for rectangle 2: "))
y2 = int(input("Enter y position for rectangle 2: "))

# getting the 2 points of the rectangles

#top left rect1
r1x1 = x1 - length1/2
r1y1 = y1 + height1/2
#bottom right rect1
r1x2 = x1 + length1/2
r1y2 = y1 - height1/2

#top left rect2
r2x1 = x2 - length2/2
r2y1 = y2 + height2/2
#bottom right rect2
r2x2 = x2 + length2/2
r2y2 = y2 - height2/2

#calculation for overlap
width_overlap = False
height_overlap = False
overlap_output = ""
inside_output = ""

if min(r1x2,r2x2) > max(r1x1,r2x1):
    width_overlap = True
if min(r1y1,r2y1) > max(r1y2,r2y2):
    height_overlap = True

if width_overlap and height_overlap:
    overlap_output = "Overlap!"
    print(overlap_output)

if length1 > length2 and height1 > height2:
    if (r2x1 >= r1x1 and r2y1<=r1y1) and (r2x2 <= r1x2 and r2y2 >= r1y2):
        inside_output = "Rect 2 is inside Rect 1"
        overlap_output =""
        print(inside_output)
elif length2 > length1 and height2 > height1:
    if (r1x1 >= r2x1 and r1y1<=r2y1) and (r1x2 <= r2x2 and r1y2 >= r2y2):
        inside_output = "Rect 1 is inside Rect 2"
        overlap_output =""
        print(inside_output)


# turtle for testing
t.color("red")
t.penup()
t.goto(x1,y1)
t.forward(length1/2)
t.pendown()
t.right(90)
t.forward(length1/2)
t.right(90)
t.forward(length1)
t.right(90)
t.forward(height1)
t.right(90)
t.forward(length1)
t.right(90)
t.forward(length1/2)

t.color("blue")
t.penup()
t.goto(x2,y2)
t.forward(length2/2)
t.pendown()
t.right(90)
t.forward(length2/2)
t.right(90)
t.forward(length2)
t.right(90)
t.forward(height2)
t.right(90)
t.forward(length2)
t.right(90)
t.forward(length2/2)

t.penup()
t.goto(min(r1x2,r2x2)+50,min(r1y2,r2y2)-50)
t.write(overlap_output)
t.goto(min(r1x2,r2x2)+50,min(r1y2,r2y2)-60)
t.write(inside_output)


t.mainloop()

