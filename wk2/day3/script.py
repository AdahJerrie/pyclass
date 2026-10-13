import csv


# What is CSV?

# CSV means Comma-Separated Values.

# CSV, which is commonly used for tables and spreadsheets.

# reading a csv

with open("developers.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# csv.dictreader turns each row into a dictionary
with open("developers.csv", "r") as file:
    reader = csv.DictReader(file)

    for developer in reader:
        dev_name = developer["name"]
        dev_language = developer["language"]

        print(f"{dev_name} knows {dev_language}")

# Mental model

# You can think of:

# csv.reader()

# as:

# CSV → lists

# while:

# csv.DictReader()

# is:

# CSV → dictionaries

# Writing a csv. Creating a csv file from python.

with open("skills.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "skill", "level"])
    writer.writerow(["Jerrie","Python","Beginner"])
    writer.writerow(["Alice", "Go", "Intermediate"])
    writer.writerow(["Bob", "Javascript", "Advanced"])

with open("skills.csv", "r") as file:
    reader = csv.DictReader(file)

    for developer in reader:
        name = developer["name"]
        skill = developer["skill"]
        level = developer["level"]

        print(f"{name} is a {level} in {skill}")

# Exercise 4: Appending CSV Records

        
