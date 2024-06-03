def display_menu():
    print("\nAutomated Banking System")
    print("1. Add Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Balance")
    print("5. Exit")

def get_choice():
    return input("Enter your choice: ")

def get_account_details():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return account_number, initial_balance

def get_transaction_details():
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount: "))
    return account_number, amount
