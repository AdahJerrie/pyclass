import utilities
import datetime

your_name = input("Enter your name: ")
name = utilities.greet_dev(your_name)
while True:
    try:
        begin_yr = int(input("Enter start year: "))
        break
    except ValueError:
        print("input must be a number")

current_yr = datetime.date.today().year
experience = utilities.calculate_experience(begin_yr, current_yr)

skill_set = input("Enter skills (separated by commas): ")
skills_list = skill_set.split(",")
skills = utilities.format_skills(skills_list)


print(name)
print(experience)
print(skills)