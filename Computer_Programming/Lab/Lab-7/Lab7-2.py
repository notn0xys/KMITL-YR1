class BankAccount:
    def __init__(self,x,y,z,nayh) -> None:
        self.__bankname = x
        self.__accname = y
        self.__accnum = z
        self.__currbal = nayh
    def deposit(self,amt):
        self.__currbal += amt
        print("New Balance: ",self.__currbal)
    def withdraw(self,amt):
        self.__currbal -= amt
        print("New Balance: ",self.__currbal)

    def print_bal(self):
        print("Balance: ",self.__currbal)
x = BankAccount("Noxu Bank", "Noxu", 12313123, 100000)
x.deposit(200)
x.withdraw(200)
x.print_bal()