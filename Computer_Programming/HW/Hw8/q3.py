from turtle import *
l = 20
def draw_arrow(l=10):
    fillcolor("black")
    left(90)
    backward(l/2)
    begin_fill()
    for i in range(3):
        forward(l)
        right(120)
    end_fill()
    forward(l/2)
    right(90)

character = input("Enter character: ").strip()
meow = dict()
for i in character:
    if i in meow:
        meow[i] += 1
    else:
        meow[i] = 1
if " " in meow:
  del meow[" "]
adjusted_length = len(character.replace(" ", ""))
max_val = max(meow.values())
print(meow)
left(90)
forward(l * max_val)
draw_arrow()
backward(l * max_val)
right(90)

for i in meow:
    forward(l)
    right(90)
    pu()
    forward(20)
    write(i)
    backward(20)
    pd()
    left(90)
    left(90)
    for j in range(2):
        forward(l * meow[i])
        right(90)
        forward(10)
        right(90)
    right(90)
    forward(10)

forward(l)
draw_arrow()
hideturtle()
done()
