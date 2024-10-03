import math
class point:
    def __init__(self,x = 0 ,y= 0) -> None:
        self.x = x
        self.y = y
    def printinfo(self):
        print(f'(X:{self.x},Y:{self.y})')
class circle(point):
    def __init__(self,x,y,r = 0) -> None:
        super().__init__(x,y)
        self.r = r
    def Area(self):
        return self.r * self.r * math.pi
    def printinfo(self):
        print(f"Position X:{self.x}, Y:{self.y} , Radius{self.r} , Area: {self.Area()}")
def main():
    x = circle(10,10,10)
    x.printinfo()
main()