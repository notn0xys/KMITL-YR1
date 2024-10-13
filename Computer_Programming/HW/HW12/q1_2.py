from abc import ABC
from turtle import *
class Char(ABC):
    def __init__(self) -> None:
        super().__init__()
    def draw(self,x = 0,y = 0):
        pass
    def getWidth():
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
    def getWidth():
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
            forward(20)
            pu()
            goto(p)
            right(225)
            forward(10)
            pd()
    def getWidth():
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
    def getWidth():
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
        goto(p)
        forward(10)
        pd()
    def getWidth():
        return 20
class Char4(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        for i in range(2):
            forward(20)
            right(90)
            forward(50)
            right(90)
    def getWidth():
        return 20
class Char5(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        for i in range(2):
            forward(20)
            right(90)
            forward(50)
            right(90)
    def getWidth():
        return 20
class Char6(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        for i in range(2):
            forward(20)
            right(90)
            forward(50)
            right(90)
    def getWidth():
        return 20
class Char7(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        for i in range(2):
            forward(20)
            right(90)
            forward(50)
            right(90)
    def getWidth():
        return 20
class Char8(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        for i in range(2):
            forward(20)
            right(90)
            forward(50)
            right(90)
    def getWidth():
        return 20
class Char9(Char):
    def __init__(self) -> None:
        super().__init__
    def draw(self, x=0, y=0):
        for i in range(2):
            forward(20)
            left(90)
            forward(50)
            right(90)
    def getWidth():
        return 20
i = Char0()
i.draw()
i = Char1()
i.draw(30,0)
i = Char2()
i.draw(60,0)
i = Char3()
i.draw(90,0)
i = Char4()
i.draw(120,0)

done()