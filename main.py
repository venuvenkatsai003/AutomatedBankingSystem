from bank import Bank
import user_interface as ui

def main():
    bank = Bank()
    
    while True:
        ui.display_menu()
        choice = ui.get_choice()
        
        if choice == '1':
            account_number, initial_balance = ui.get_account_details()
            bank.add_account(account_number, initial_balance)
        elif choice == '2':
            account_number, amount = ui.get_transaction_details()
            bank.deposit(account_number, amount)
        elif choice == '3':
            account_number, amount = ui.get_transaction_details()
            bank.withdraw(account_number, amount)
        elif choice == '4':
            account_number = input("Enter account number: ")
            bank.view_balance(account_number)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
