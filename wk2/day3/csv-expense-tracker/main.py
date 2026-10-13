import csv
from pathlib import Path

def expense_tracker():
    while True:
        print("=== Expense Tracker ===")
        print("Add expense")
        print("View expenses")
        print("Calculate total expenses")
        print("Exit")
        options = input("select an option 1- 4: \t\n")
        try:
            selected_option = int(options)
        except ValueError:
            print(f"{options} is not a valid option")
            continue
        
        if selected_option == 1:
            date = input("Enter date (yy - mm - dd): ")
            category = input("Enter category (food, transport, internet): ")
            amount = input("Enter amount: ")

            with open("expenses.csv", "a", newline="") as file:
                fieldnames = ["date", "category", "amount"]

                writer = csv.DictWriter(file, fieldnames=fieldnames)

                file_exist = Path("expenses.csv").exists()
                if not file_exist:
                    writer.writeheader()  

            with open("expenses.csv", "a", newline="") as file:
                    writer.writerow({
                        "date": date,
                        "category": category,
                        "amount": amount
                    })

        if selected_option == 2:
            with open("expenses.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                for expenses in reader:
                    date = expenses["date"]
                    category = expenses["category"]
                    amount = expenses["amount"]

                    print(f"{date} - {category} - {amount}")

        if selected_option == 3:
            with open("expenses.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                total = 0
                for expenses in reader:
                    total += float(expenses["amount"])
                    print(total)

        elif selected_option == 4:
            print("Goodbye")
            break
        else:
            if selected_option > 4:
                print(f"{selected_option} is not a valid option")


expense_tracker()