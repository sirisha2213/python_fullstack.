#data abstraction
from abc import ABC,abstractmethod
class bankaccount:
    def checkbalance(self):
        print('you can checkout you balance')
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass

class savingaccount(bankaccount):
    def deposit(self):
        print('2 lakhs per day')
    def withdraw(self):
        print('1 lakh per day')
        
class currentaccount(bankaccount):
    def deposit(self):
        print('unlimited deposit')
    def withdraw(self):
        print('unlimited withdrawal')

class jointaccount(bankaccount):
    def deposit(self):
        print('only those 2 can deposit')
    def withdraw(self):
        print('1-2 lakh per day')
class salaryaccount(bankaccount):
    def deposit(self):
        print('no limit')
    def withdraw(self):
        print('20000-1lakh perday')
class pensionaccount(bankaccount):
    def deposit(self):
        print('no deposit')
    def withdraw(self):
        print('40k per day')

print('---------------sirisha------------')
sirisha = savingaccount()
sirisha.checkbalance()
sirisha.deposit()
sirisha.withdraw()
print('---------------sanjana------------')              
sanjana = currentaccount()
sanjana.checkbalance()
sanjana.deposit()
sanjana.withdraw()
print('-------------bhavana_varsha--------------')
bhavana_varsha = jointaccount()
bhavana_varsha.checkbalance()
bhavana_varsha.deposit()
bhavana_varsha.withdraw()

print('-------------siri--------------')

siri = salaryaccount()
siri.checkbalance()
siri.deposit()
siri.withdraw()
print('-------------meetiru--------------')
meetiru = pensionaccount()
meetiru.checkbalance()
meetiru.deposit8meetiru.withdraw()

                 
              
