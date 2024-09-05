import math as nyah
class quadEqua:
    def __init__(self,a,b,c) -> None:
        self.__a = a
        self.__b = b
        self.__c = c
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getdiscriminant(self):
        x = (self.__b**2) - (4 * self.__a * self.__c)
        return x
    def getRoot1(self):
        if self.getdiscriminant() < 0:
            return 0
        else:
            r1 = ((-1 * self.__b) + nyah.sqrt(self.getdiscriminant())) / (self.__a * 2)
            return r1
    def getRoot2(self):
        if self.getdiscriminant() < 0:
            return 0
        else:
            r2 = ((-1 * self.__b) - nyah.sqrt(self.getdiscriminant())) / (self.__a * 2)
            return r2
first_ques =quadEqua(4,5,6)
print(f"{first_ques.getA()} {first_ques.getB()} {first_ques.getC()}")
print(first_ques.getdiscriminant())
print(first_ques.getRoot1())
print(first_ques.getRoot2())