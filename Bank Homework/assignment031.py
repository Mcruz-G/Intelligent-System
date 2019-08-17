"""This module contains a code example related to

   the assignment 1 of the CS4000 Intelligent Systems course
   
   Date: August .., 2019
   Authors: A0... ... Campus: ...
            A0... ... Campus: ...
"""

class Bank:
    """Represents a savings bank, a financial institution for savings accounts.

    attributes: ..."""

    def __init__(self, bank='Unnamed'):
        self.bank = bank
        self.clients = []

    def __str__(self):
        return str(self.__dict__)    
    # add methods ...

    def deposit(self, client='undefined', amount=200):
        for item in self.clients:
            if client == item[0]:
                amount += item[1]
                self.clients.remove(item)
        self.add(client,amount)

    def add(self, client='undefined', amount=200):
        count = 1
        if client == 'undefined':
            for item in self.clients:
                    if 'client' in item[0]:
                        count += 1
            client = 'client{}'.format(count)
        self.clients.append(tuple((client, amount)))

def consult(bankobj, client):
    find = 0
    for item in bankobj.clients: 
        if item[0] == client:
            print("{} has {} in its {} savings account".format(client,item[1],bankobj.bank))
            find = 1
    if find != 1:
        print('Error: {} is not a client of {} bank'.format(client,bankobj.bank))
    
def withdraw(bankobj, client, amount):
    found = 0
    for item in bankobj.clients:
        if client == item[0]:
            amount = item[1] - amount
            bankobj.clients.remove(item)
            print('{} withdrew {} from its {} savings account'.format(client,amount,bankobj.bank))
            bankobj.clients.append(tuple((client, amount)))
            found = 1
    if found != 1:
        print('Error: {} is not a client of {} bank'.format(client,bankobj.bank))
            
def cancel(bankobj, client):
    found = 0
    for item in bankobj.clients:
        if client == item[0]:
            bankobj.clients.remove(item)
            print('{} canceled its {} savings account'.format(client,bankobj.bank))
            found = 1
    if found != 1:
        print('Error: {} is not a client of {} bank'.format(client,bankobj.bank))

def report(bankobj, amount=float("inf"), gt=0, clients=[]):
    if not clients: 
        clients = dict(bankobj.clients).keys()
    print('----------------------------------')
    print('| * {} bank savings accounts * |'.format(bankobj.bank))
    print('----------------------------------')
    print('| Client             | Balance   |')
    print('----------------------------------')
    total = 0
    for item in bankobj.clients:
        if (item[0] in clients) and (item[1] <= amount) and (item[1] >= gt):
            print('| {:18} | $ {:7,} |'.format(item[0],item[1]))
            total += item[1]
    print('----------------------------------')
    print('|              Total | $ {:7,} |'.format(total))
    print('----------------------------------')
            
def add_clients(bankobj, clients):
    for item in clients:
        if type(item) == int:
            bankobj.deposit(amount=item)
        else:
            bankobj.deposit(item[0],item[1])

def cancel_clients(bankobj, clients):
    for item in clients:
        cancel(bankobj,item)

def main():
    # create an unnamed bank
    b1 = Bank()
    print(b1)
    # > {bank: 'Unnamed', clients: []}
    # add a client ... by depositing an amount in the bank
    b1.deposit('pedro',100)
    print(b1)
    # > {bank: 'Unnamed', clients: [('pedro',100)]}
    # create a BBVA bank
    bbva = Bank("BBVA")
    print(bbva)
    # > {bank: 'BBVA bank', clients: []}
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
