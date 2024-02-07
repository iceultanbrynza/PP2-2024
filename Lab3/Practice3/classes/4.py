print("каспи банк взлом скачать бесплатно без смс и регистрации")
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"____________________\nLogin: {self.owner}\nAvailable money: {self.balance}$\n____________________"
    def Deposit(self, ForDepo):
        self.balance+=ForDepo
        return "Deposit accepted"
    def Withdraw(self, MinusMoney):
        if(MinusMoney <= self.balance):
            self.balance-=MinusMoney
            return f"{MinusMoney} dollars was successfully withdrawn"
        return "Request declined\nYour request exceed the balance"

login = input("Input your login: ")
balance = int(input("How much money you have: "))
Client = Account(login, balance)
print(Client)
Depo = int(input("Money for deposit: "))
print(Client.Deposit(Depo))
ToWD = int(input("Money to withdraw: "))
print(Client.Withdraw(ToWD))
