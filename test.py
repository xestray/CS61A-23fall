class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """Subtrack amount from balance."""
        if amount>self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance
    
class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount+self.withdraw_fee)