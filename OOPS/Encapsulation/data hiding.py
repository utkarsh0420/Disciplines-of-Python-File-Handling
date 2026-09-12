# Data Hiding - Public, Protected & Private
"""
Public - Attributes are accessible inside class as well as outside class (Everywhere)
Protected (_) - Attributes are accessible in class + subclass(Inheritance)
Private (__) - Attributes are only accessible inside class but outside the class we can access them
"""
"""class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        # self.balance = balance # Publc
        self._balance = balance # Protected
        self.__balance = balance # Private
"""
"""Protected - code"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance #protected

    def get_info(self):
        print(f"Account holder name : {self.name} and balance is {self._balance}")

acc1 = BankAccount("Chris", 60_000)
acc1.get_info()
print(acc1._balance)
acc1._balance = 80000
print(acc1._balance)

"""Private - code"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def get_info(self):
        print(f"Account holder name : {self.name} \naccount balance : {self.__balance}")

acc1 = BankAccount("Chris", 100_000)
acc1.get_info()
print(acc1.name, acc1.__balance) # Somehow it will throw error for private encapsulation because it enforce it to not get accessed outside the class
print(acc1.name, acc1._BankAccount__balance) # By using class name we can access balance (which is encapsulated via private) before class name we are using (_)

#using getter and setter method we can access private encapsulation too
class BankAccount:
    def __init__(self, name, balance):
        self.name = name 
        self.__balance = balance

    def get_balance(self): #gettr method
        # return self.__balance
        return f"Account holder name : {self.name} \naccount balance : {self.__balance}"

    def set_balance(self, NewBalance): # It is instance method and in an instance method there will be compulsory 1st parameter (self) and it can have multiple parameters in it 
        self.__balance = NewBalance #setter method BTW

acc1 = BankAccount("Chris", 100_000)
"""Following are two methods to access balance outsite the class - 1st is by getter method and 2nd is by using class name"""
# print(acc1.name, acc1.get_balance())
# print(acc1.name, acc1._BankAccount__balance)
acc1.set_balance(200_000)
print(acc1.name, acc1.get_balance())

