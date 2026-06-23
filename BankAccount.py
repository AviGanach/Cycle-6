class BankAccount:
    def __init__(self, name, account_no):
        self.__name = name
        self.__account_no = account_no
        self.__balance = 0

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def account_no(self):
        return self.__account_no
    @account_no.setter
    def account_no(self, account_no):
        self.__account_no = account_no

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            self.__balance -= self.__balance
            print("You don't have enough money")

    def __str__(self):
        return f"name holder: {self.__name}, account number {self.__account_no}, balance: {self.__balance}"