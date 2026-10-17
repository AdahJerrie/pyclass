ALLOWED_CATEGORIES = {"Network", "Hardware", "Software", "Other"}
ALLOWED_URGENCIES = {"low", "medium", "high"}

def calculate_priority(urgency, affected_users):


    normalized_urgency = str(urgency).strip().lower()

    if normalized_urgency == "high" and affected_users >= 10:
        return "critical"

    elif normalized_urgency == "high" or affected_users >= 10:
        return "high"

    elif normalized_urgency == "medium" or affected_users >= 3:
        return "medium"

    else:
        return "low"


def validate_ticket_inputs(title, category, urgency, affected_users):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title must not be blank")
    cleaned_title = title.strip()

    if not isinstance(category, str) or not category.strip():
        raise ValueError(f"category must be one of: {', '.join(ALLOWED_CATEGORIES)}")
    cleaned_category = category.strip().capitalize()
    if cleaned_category not in ALLOWED_CATEGORIES:
        raise ValueError(
            f"Invalid category '{category}'. Allowed categories: {', '.join(ALLOWED_CATEGORIES)}."
        )
    
    if not isinstance(urgency, str) or not urgency.strip():
        raise ValueError(f"urgency must be one of: {', '.join(ALLOWED_URGENCIES)}")
    cleaned_urgency = urgency.strip().lower()
    if cleaned_urgency not in ALLOWED_URGENCIES:
        raise ValueError(
            f"Invalid urgency '{urgency}'. Allowed urgency levels : {', '.join(ALLOWED_URGENCIES)}."
        )

    if isinstance(affected_users, bool):
        raise ValueError("affected_users must be a positive integer (not boolean).")
    if isinstance(affected_users, int):
        parsed_users = affected_users
    elif isinstance(affected_users, str):
        stripped_users = affected_users.strip()
        if not stripped_users:
            raise ValueError("affected_users must be a positive integer.")
        try:
            parsed_users = int(stripped_users)
        except ValueError:
            raise ValueError("affected_users must be a positive integer (not decimal or text).")
    else:
        raise ValueError("affected_users must be a positive integer (not decimal or text).")
    if parsed_users <= 0:
        raise ValueError("affected_users must be a positive integer greater than 0.")