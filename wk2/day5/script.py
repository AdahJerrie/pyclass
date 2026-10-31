from datetime import datetime, timedelta

def get_today():
    return datetime.now().date()

def show_today():
    today = get_today()
    print(f"Today is {today.strftime('%A, %d %B %Y')}")

def calculate_deadline():
    deadline_str = input("Enter deadline (YYYY-MM-DD): ")
    try:
        deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    today = get_today()
    delta = deadline_date - today
    days_remaining = delta.days

    if days_remaining == 0:
        print("Your deadline is today!")
    elif days_remaining < 0:
        print(f"Deadline passed {abs(days_remaining)} days ago.")
    else:
        print(f"Days remaining: {days_remaining}")

def calculate_future_date():
    days_str = input("Enter number of days: ")
    try:
        days = int(days_str)
        if days < 0:
            print("Please enter a positive number of days.")
            return
    except ValueError:
        print("Invalid number. Please enter a whole integer.")
        return

    today = get_today()
    future_date = today + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def run_date_calculator():
    while True:
        print("\n=== Date Calculator ===")
        print("1. Show today's date")
        print("2. Calculate days until a deadline")
        print("3. Calculate a future date")
        print("4. Exit")
        
        choice = input("\nSelect an option 1 - 4: ")
        
        if choice == "1":
            show_today()
        elif choice == "2":
            calculate_deadline()
        elif choice == "3":
            calculate_future_date()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")

run_date_calculator()
