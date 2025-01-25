class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Рахунок поповнено на {amount} грн. Поточний баланс: {self.balance} грн.")
        else:
            print("Сума поповнення повинна бути більше 0.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"З рахунку знято {amount} грн. Поточний баланс: {self.balance} грн.")
            else:
                print(f"Недостатньо коштів. Поточний баланс: {self.balance} грн.")
        else:
            print("Сума зняття повинна бути більше 0.")
    def check_balance(self):
        print(f"Поточний баланс: {self.balance} грн.")
    def account_info(self):
        print(f"Власник рахунку: {self.account_holder}")
        print(f"Баланс: {self.balance} грн.")
my_account = BankAccount("Руслан", 1000)
my_account.account_info()
my_account.deposit(500)
my_account.withdraw(300)
my_account.check_balance()
my_account.withdraw(2000)  
