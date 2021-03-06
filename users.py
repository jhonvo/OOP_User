class User:
    
    def __init__(self,name):
        self.name = name
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw (self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print(f"Balance is not sufficient to withdraw {amount}")
    
    def transfer(self, destination, amount):
        if amount < self.balance:
            self.balance -= amount
            destination.balance += amount
        else:
            print(f"Balance is not sufficient to transfer {amount}")

    def display_user_balance(self):
        print(f'User: {self.name}, Balance:{self.balance}')