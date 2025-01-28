class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initialAmount,accName):
        self.balance=initialAmount
        self.name=accName
        print(f"\nAccount'{self.name}' created.\nBalance-${self.balance:.2f}")
    def getBalance(self):
        print(f"\nAccount'{self.name}'Balance=${self.balance:.2f}")
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"\nDeposit complete")
        self.getBalance()
        
    def viableTranction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\nsorry, Account'{self.name}'only has a balance of ${self.balance:.2f}")
      
           
    def Withdraw(self,amount):
        try:
            self.viableTranction(amount)
            self.balance=self.balance-amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
            
    def transfer(self,amount,account):
        try:
            print('\n**************\n\nBegining Transfer.. 🚀')
            self.viableTranction(amount)
            self.Withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!✅\n\n************')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌{error}')
            
class InterestRewardsAcct(BankAccount):  #InterestRewardsAcct class inherits the BankAccount calss
    def deposit(self, amount):
        self.balance=self.balance +(amount *1.05)
        print("\n Deposit complete.")
        self.getBalance()

class Savingsacct(InterestRewardsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5
        
    def Withdraw(self, amount):
        try:
            self.viableTranction(amount + self.fee)
            self.balance=self.balance - (amount +self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw interrupted:{error}')