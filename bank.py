from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, initial_balance):
        new_account = Account(account_number, initial_balance)
        self.accounts[account_number] = new_account
        print(f'Account {account_number} created with an initial balance of ${initial_balance:.2f}.')

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            print(f'${amount:.2f} deposited into account {account_number}.')
        else:
            print(f'Account {account_number} not found.')

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number].withdraw(amount):
                print(f'${amount:.2f} withdrawn from account {account_number}.')
            else:
                print('Insufficient funds.')
        else:
            print(f'Account {account_number} not found.')

    def view_balance(self, account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number])
        else:
            print(f'Account {account_number} not found.')
