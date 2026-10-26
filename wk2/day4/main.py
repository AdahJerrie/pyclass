import datetime

from tools.greetings import greet_dev
from tools.experience import calculate_experience
from tools.skills import format_skills

your_name = input("Enter your name: ")
name = greet_dev(your_name)
while True:
    try:
        begin_yr = int(input("Enter start year: "))
        break
    except ValueError:
        print("input must be a number")

current_yr = datetime.date.today().year
experience = calculate_experience(begin_yr, current_yr)

skill_set = input("Enter skills (separated by commas): ")
skill = [skill.strip() for skill in skill_set.split(",") if skill.strip()]
skills = format_skills(skill)

print(name)
print(f"Years of experience: {experience}")
print(f"Skills: {skills}")