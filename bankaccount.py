class BankAccount:
    def __init__(self, name : str, account_num : int):
        self.__name = name
        self.__account_num = account_num
        self.__balance = 0

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name : str) -> None:
        self.__name = new_name

    @property
    def account_num(self) -> int:
        return self.__account_num

    @account_num.setter
    def account_num(self, new_account_num : int) -> None:
        self.__account_num = new_account_num

    def deposit(self, amount : int) -> None:
        self.__balance += amount

    def withdraw(self, amount : int) -> None:
        self.__balance -= amount if amount <= self.__balance else 0

    def __str__(self):
        return f"""Name: {self.__name}
account number: {self.__account_num}
balance: {self.__balance}"""

