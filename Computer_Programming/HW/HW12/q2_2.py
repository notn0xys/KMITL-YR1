class StationaryGood:
    def __init__(self,amount = 0,price = 0,Name = "") -> None:
        self.name = Name
        self.amount = amount
        self.price = price
    def getPrice(self) -> int:
        pass
class Magazine(StationaryGood):
    def __init__(self, amount=0, price=0,Name = "") -> None:
        super().__init__(amount, price, Name)
    def getPrice(self) -> int:
        return self.amount * self.price
class Book(StationaryGood):
    def __init__(self, amount=0, price=0, Name = "") -> None:
        super().__init__(amount, price, Name)
    def getPrice(self) -> int:
        return self.price * 0.9 * self.amount
class Ribbon(StationaryGood):
    def __init__(self, amount=0, Name="") -> None:
        self.amount = amount
        self.name = Name
    def getPrice(self) -> int:
        return self.amount * 5
def getTotalCost(basket:list):
    acc = 0
    for i in basket:
        acc += i.getPrice()
    return acc
basket = [Magazine(3,70,"Computer World"),Book(2,200,"Windows 7 for beginners"),Ribbon(10,"Blue")]
print(getTotalCost(basket))
