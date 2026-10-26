
def greet_dev(name: str) -> str :

    return f"Welcome, {name}!"

def calculate_experience(start_yr: int, current_yr: int) -> int:

    return current_yr - start_yr

    

def format_skills(skill_set: list[str]) -> str:

    cleaned_skills = ", ".join(skill_set)
    
    return cleaned_skills