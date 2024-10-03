class Name:
    def __init__(self,t= "",f = "",l ="") -> None:
        self.t = t
        self.f = f
        self.l = l
    def set_name(self,t= "",f = "",l =""):
        self.t = t
        self.f = f
        self.l = l
    def getFullName(self):
        return f"{self.t} {self.f} {self.l}"
class Date:
    def __init__(self,d = 1,m = 1,y = 2000) -> None:
        if d not in range(1,32):
            ValueError
        else:
            self.d = d
        if m not in range(1,13):
            ValueError
        else:
            self.m = m
        self.y = y
    def setDate(self,d = 1,m = 1,y = 2000) -> None:
        if d not in range(1,32):
            ValueError
        else:
            self.d = d
        if m not in range(1,13):
            ValueError
        else:
            self.m = m
        self.y = y
    def Date(self) -> str:
        return f"{self.d}/{self.m}/{self.y}"
    def DateBc(self) -> str:
        return f"{self.d}/{self.m}/{self.y + 543}"
class Adress:
    def __init__(self,h = "",s = "",d = "",ct = "",c = "",pt = "") -> None:
        self.house = h
        self.street = s
        self.district = d
        self.city = ct
        self.country = c
        self.postcode = pt
    def setAdress(self,h = "",s = "",d = "",ct = "",c = "",pt = "") -> None:
        self.house = h
        self.street = s
        self.district = d
        self.city = ct
        self.country = c
        self.postcode = pt
    def getAdress(self):
        return f"{self.house} {self.street} {self.district} {self.city} {self.country} {self.postcode}"
class Person():
    def __init__(self,N:Name,bd:Date,add:Adress) -> None:
        self.name = N.getFullName()
        self.birthdate = bd.Date()
        self.adress = add.getAdress()
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Bithdate: {self.birthdate}")        
        print(f"Adress: {self.adress}")
class Employee(Person):
    def __init__(self, N: Name, bd: Date, add: Adress, startdate = "" , department = "") -> None:
        super().__init__(N, bd, add)
        self.dp = department
        self.startdate = startdate
        
    def print_info(self):
        super().print_info()
        print(f"Department: {self.dp}")
        print(f"Start Date: {self.startdate}")
    def change_department(self, x):
        self.dp = x
class TempEmployee(Employee):
    def __init__(self, N: Name, bd: Date, add: Adress, startdate="", department="", wage = 0) -> None:
        super().__init__(N, bd, add, startdate, department)
        self.wage = wage
        self.status = False
    def print_info(self):
        super().print_info()
        print(f"Status: Temporary Employee")
        print(f"Wage: {self.wage}")
    def get_status(self):
        return self.status
class PermEmployee(Employee):
    def __init__(self, N: Name, bd: Date, add: Adress, startdate="", department="", wage = 0) -> None:
        super().__init__(N, bd, add, startdate, department)
        self.status = True
        self.salary = wage
    def print_info(self):
        super().print_info()
        print(f"Status: Permanent Employee")
        print(f"Salary: {self.salary}")
    def get_status(self):
        return self.status
class Department():
    def __init__(self,d = "One of the departments of all time", name = "") -> None:
        self.name = name
        self.description = d
        self.manager = "None"
        self.employeelist = []
    def addEmployee(self, x):
        x.change_department(self.name)
        self.employeelist.append(x.name)
    def deleteEmployee(self, x):
        x.change_department("Not in a department")
        self.employeelist.remove(x.name)
    def setManager(self,x):
        if x.get_status() and x.name in self.employeelist:
            self.manager = x.name
        else:
            print("Missing Requirements cant be manager")
    def print_info(self):
        print(f"Description: {self.description} , Manager: {self.manager} , employee list: {self.employeelist}")

x = Name("Mr", "John", "Pork")
y = Date(15,6,2023)
addy = Adress("45","Wok")
L = PermEmployee(x,y,addy,"15 Aug 2024","", 100)
L.print_info()
cat = Department("yea","cat")
cat.addEmployee(L)
cat.print_info()
L.print_info()
cat.setManager(L)
cat.print_info()


