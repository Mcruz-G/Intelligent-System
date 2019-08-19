"""This module contains a code example related to

   the assignment 1 of the CS4000 Intelligent Systems course
   
   Date: August 19, 2019
   Authors: A01037093 Campus: MTY
            A0... ... Campus: ...
"""

class Bank():
    """Represents a savings bank, a financial institution for savings accounts.

    attributes: ..."""

    # add methods ...
    
    def __init__(self,name = 'Unnamed'):
        self.name = name
        self.clients = []
        self.noname = 1
    def __repr__(self):
        return  f"bank: {self.name}, clients:{self.clients}"
    
    
    def deposit(self, user = None, amount = 200):

        if not user:
            clientNumber = self.noname
            user = 'client'+ str(clientNumber)
            self.noname += 1
        self.clients.append((user,amount))


def consult(self, user):
    
    for name, money in self.clients:
        if user == name:
            return print(f'{user} has {money} in its {self.name} savings account')

    return print(f'Error: {user} is not a client of {self.name} bank')
    
def withdraw(self,user,amount):

    for name, money in self.clients:
        if user == name:
            index = self.clients.index((user,money))
            self.clients[index] = (user, money - amount)
            return print(f'{user} withdrew {amount} from its {self.name} savings account')

    return print(f'Error: {user} is not a client of {self.name} bank')
    

def cancel(self,user):

    for name, money in self.clients:
        
        if user == name:
            self.clients.remove((name, money))
            return print(f'{user} canceled its {self.name} savings account')
        
    return print(f'Error: {user} is not a client of {self.name} bank')

def report(self, lt = None, gt = None, clients = None ):
    
    if clients:
        for client in clients:
            nameList = list(filter( lambda x: client in x, self.clients ))
            if len(nameList) == 0:
                print(f'Error: {client} is not a client of {self.name} bank')

    print('----------------------------------')
    print(f'| * {self.name} bank savings accounts * |')
    print('----------------------------------')
    print('| Client             | Balance   |')
    print('----------------------------------')
    totalMoney = 0

    if not lt and not gt and not clients:
        for name, money in self.clients:
            print(f'| {name}            | $   {money} |')
            
            totalMoney += money
        
    if lt:
        for name, money in self.clients:
            if money < lt:
                print(f'| {name}            | $   {money} |')
                
                totalMoney += money

    if gt:
        for name, money in self.clients:
            if money > gt:
                print(f'| {name}            | $   {money} |')
                
                totalMoney += money

    if clients:
        for client in clients:
            for name, money in self.clients:
                if name == client:
                    print(f'| {name}            | $   {money} |')
                    
                    totalMoney += money
            
    print('----------------------------------')
    print(f'|              Total | $   {totalMoney} |')
    print('----------------------------------')
    
    
        
    
def cancel_clients(self, clientsList):
    for client in clientsList:
        cancel(self,client)

def add_clients(self, clientsList):

    deposit = 0
    newClients = 0

    for clientInfo in clientsList:

        if type(clientInfo) == int:
            clientNumber = self.noname
            userName = 'client'+ str(clientNumber)
            self.noname += 1
            self.clients.append((userName,clientInfo))
            newClients += 1
        
        elif type(clientInfo) == tuple:

            nameList = list(filter( lambda x: clientInfo[0] in x, self.clients ))
            if len(nameList) != 0:
                index = self.clients.index(nameList[0])
                self.clients[index] = (nameList[0][0], nameList[0][1] + clientInfo[1])
                deposit += 1
            else:
                self.clients.append(clientInfo)
                newClients += 1

    return print(f'Added {newClients} new clients and {deposit} deposit to {self.name} bank\n '), print(self)


def main():
    # create an unnamed bank
    b1 = Bank()
    print(b1)
    # add a client ... by depositing an amount in the bank
    b1.deposit('pedro',100)
    print(b1)
    # create a BBVA bank
    bbva = Bank("BBVA")
    print(bbva)
    # add an unnamed client
    bbva.deposit(amount = 2000)
    print(bbva)
    # add another unnamed client
    bbva.deposit(amount = 500)
    print(bbva)
    # add Juan as a client ... by default it will deposit 200 pesos
    bbva.deposit('juan')
    print(bbva)
    # consult the balance for Lupita
    consult(bbva, 'lupita')
    # consult the balance for Juan
    consult(bbva, 'juan')
    # withdraw 50 pesos from Pedro's account
    withdraw(b1, 'pedro', 50)
    print(b1)
    # withdraw 100 pesos from Juan's account
    withdraw(b1, 'juan', 100)
    withdraw(bbva, 'juan', 100)
    print(bbva)
    # cancel the unnamed client2 account
    cancel(b1, 'client2')
    cancel(bbva, 'client2')
    print(bbva)
    # generate a full report for BBVA bank ... all clients
    report(bbva)
    # generate a report of clients that have less than 400 pesos at BBVA bank
    report(bbva, 400)
    # generate a report of clients that have more than 1000 pesos at BBVA bank
    report(bbva, gt=1000)
    # add a list of clients to BBVA bank
    add_clients(bbva, [450,('hugo',3000),1500,('isabel',750),('juan',250)])
    report(bbva)
    # cancel the accounts of a list of clients
    cancel_clients(bbva,['juan','roberto','isabel'])
    report(bbva)
    # report a list of specific clients
    report(bbva,clients=['juan','hugo','client1'])
    print("*** End ***")


if __name__ == '__main__':
    main()

