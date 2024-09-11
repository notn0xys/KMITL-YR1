class Linear_Equations:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__d
    def getE(self):
        return self.__e
    def getF(self):
        return self.__f
    def isSolvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) != 0:
            return True
        else:
            return False
    def getX(self):
        if self.isSolvable():
            return ((self.__e * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c))
        else:
            return None
    def getY(self):
        if self.isSolvable():
            return ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c))
        else:
            return None
p = Linear_Equations(3,2,5,6,3,76)
print(p.getX())
print(p.getY())