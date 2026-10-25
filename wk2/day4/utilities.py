def greet_dev(name="Jerrie") -> str :
    # name = input("Enter name: ")
    return f"welcome, {name}!"

def calculate_experience(start_yr, current_yr):
    start_yr = int(input("Enter start year: "))
    current_yr = int(input("Enter current year: "))

    experience = current_yr - start_yr

    return experience