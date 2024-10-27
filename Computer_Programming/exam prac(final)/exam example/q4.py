class savingsaccount:
    def __init__(self,bank_name = "", acc_name = "", acc_id = "", balance = 0):
        if balance < 0:
            print("Balance cant be negative")
            balance = 0
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.balance = balance
        self.transaction_history = []
    def deposit(self,money = 0,person = "",date = ""):
        if money < 0:
            print("cant deposit negative money")
            money = 0
        self.balance += money
        self.transaction_history.append(f"Deposit {money}$ , by {person} at {date}")
    def withdraw(self,money= 0,person = "",date = ""):
        if self.balance < money:
            print("Unable to withdraw")
            return
        else:
            self.balance -= money
            self.transaction_history.append(f"Withdraw {money}$ , by {person} at {date}")
    def get_balance(self):
        return self.balance
    def print_statement(self):
        print(self.transaction_history)
class overdrawn_account(savingsaccount):
    def __init__(self,bank_name = "", acc_name = "", acc_id = "", balance = 0,limit = 0) -> None:
        super().__init__(bank_name = "", acc_name = "", acc_id = "")
        self.balance = balance
        if limit < 0:
            print("Overdrawn limit cannot be less than 0")
            limit = 0
        self.limit = limit
    def deposit(self, money=0, person="", date=""):
        super().deposit(money, person, date)
    def withdraw(self, money=0, person="", date=""):
        if self.balance + self.limit < money:
            print("Exceed overdrawn limit")
            return
        else:
            self.balance -= money
            self.transaction_history.append(f"Withdraw {money}$ , by {person} at {date}")
    def get_balance(self):
        return super().get_balance()
    def print_statement(self):
        super().print_statement()
    


saving = savingsaccount("Nyan","Noxz","123123DZ",200)
print(saving.get_balance())
saving.deposit(500,"Jom","yesterday")
print(saving.get_balance())
saving.print_statement()
over = overdrawn_account("Nyan", "Moew", "1231312d", -200, 1000)
print(over.get_balance())
over.withdraw(700,"Moew","12/23/22")
print(over.get_balance())
over.withdraw(300)
