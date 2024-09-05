from turtle import *
import math
class Rectangle:
    def __init__(self,x,y,w,h) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        return None
    def get_area(self) -> int:
        return self.w * self.h
    def get_peri(self) -> int:
        return (2* self.w) + (2* self.l)
    def move(self,x,y):
        self.x = x
        self.y = y
    def intersec(self, rec):
        # Coordinates of the current rectangle
        left1 = self.x
        right1 = self.x + self.w
        top1 = self.y
        bottom1 = self.y - self.h
        
        # Coordinates of the other rectangle
        left2 = rec.x
        right2 = rec.x + rec.w
        top2 = rec.y
        bottom2 = rec.y - rec.h
        
        # Check if there is no overlap
        if right1 < left2 or left1 > right2 or top1 < bottom2 or bottom1 > top2:
            print("Not overlap")
            return None
        
        # Calculate the intersection rectangle
        new_x = max(left1, left2)
        new_y = min(top1, top2)
        new_w = min(right1, right2) - new_x
        new_h = new_y - max(bottom1, bottom2)
        
        if new_w <= 0 or new_h <= 0:
            print("Not overlap")
            return None
        
        return Rectangle(new_x, new_y, new_w, new_h)
    def draw(self):
        penup()
        goto(self.x,self.y)
        pendown()
        for i in range(2):
            forward(self.w)
            right(90)
            forward(self.h)
            right(90)
class circle1:
    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.r = r
        return None
    def get_area(self) -> int:
        return self.r * self.r * math.pi
    def get_per(self) -> int:
        return self.r * 2 * math.pi
    def move(self,x,y):
        self.x = x
        self.y = y 
    def draw(self):
        penup()
        goto(self.x, self.y - self.r)
        pendown()
        circle(self.r)
rec2 = Rectangle(0,0,100,100)
rec1 = Rectangle(-50,-50,300,300)
rec1.draw()
rec2.draw()
rec3 = rec1.intersec(rec2)
print(f"{rec3.x} + {rec3.y} + {rec3.w} + {rec3.h}")
rec3.draw()
rec3.move(-200,-200)
rec3.draw()
done()
