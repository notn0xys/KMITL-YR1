class test():
    def __init__(self,x):
        self.val = x
    def test(self):
        print(f"test test {self.val}")
class test_case(test):
    def __init__(self,x):
        super().__init__(x)
    def test(self):
        print(f"test_case test {self.val}")
        super().test()
def main():
    x = test_case(5)
    x.test()
main()