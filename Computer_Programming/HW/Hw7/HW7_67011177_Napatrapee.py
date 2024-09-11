#Q1
class Clock:
    def __init__(self):
        self.__h = 0
        self.__mins = 0
        self.__s = 0
    def set_time(self,time):
        time_split = time.split(":")
        while True:
            if len(time_split) == 3:
                break
            time_split.append("0")
        self.__h = int(time_split[0])
        self.__mins = int(time_split[1])
        self.__s = int(time_split[2])
    def get_time(self):
        return(f"{self.__h:02}:{self.__mins:02}:{self.__s:02}")
    def tick(self):
        self.__s += 1
    def display_12hr(self):
        after = ""
        if int(self.__h) >= 12:
            after = "PM"
            if self.__h != 12:
                self.__h -= 12
        else:
            after = "AM"
        print(f"{self.__h:02}:{self.__mins:02}:{self.__s:02} {after}")
clock = Clock()
clock.set_time("23:04")
print(clock.get_time())
clock.display_12hr()
#Q2
def isNeg(x):
    if x < 0:
        return True
    else:
        return False
class Poly:
    def __init__(self,x) -> None:
        self.val = x
    def power(self,n):
        result = Poly((0,0))
        if n == 0:
            return Poly(tuple([1]))
        elif n > 0:
            temp = self
            for i in range(n - 1):
                temp = temp.multiply(self)
            result = result.add(temp)
            return result
        else:
            print("Cant Take power of negative")
            return False
    def multiply(self,p):
        list1 = list(self.val)
        result = Poly((0,0,0))
        for i in range(len(list1)):
            if list1[i] != 0:
                temp = p.scalar_multiply(list1[i])
                temp_list = list(temp.val)
                for j in range(i):
                    temp_list.insert(0,0)
                result = result.add(Poly(tuple(temp_list)))
        return result
    def scalar_multiply(self,x):
        l = list(self.val)
        for i in range(len(l)):
            l[i] *= x
        return Poly(tuple(l))        
    def print(self):
        counter = 0
        val = list(self.val)
        for i in range(len(val)):
            if val[i] != 0:
                if counter == 0:
                    if i == 0:
                        print(f"{val[i]} ", end="")
                    elif i == 1:
                        print(f"{val[i]}x ",end="")
                    else:
                        print(f"{val[i]}x^{i} ",end="")
                    counter += 1
                else:
                    if isNeg((val[i])):
                        print("- ",end="")
                    else:
                        print("+ ",end="")
                    if i == 1:
                        print(f"{abs(val[i])}x ",end="")
                    else:
                        print(f"{abs(val[i])}x^{i} ",end="")
            if i == len(val) - 1:
                print()      
    def add(self,p):
        i = 0
        is1onger = True
        obj_1 = list(self.val)
        obj_2 = list(p.val)
        while i < len(obj_1) and i < len(obj_2):
            if len(obj_1) > len(obj_2):
                is1onger = True
                obj_1[i] += obj_2[i]
            else: 
                is1onger = False
                obj_2[i] += obj_1[i]
            i += 1
        if is1onger:
            return Poly(tuple(obj_1))
        else:
            return Poly(tuple(obj_2))
    def eval(self,x):
        result = 0
        for i in range(len(self.val)):
            result += self.val[i] * (x**i)
        print(result)
    def diff(self):
        return_list = []
        for i in range(1,len(self.val)):
            return_list.append(self.val[i] * i)
        return Poly(tuple(return_list))
    def integrate(self):
        return_list = list(self.val)
        for i in range(len(return_list)):
            return_list[i] = round(return_list[i] / (i + 1),2)
        return_list.insert(0,0)
        return Poly(tuple(return_list))
l = Poly((1,0,-2))
q = l.power(2)
l.power(1).print()
l.power(0).print()
l.power(3).print()
p = Poly((1,0,0,0,2))
m = Poly((1,1))
h = p.multiply(m)
h.print()
h.integrate().print()
lol  = h.integrate()
lol.diff().print()
l.power(10).print()
#Q3
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
