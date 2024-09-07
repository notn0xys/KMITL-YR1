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
        val = list(self.val)
        for i in range(len(val)):
            if val[i] != 0:
                if i == 0:
                    print(f"{val[i]} ", end="")
                elif i == 1:
                    if isNeg((val[i])):
                        print("- ",end="")
                    else:
                        print("+ ",end="")
                    print(f"{abs(val[i])}x ",end="")
                else:
                    if isNeg((val[i])):
                        print("- ",end="")
                    else:
                        print("+ ",end="")
                    print(f"{abs(val[i])}x^{i} ",end="")
            if i == len(val) - 1:
                print()      
    def add(self,p):
        i = 0
        is1onger = True
        obj_1 = list(self.val)
        obj_2 = list(p.val)
        i = 0
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
        return result
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
h = p.multiply(m).print()
mn = l.add(q)
mn.diff().print()
noxu = Poly((0,2,5))
noxu.integrate().print()