import csv

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
            date = input("Enter date (dd - mm - yy): ")
            category = input("Enter category (food, transport, internet): ")
            amount = int(input("Enter amount: "))

            with open("expenses.csv", "w", newline="") as file:
                fieldnames = ["date", "category", "amount"]

                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()

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
        break


expense_tracker()