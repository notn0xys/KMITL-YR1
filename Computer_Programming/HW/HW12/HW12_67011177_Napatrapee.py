#Q1
def textese(s:str,ref:dict):
    keys = list(ref.keys())
    reverse = keys[::-1]
    for i in reverse:
        s = s.replace(i, ref[i])
    return s
def untextese(s:str,ref:dict):
    list_of_vals = list(ref.values())
    list_of_keys = list(ref.keys())
    list_of_keys = list_of_keys[::-1]
    list_of_vals = list_of_vals[::-1]
    string_list = s.split()
    for i in range(len(string_list)):
        try:
            position = list_of_vals.index(string_list[i])
            string_list[i] = list_of_keys[position]
        except:
            continue
    e = " ".join(string_list)
    return e
abbreviations = {
    "be": "b",
    "because": "cuz",
    "see": "c",
    "the": "da",
    "okay": "ok",
    "are": "r",
    "you": "u",
    "without": "w/o",
    "why": "y",
    "see you": "cu",
    "ate": "8",
    "great": "gr8",
    "mate": "m8",
    "wait": "w8",
    "later": "l8r",
    "tomorrow": "2mro",
    "for": "4",
    "before": "b4",
    "once": "1ce",
    "and": "&",
    "Your": "ur",
    "You're": "ur",
    "As far as I know": "afaik",
    "As soon as possible": "ASAP",
    "At the moment": "atm",
    "Be right back": "brb",
    "By the way": "btw",
    "For your information": "FYI",
    "In my humble opinion": "imho",
    "In my opinion": "imo",
    "Laughing out loud": "lol",
    "Oh my god": "omg",
    "Rolling on the floor laughing": "rofl",
    "Talk to you later": "ttyl"
}
s = "be As far as I know By the way gyaaat Talk to you later"
l = textese(s,abbreviations)
print(l)
l = untextese(l,abbreviations)
print(l)
#Q2
def composit(x:dict,y:dict):
    return_dict = {}
    for nyan,meow in x.items():
        for nyah , muah in y.items():
            if meow == nyah:
                return_dict[nyan] = muah
    return return_dict
dict1 = {'a': "p",'b': "r",'c': "q",'d': "p",'e': "n",}
dict2 = {'p': "1",'q': "2",'r': "3"}
print(composit(dict1,dict2))
#Q3
import itertools

def product_sets(*sets):
    result = itertools.product(*sets)
    set_result = set(result)
    return set_result

s1 = {1,2,3}
s2 = {'p','q'}
s3 = {'a','b','c'}
print(product_sets(s1,s2,s3))
#Q4
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
#Q5
from abc import ABC
from turtle import *
class Char(ABC):
    def __init__(self) -> None:
        super().__init__()
    def draw(self,x = 0,y = 0):
        pass
    def getWidth(self):
        pass
class Char0(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        pu()
        goto(x,y)
        pd()
        forward(20)
        left(90)
        forward(40)
        left(90)
        forward(20)
        left(90)
        forward(40)
        left(90)
        forward(20)
        pu()
        forward(10)
        pd()
    def getWidth(self):
        return 20
class Char1(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
            pu()
            goto(x,y)
            pd()
            forward(20)
            p = pos()
            backward(10)
            left(90)
            forward(40)
            left(135)
            forward(15)
            pu()
            goto(p)
            right(225)
            forward(10)
            pd()
    def getWidth(self):
        return 20
class Char2(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        pu()
        goto(x,y)
        pd()
        forward(20)
        p = pos()
        backward(20)
        left(90)
        forward(20)
        right(90)
        forward(20)
        left(90)
        forward(20)
        left(90)
        forward(20)
        pu()
        right(180)
        goto(p)
        forward(10)
        pd()
    def getWidth(self):
        return 20
class Char3(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        pu()
        goto(x,y)
        pd()
        forward(20)
        p = pos()
        left(90)
        forward(20)
        left(90)
        forward(20)
        backward(20)
        right(90)
        forward(20)
        left(90)
        forward(20)
        pu()
        right(180)
        goto(p)
        forward(10)
        pd()
    def getWidth(self):
        return 20
class Char4(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        pu()
        goto(x,y)
        forward(20)
        pd()
        left(90)
        forward(40)
        backward(20)
        left(90)
        forward(20)
        right(90)
        forward(20)
        right(90)
        
    def getWidth(self):
        return 20
class Char5(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        pu()
        goto(x,y)
        pd()
        forward(20)
        left(90)
        forward(20)
        left(90)
        forward(20)
        right(90)
        forward(20)
        right(90)
        forward(20)
    def getWidth(self):
        return 20
class Char6(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        pu()
        goto(x,y)
        pd()
        left(90)
        forward(40)
        right(90)
        forward(20)
        backward(20)
        right(90)
        forward(20)
        left(90)
        for i in range(4):
            forward(20)
            right(90)
    def getWidth(self):
        return 20
class Char7(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        pu()
        goto(x,y)
        forward(20)
        pd()
        left(90)
        forward(40)
        left(90)
        forward(20)
        right(180)

    def getWidth(self):
        return 20
class Char8(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        pu()
        goto(x,y)
        pd()
        for i in range(2):
            forward(20)
            left(90)
            forward(40)
            left(90)
        left(90)
        forward(20)
        right(90)
        forward(20)
    def getWidth(self):
        return 20
class Char9(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        pu()
        goto(x,y)
        pd()
        forward(20)
        left(90)
        forward(20)
        left(90)
        for i in range(4):
            forward(20)
            right(90)
        right(180)        
    def getWidth(self):
        return 20
ref = {"0":Char0(),"1":Char1(),"2":Char2(),"3":Char3(),"4":Char4(),"5":Char5(),"6":Char6(),"7":Char7(),"8":Char8(),"9":Char9()}
meow = input("Enter a number to draw: ")
acc = 0
for i in meow:
    try:
        ref[i].draw(acc,0)
        acc += ref[i].getWidth() + 10
    except:
        print(f"{i} is not a number unable to draw")
        continue
done()
#Q6
class StationaryGood:
    def __init__(self,amount = 0,price = 0,Name = "") -> None:
        self.name = Name
        self.amount = amount
        self.price = price
    def getPrice(self) -> int:
        pass
class Magazine(StationaryGood):
    def __init__(self, amount=0, price=0,Name = "") -> None:
        super().__init__(amount, price, Name)
    def getPrice(self) -> int:
        return self.amount * self.price
class Book(StationaryGood):
    def __init__(self, amount=0, price=0, Name = "") -> None:
        super().__init__(amount, price, Name)
    def getPrice(self) -> int:
        return self.price * 0.9 * self.amount
class Ribbon(StationaryGood):
    def __init__(self, amount=0, Name="") -> None:
        self.amount = amount
        self.name = Name
    def getPrice(self) -> int:
        return self.amount * 5
def getTotalCost(basket:list):
    acc = 0
    for i in basket:
        acc += i.getPrice()
    return acc
basket = [Magazine(3,70,"Computer World"),Book(2,200,"Windows 7 for beginners"),Ribbon(10,"Blue")]
print(getTotalCost(basket))
