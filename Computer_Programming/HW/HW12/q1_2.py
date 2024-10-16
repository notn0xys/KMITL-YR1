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
        right(20)
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