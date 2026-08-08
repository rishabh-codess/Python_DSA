class Bankaccount:
    def __init__(self, owner, bankbalance=0):
        self.owner=owner
        self.bankbalance= bankbalance

    def deposite(self, amount):
        self.bankbalance += amount
        print(f"{amount} new bankbalance is {self.bankbalance}")

    def withdraw(self, amount):
        if amount<self.bankbalance:
            print(f"{amount} insufficient funds! {self.bankbalance}")
        else:
            self.bankbalance-=amount
            print(f"{amount} is succesfully withdrawn .new balance is {self.bankbalance} ")
    def get_bankbalance(self):
        return self.bankbalance

account=Bankaccount("rishabh",5000)
print (account.bankbalance)
account.deposite(500)
print (account.bankbalance)
account.withdraw (1000)