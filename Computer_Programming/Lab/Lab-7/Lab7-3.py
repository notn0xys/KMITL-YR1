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
    def intersec(self,rec):
        right1 = self.x + self.w
        bot1 = self.y - self.h
        left1 = self.x 
        top1 = self.y
        right2 = rec.x + rec.w
        bot2 = rec.y - rec.h
        left2 = rec.x 
        top2 = rec.y
        new_x = 0
        new_y = 0
        new_l = 0
        new_w = 0
        if right1 < left2 or left1 > right2 or bot1 > top2 or top1 < bot2:
            print("Not overlap")
            return None
        else:
            if left1 >= left2 and left1 <= right2:
                new_x = left1
                if right1 < right2:
                    new_l = right1 - left1
                else:
                    new_l = abs(left1 - right2)
                print("left")

            elif right1 >= left2 and right1 <= right2:
                new_l = right1 - left2
                new_x = right1 - new_l
                print("right")
            else:
                if right1 > right2 and left1 < left2:
                    new_x = left2
                    new_l = right2 - left2
                else:
                    new_x = left1
                    new_l = right1 - left1      
            if top1 >= bot2 and bot1 <= bot2:
                new_y = top1
                new_w = top1 - bot2
                print("top")
            if bot1 <= top2 and bot2 <= bot1:
                new_w = top2 - bot1
                new_y = bot1 + new_w
                print("bot")         
            else:
                print("wtf2")
        return_rec = Rectangle(new_x,new_y,new_l,new_w)
        return return_rec
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
rec2 = Rectangle(5,7,4,3)
rec1 = Rectangle(6,8,3,4)
rec1.draw()
rec2.draw()
rec3 = rec1.intersec(rec2)
print(f"{rec3.x} + {rec3.y} + {rec3.w} + {rec3.h}")
rec3.draw()
rec3.move(-200,-200)
rec3.draw()
done()
