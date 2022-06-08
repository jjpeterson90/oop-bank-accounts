
from ctypes import ArgumentError
from logging import exception


import csv
import os.path
from re import L
from unicodedata import name

class Bank:
    
    def __init__(self):
        self.accounts = []
        pass
    
    @classmethod
    def accounts(self):
        return self.accounts
    
    # def create_account(self, ID, initial_deposit):
    #     accounts = []
        
    #     pass

class Account(Bank):

    def __init__(self, ID, initial_deposit, time):
        # New account cannot be created with an initial negatie balance
        if int(initial_deposit) < 0:
            raise ValueError('New account cannot have a negative balance')
        self.id = ID
        self.current_balance = initial_deposit
        self.time = time
        
    def import_accounts(self):
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../support/accounts.csv")
        
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                accounts.append(Account(**dict(row)))
                
        return accounts
    
    # def id(self):
    #     return self.id
    
    def all_accounts(self):
        return Bank.accounts()
    
    def find(self, ID):
        for this_account in self.all_accounts():
            if this_account.id == ID:
                return this_account
    
    def withdraw(self, amount):
        # Must not allow the account to go negative
        if self.current_balance - amount:
            raise ValueError('Withdrawals cannot result in a negative balance')
        self.current_balance -= amount
        print(f'You withdrew ${amount}. Your new balance is {self.current_balance}')
        return self.current_balance
    
    def deposit(self, amount):
        self.current_balance += amount
        print(f'You deposited ${amount}. Your new balance is {self.current_balance}')
        return self.current_balance
    
    def balance(self):
        return self.current_balance
    
class Savings(Account):
    
    def __init__(self, ID, initial_deposit, time):
        super().__init__(ID, initial_deposit, time)
        if initial_deposit < 10:
            raise ArgumentError(f'Must deposit more than {initial_deposit} to start')
        self.current_balance = initial_deposit
        self.interest_rate = 0.25
    
    def withdraw(self, amount):
        # Must not allow the account to go negative
        if self.current_balance - (amount + 2) < 10:
            raise ValueError('Withdrawals cannot result in a negative balance')
        self.current_balance -= (amount + 2)
        print(f'You withdrew ${amount} and incurred a $2 fee. Your new balance is {self.current_balance}')
        return self.current_balance
        
    def add_interest(self):
        self.current_balance += self.current_balance * self.interest_rate/100
        
class Checking(Account):
    
    def __init__(self, ID, initial_deposit, time, initial_balance):
        super().__init__(ID, initial_deposit, time, initial_balance)
        
class Owner(Account):
    
    def __init__(self, ID, last_name, first_name, street, city, state):
        self.id = ID
        self.last_name = last_name
        self.first_name = first_name
        self.street = street
        self.city = city
        self.state = state
    
    @classmethod
    def objects(cls):
        owners = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../support/owners.csv")
        
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                owners.append(Owner(**dict(row)))
                
        return owners
    
    # def match_owners_to_accounts(self, id):
    #     my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = os.path.join(my_path, "../support/account_owners.csv")
        
    #     with open(path) as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             if row['accountid'] == id:
    #                 self.ownerid = row['ownerid']
    #                 return self.ownerid
                
                # owners.append(Owner(**dict(row)))