expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully")


def view_expenses():
    if not expenses:
        print("No expenses found")
        return

    total = 0

    print("\n--- Expenses ---")

    for expense in expenses:
        print(f"{expense['name']} : ₹{expense['amount']}")
        total += expense["amount"]

    print(f"\nTotal Expense: ₹{total}")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Program closed")
        break

    else:
        print("Invalid choice")
