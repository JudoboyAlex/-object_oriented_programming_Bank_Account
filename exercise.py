class BankAccount:

    def __init__(self,balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def __str__(self):
        return "Currently, you have ${} with rate of {}%.".format(self.balance, self.interest_rate)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def gain_interest(self, rate):
        self.balance = self.balance * (1+rate/100)
        return self.balance

my_account = BankAccount(5000, 10)

print(my_account.deposit(30))
print(my_account.withdraw(20))
print(my_account.gain_interest(10)) 