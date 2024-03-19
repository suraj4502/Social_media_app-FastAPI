def add(n1: int, n2: int):
    return n1 + n2


def divide(n1: int, n2: int):
    return n1 / n2

class BankAccount():
    def __init__(self, starting_balance :float =0) -> None:
        self.balance = starting_balance
    
    def deposit(self, amount : float):
        self.balance += amount
        
    def withdraw(self, amount : float):
        self.balance -= amount
    
    def collect_interest(self):
        self.balance *= 1.1
    
    