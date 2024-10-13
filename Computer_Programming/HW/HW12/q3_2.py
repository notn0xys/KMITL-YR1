import math
from turtle import *
class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.furthest = 0
    def get_distance(self):
        d = math.sqrt((self.x ** 2) + (self.y ** 2))
        return d
    def draw_points(self):
        pu()
        goto(self.x,self.y - 3)
        pd()
        circle(3)
class Rectangle:
    def __init__(self) -> None:
        self.w = 0
        self.l = 0
        self.far = 0
    def furthest(self, x:list):
        self.leftx = x[0].x
        self.rightx = x[0].x
        self.topy = x[0].y
        self.boty = x[0].y
        for i in x:
            if i.x > self.rightx:
                self.rightx = i.x
            if i.x < self.leftx:
                self.leftx = i.x
            if i.y > self.topy:
                self.topy = i.y
            if i.y < self.boty:
                self.boty = i.y
        self.centerX = (self.leftx + self.rightx) / 2
        self.centerY = (self.topy + self.boty) / 2
        self.width = self.rightx - self.leftx
        self.height = self.topy - self.boty
        print(f"The bounding rectangle is centered at ({self.centerX}, {self.centerY}) "
              f"with width {self.width} and height {self.height}.")
    def drawsq(self):
        pu()
        goto(self.leftx,self.boty)
        pd()
        goto(self.rightx,self.boty)
        goto(self.rightx,self.topy)
        goto(self.leftx,self.topy)
        goto(self.leftx,self.boty)
        pu()
        goto(self.centerX,self.centerY)
x = input("Please enter the points: ")
meow = list(map(int, x.split()))
list_of_points = []
if len(meow) % 2 != 0:
    meow.pop()
for i in range(0,len(meow),2):
    pointa = Point(meow[i],meow[i+ 1])
    list_of_points.append(pointa)
for i in list_of_points:
    i.draw_points()
meow = Rectangle()
meow.furthest(list_of_points)
meow.drawsq()
done()