class BankAccount():
    def __init__(self):
        self.balance=0

    def put_money(self,money):
        self.balance+=money

    def get_money(self,money):
        if self.balance>=money:
            self.balance-=money
        else:
            print("The transaction was declined due to insufficient funds.")

class SavingAccounts(BankAccount):
    def __init__(self,min_money):
        BankAccount.__init__(self)
        self.min_balance=min_money

    def get_money(self,money):
        if self.balance-money>=self.min_balance:
            self.balance-=money
            print("Your withdrawal was successful.")
        else:
            print("The transaction was declined due to insufficient funds.")

savings=SavingAccounts(1900)
savings.put_money(5000)
savings.get_money(3100)
print(savings.balance)