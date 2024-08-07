#HW3-1
name = input("Enter Employee's name: ")
no_of_hours = float(input("Enter The amount of hours worked in a week: "))
pay_rate = float(input("Enter Hourly Payrate: "))
tax_withholding_rate = float(input("Enter federal tax withholding rate: "))
state_tax_withholding = float(input("Enter State tax withholding rate: "))

grosspay = no_of_hours * pay_rate
fed_taxed = grosspay * tax_withholding_rate
state_taxed = grosspay * state_tax_withholding
total_taxxed = fed_taxed + state_taxed
net_pay = grosspay - total_taxxed

print("Employee's Name: " + name)
print(f"Hours worked: {no_of_hours}")
print(f"Pay Rate: ${pay_rate}" )
print(f"Gross Pay: ${grosspay:.2f}" )
print("Deductions:")
print(f" Federal Withholding ({tax_withholding_rate:.1%}) : ${fed_taxed:.2f}")
print(f" State Withholding ({state_tax_withholding:.1%}) : ${state_taxed:.2f}")
print(f" Total Deduction : ${total_taxxed:.2f}")
print(f"Net Pay : ${net_pay:.2f}")

#HW3-2
while True:
    x = input("Enter Your input: ")
    if len(x) == 4:
        if x.isdigit():
            x = "".join(reversed(x))
            x = int(x)
            break
        print("Not an integer")
    else:
        print("Not 4 characters long")
print(x)

#HW3-3
from turtle import *
lenght = int(input("Enter your the lenght of the star: "))

for i in range(5):
    forward(lenght)
    right(144)
done()

#HW3-4
from turtle import *
while True:
    r = input("Please enter radius: ")
    if r.isdigit():
        r = int(r)
        break
    print("Please enter an integer: ")
small_gap = 0.2 * r
top_move = r*2 + small_gap
pensize(r/15)
penup()
backward(r * 2)
pendown()
color("blue")
circle(r)
penup()
forward(top_move)
x = pos()
color("black")
pendown()
circle(r)
penup()
forward(top_move)
pendown()
color("red")
circle(r)
penup()
goto(-r * 2, (3*r)/4)
right(90)
forward(r*2)
left(90)
forward(top_move/2)
pendown()
color("yellow")
circle(r)
penup()
goto(x)
forward(top_move/2)
left(90)
forward((3*r)/4)
left(180)
forward(r*2)
left(90)
pendown()
color("green")
circle(r)
done()

#HW3-5
from turtle import *
import math
print("Point1")
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
print("Point2")
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
print("Point3")
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))
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
write(area_formatted)
done()