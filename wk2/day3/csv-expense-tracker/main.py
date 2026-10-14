import csv
from pathlib import Path

def expense_tracker():
    # define file path once at the top
    file_path = Path("expenses.csv")

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Calculate total expenses")
        print("4. Exit")

        options = input("select an option 1- 4: \t\n")
        try:
            selected_option = int(options)
        except ValueError:
            print(f"{options} is not a valid option")
            continue
    
        if selected_option == 1:
            date = input("Enter date (yy - mm - dd): ")
            category = input("Enter category (food, transport, internet): ")
            try:
                amount = float(input("Enter amount: "))
                if amount <= 0:
                    print(f"amount must be greater than zero")
                    continue
            except ValueError:
                print("Invalid amount")
                continue

            # check file existence before opening
            file_exist = file_path.exists()

            with open("expenses.csv", "a", newline="") as file:
                fieldnames = ["date", "category", "amount"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # this writes header only if it's a new file
                if not file_exist:
                    writer.writeheader()  

                writer.writerow({
                    "date": date,
                    "category": category,
                    "amount": amount
                })
                print("Expense added successfully")

        elif selected_option == 2:
            if not file_path.exists():
                print("No expenses added")
                continue

            with open("expenses.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                for expenses in reader:
                    date = expenses["date"]
                    category = expenses["category"]
                    amount = expenses["amount"]

                    print(f"{date} - {category} - {amount}")

        elif selected_option == 3:
            if not file_path.exists():
                print("No expenses recoded yet")
                continue

            with open("expenses.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                total = 0.0
                for expenses in reader:
                    try:
                        total += float(expenses["amount"])
                    except ValueError:
                        continue
                print(f"Total expenses: {total:.2f}")

        elif selected_option == 4:
            print("Goodbye")
            break
        else:
            print(f"{selected_option} is not a valid option")

expense_tracker()