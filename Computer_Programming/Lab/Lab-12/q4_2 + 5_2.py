from turtle import *
from abc import ABC
speed(0)
class TwoDShape(ABC):
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y
    def draw(self):
        pu()
        goto(self.x,self.y)
class line(TwoDShape):
    def __init__(self, x=0, y=0,targetx = 10 , targety = 10) -> None:
        super().__init__(x, y)
        self.targetx = targetx
        self.targety = targety
    def draw(self,x = 0,y = 0):
        super().draw()
        pd()
        goto(self.targetx,self.targety)
class Rectangle(TwoDShape):
    def __init__(self, x=0, y=0,w = 10 , l = 20) -> None:
        super().__init__(x, y)
        self.w = w
        self.l = l
    def draw(self):
        super().draw()
        backward(self.l/2)
        left(90)
        forward(self.w/2)
        right(90)
        pd()
        for i in range(2):
            forward(self.l)
            right(90)
            forward(self.w)
            right(90)
class Circle(TwoDShape):
    def __init__(self, x=0, y=0,r = 20) -> None:
        super().__init__(x, y)
        self.r = r
    def draw(self):
        super().draw()
        goto(self.x, self.y - self.r)
        pd()
        circle(self.r)
class Square(TwoDShape):
    def __init__(self, x=0, y=0, l = 20) -> None:
        super().__init__(x, y)
        self.l = l
    def draw(self):
        super().draw()
        backward(self.l/2)
        left(90)
        forward(self.l/2)
        right(90)
        pd()
        for i in range(4):
            forward(self.l)
            right(90)
meow = [Circle(100,200,30),line(10,10,100,100),Rectangle(0,0,19,30),Square(30,30,50)]

for i in meow:
    i.draw()
done()

        
        
