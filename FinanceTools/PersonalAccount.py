"""
PersonalAcount.py
    Script to generate bank account objects 
"""

# Nonstandard Imports 
import datetime
import numpy as np 
import pandas as pd 



class Account:
    """
    Creates a bank account for a specific user  
    """

    def __init__(self, initial_balance: float = 0) -> None:
        """
        Create 
        
        """
        self.balance = initial_balance
        self.statement = pd.DataFrame(columns=['Date',' Time', 'Current Balance','Balance Change'])
        self.statement.loc[len(self.statement)] = [datetime.datetime.now().date(), datetime.datetime.now().strftime('%H:%M'), str(initial_balance), 0]

    def deposit(self, deposit_amount: float) -> None:   
        """Deposit an amount of money into the account"""
        self.balance += deposit_amount
        self.statement.loc[len(self.statement)] = [datetime.datetime.now().date(), datetime.datetime.now().strftime('%H:%M'), str(self.balance), '+' + str(deposit_amount)]

    def withdraw(self, withdraw_amount: float) -> None:
        """Withdraw an amount of money from the account"""
        if withdraw_amount > self.balance:
            raise ValueError('Withdraw request exceeds account balance')
        self.balance -= withdraw_amount
        self.statement.loc[len(self.statement)] = [datetime.datetime.now().date(), datetime.datetime.now().strftime('%H:%M'), str(self.balance), '+' + str(withdraw_amount)]

    def return_statement(self):
        """See current bank statement"""
        return self.statement


    


if __name__ == '__main__':
    account_1 = Account(10)
    account_1.deposit(10)
