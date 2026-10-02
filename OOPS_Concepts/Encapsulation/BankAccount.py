class BankAccount:
    # __balance is a private variable
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def getBalance(self):
        return self.__balance
    
class Employee:
    def __init__(self):
        self.__bankBalance = 100000

emp = Employee()
print(emp._Employee__bankBalance)
    
acc = BankAccount(1000)
acc.deposit(5000)
print(acc.getBalance())