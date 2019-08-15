####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.




class Account():
    def __init__(self,owner,balance ):

        self.owner = owner
        self.balance = balance
    def __repr__(self):
        return  f"Account Owner: {self.owner}, Balance:{self.balance}"
        
    def deposit(self,money):
        self.balance = self.balance + money

        return f'Deposit done by: {money}$ bucks!'

    def withdraw(self,money):
        if self.balance < money:
            return "ERROR: Funds not available."
        newBalance = self.balance - money
        self.balance = newBalance
        return f'Withdraw done by: {money}$ bucks'


# 1. Instantiate the class

acct1 = Account('Mike',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
print(acct1.owner)




# 4. Show the account balance attribute
print(acct1.balance)




# 5. Make a series of deposits and withdrawals
print(acct1.deposit(50))

print(acct1.balance)




print(acct1.withdraw(75))




# 6. Make a withdrawal that exceeds the available balance
print(acct1.withdraw(500))

