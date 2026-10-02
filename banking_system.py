import random
from datetime import datetime

accounts = {}
def create_account():
    name = input("Enter your name: ")
    phone = input("Enter your number: ")
    pin = ("Create a 4 digit pin: ")

    account_number = random.randint(10000000, 99999999)
    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0,
        "history": []
    }

    print("\nAccount created successfully")
    print("Your Account Number:", account_number)

def login():
    account_number = input("Enter your Account Number: ")
    pin = input("ENTER YOU PIN: ")

    account_number = int(account_number)

    if account_number in accounts:
        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,",accounts[account_number]["name"])
            return account_number
        else:
            print("Incorrect PIN!")
    else:
        print("Account number not found!")
    return None

def account_menu(account_number):
    while True:
        print("\n=========== ACCOUNT MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is:", accounts[account_number]["balance"])

        elif choice =="2":
            deposit(account_number)

        elif choice =="3":
            withdraw(account_number)

        elif choice =="4":
            transfer(account_number)

        elif choice =="5":
            transaction_history(account_number)

        elif choice =="6":
            change_pin(account_number)

        elif choice =="7":
            print("\nLogged out successfully!")
            break
        else:
            print("This option will be added next.")

def deposit(account_number):
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        accounts[account_number]["balance"] += amount
        time = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")

        transaction = f"{time} - Deposited ${amount:.2f}"
        accounts[account_number]["history"].append(transaction)

        print("Deposited successful!")
        print("New balance:", accounts[account_number]["balance"])

    else:
        print("Amount must be greater than 0.")

def withdraw(account_number):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Amount must be greater than 0.")

    elif amount > accounts[account_number]["balance"]:
        print("Insufficient balance!")

    else:
        accounts[account_number]["balance"] -= amount

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        transaction = f"{time} - withdrawn ${amount:.2f}"
        accounts[account_number]["history"].append(transaction)

        print("Withdrawal successful!")
        print("New balance:", accounts[account_number]["balance"])

def transfer(account_number):
    receiver = input("Enter receiver account number: ")
    receiver = int(receiver)

    if receiver not in accounts:
        print("Receiver account not found!")
        return

    if receiver == account_number:
        print("You cannot transfer the money to your own account!")
        return
    amount = float(input("Enter the amount to transfer: "))

    if amount <= 0:
        print("Amount must be greater than 0")

    elif amount > accounts[account_number]["balance"]:
        print("Insufficient balance!")

    else:
        accounts[account_number]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        sender_transaction = (
            f"{time} - Transferred ${amount:.2f} to Account {receiver}"
        )

        receiver_transaction = (
             f"{time} - received ${amount:.2f} to Account {receiver}"
        )

        accounts[account_number]["history"].append(sender_transaction)
        accounts[receiver]["history"].append(receiver_transaction)

        print("Transfer successful!")
        print("New balance:", accounts[account_number]["balance"])

def transaction_history(account_number):
    history = accounts[account_number]["history"]

    print("\n========== TRANSACTION HISTORY ==========")

    if len(history) == 0:
        print("No transactions yet")

    else:
        for transaction in history:
            print(transaction)

def change_pin(account_number):
    old_pin = input("Enter your current PIN: ")

    if old_pin == accounts[account_number]["pin"]:
        new_pin = input("Enter your 4-digit PIN: ")
        confirm_pin = input("conform your new PIN:")

        if new_pin == confirm_pin:
            if len(new_pin) == 4 and new_pin.isdigit():
                accounts[account_number]["pin"] = new_pin
                print("PIN changed successfully!")
            else:
                print("PIN must contain exactly 4 digits")
        else:
            print("New pins don't match")
    else:
        print("Incorrect current pin")

def main():
    while True:
        print("\n========== BANKING SYSTEM ==========")
        print("1. create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            create_account()

        elif choice == "2":
            account_number = login()

            if account_number is not None:
                account_menu(account_number)

        elif choice == "3":
            print("\nThank you for using our banking system")
            break

        else:
            print("Invalid choice please try again later")

main()

    
