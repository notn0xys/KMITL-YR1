import math
class Calc():
    def __init__(self,x = 0.00) -> None:
        self.val = x
    def set_accumulator(self,x):
        self.val = x
    def get_accumulator(self) -> float:
        return self.val
    def add(self,x):
        self.val += x
    def subtract(self,x):
        self.val -= x
    def multiply(self,x):
        self.val *= x
    def divide(self,x):
        self.val /= x
    def print_result(self):
        print(f"Result: {self.val}")
class Sci_calc(Calc):
    def __init__(self, x=0) -> None:
        super().__init__(x)
    def square(self):
        self.val = self.val * self.val
    def expo(self,x):
        self.val = self.val ** x
    def factorial(self):
        self.val = math.factorial(self.val)
    def print_result(self):
        return super().print_result()
def main():
    calc = Calc()
    sci_calc = Sci_calc()
    calc.add(10)
    calc.divide(2)
    calc.print_result()
    sci_calc.add(10)
    sci_calc.factorial()
    sci_calc.print_result()
main()

