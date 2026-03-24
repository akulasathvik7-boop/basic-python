class Account:
    def __init__(self):
        self.total_amount=10
    def deposit(self,total_amount):
        self.total_amount+=total_amount
        print(f"total amount in account {self.total_amount}")
        print(f"deposited amount in account {total_amount}")
    def withdraw(self,withdraw_amount):
        self.total_amount-=withdraw_amount
        print(f"total amount in account {self.total_amount}")
        print(f"withdraw amount in account {withdraw_amount}")
obj1=Account()
obj1.deposit(20000)
obj1.withdraw(20000)