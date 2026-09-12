class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def get_deposit(self, amount):
        if amount<0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        if amount > self.balance:
            raise ValueError("Insufficient funds !!!")
        self.balance -= amount
        return self.balance
    
    def check_balance(self):
        return self.balance

acc1 = BankAccount("123456789", "XYZ ABC", 2500.00)
print(f"Account number : {acc1.account_number} \nOwner name : {acc1.owner_name} \nBalance : {acc1.balance}")
print(f"Deposited amount : {acc1.get_deposit(1500)}")
print(f"Withdraw amount : {acc1.withdraw(500)}")
print(f"Available balance : {acc1.check_balance()}")