class BankAccount:
    def __init__(self, name: str, account_num: int):
        self.__name = name
        self.__account_num = account_num
        self.__balance = 0

    @property
    def name(self)-> str:
        return self.__name

    @name.setter
    def name(self, new_name)-> None:
        self.__name = new_name

    @property
    def account_num(self)-> int:
        return self.__account_num

    @account_num.setter
    def account_num(self, new_num)-> None:
        self.__account_num = new_num

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, new_balance: int)-> None:
        self.__balance = new_balance

    def withdrawal(self, amount: int)-> None:
        if amount <= 0:
            print("Error!")
        if self.__balance - amount < 0:
            print("Error!")
        else:
            self.__balance -= amount

    def deposit(self, amount: int)-> None:
        if amount <= 0:
            print("Error: Deposit amount must be positive!")
            return
        self.__balance += amount

    def __str__(self)-> str:
        return f"Hello mr. {self.__name} account number: {self.__account_num}, your balance is: {self.__balance}"

acc = BankAccount("Menachem", 12345)
acc.deposit(1000)
acc.withdrawal(300)
acc.deposit(-50)
print(acc)