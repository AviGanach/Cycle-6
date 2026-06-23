class BankAccount:
    def __init__ (self, name:str , account_num:int):
        self._name = name
        self._account_num = account_num
        self._balance = 0

    @property  
    def name(self):
        return self._name
    
    @name.setter
    def name (self, name):
        self._name = name

        
    @property 
    def account_num(self):
        return self._account_num
    
    @account_num.setter
    def account_num(self, account_number):
        self._account_num = account_number
        
    
    @property  
    def balance(self):
        return self._balance
        

    @balance.setter
    def balance(self, balance):
        self._balance = balance
    


    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0:
            if self._balance - amount >= 0:
                self._balance -= amount
    

    def __str__(self):
        return f"account number is: {self._account_num}, your name is: {self._name} and your balance is: {self._balance}"


ba=BankAccount("yaakov", 1234)
ba.withdraw(100)
print (ba)