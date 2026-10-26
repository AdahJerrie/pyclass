
def greet_dev(name: str) -> str :

    return f"Welcome, {name}!"

def calculate_experience(start_yr: int, current_yr: int) -> int:

    return current_yr - start_yr

    

def format_skills(skill_set: list[str]) -> str:

    skill = [skill.strip() for skill in skill_set.split(",") if skill.strip()]

    cleaned_skills = ", ".join(skill)
    
    return cleaned_skills