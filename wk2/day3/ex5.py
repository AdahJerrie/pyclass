import csv 


with open("employees.csv", "w", newline="") as file:
    fieldnames = ["name", "role", "salary"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "name": "Jerrie",
        "role": "python developer",
        "salary": "750000000"
    })

    writer.writerow({
        "name": "Alice",
        "role": "Backend developer",
        "salary": "85000000"
    })

    writer.writerow({
        "name": "Bob",
        "role": "Data analyst",
        "salary": "545400"
    })

print("=== Employees ===")

with open("employees.csv", "r", newline="") as file:
    employees = csv.DictReader(file)

    for employee in employees:
        name = employee["name"]
        role = employee["role"]
        salary = employee["salary"]

        print(f"{name} - {role} - {salary}")