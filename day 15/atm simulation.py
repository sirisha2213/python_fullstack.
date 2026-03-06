# atm simulation menu
def check_average_transaction():
    try:
        total = 1000
        transactions = 0  # causes ZeroDivisionError
        avg = total / transactions
        print("Average Transaction:", avg)
    except ZeroDivisionError:
        print("Error Occurred: Division by zero (ZeroDivisionError)")


def withdraw_invalid_input():
    try:
        amount = int(input("Enter amount to withdraw: "))
        print("Withdrawing:", amount)
    except ValueError:
        print("Error Occurred: Invalid input (ValueError)")


def deposit_invalid_type():
    try:
        balance = 5000
        deposit = "1000"  # string
        balance += deposit  # TypeError
    except TypeError:
        print("Error Occurred: Invalid data type (TypeError)")


def access_invalid_transaction_history():
    try:
        transactions = [100, 200, 300]
        print(transactions[5])  # IndexError
    except IndexError:
        print("Error Occurred: Transaction index out of range (IndexError)")


def access_nonexistent_account():
    try:
        accounts = {"101": "Ravi", "102": "Sita"}
        print(accounts["105"])  # KeyError
    except KeyError:
        print("Error Occurred: Account does not exist (KeyError)")


def read_missing_log_file():
    try:
        file = open("transaction_log.txt", "r")  # FileNotFoundError
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("Error Occurred: File not found (FileNotFoundError)")


# ---------------- MAIN MENU ----------------
while True:
    print("\n--- ATM Simulation Menu ---")
    print("1. Check Average Transaction (ZeroDivisionError)")
    print("2. Withdraw with Invalid Input (ValueError)")
    print("3. Deposit with Invalid Data Type (TypeError)")
    print("4. Access Invalid Transaction History (IndexError)")
    print("5. Access Non-Existent Account (KeyError)")
    print("6. Read Missing Transaction Log File (FileNotFoundError)")
    print("7. Exit")

    try:
        choice = int(input("Select an option (1-7): "))

        if choice == 1:
            check_average_transaction()
        elif choice == 2:
            withdraw_invalid_input()
        elif choice == 3:
            deposit_invalid_type()
        elif choice == 4:
            access_invalid_transaction_history()
        elif choice == 5:
            access_nonexistent_account()
        elif choice == 6:
            read_missing_log_file()
        elif choice == 7:
            print("Thank you for using ATM Simulation.")
            break
        else:
            print("Invalid option. Please choose between 1 and 7.")

    except ValueError:
        print("Error Occurred: Please enter a number only")
