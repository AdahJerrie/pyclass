
def calculate_priority(urgency, affected_users):
    ALLOWED_CATEGORIES = ("Network", "Hardware", "Software", "Other")
    ALLOWED_URGENCIES = ("low", "medium", "high")

    normalized_urgency = str(urgency).strip().lower()

    if normalized_urgency == "high" and affected_users >= 10:
        return "critical"

    elif normalized_urgency == "high" or affected_users >= 10:
        return "high"

    elif normalized_urgency == "medium" or affected_users >= 3:
        return "medium"

    else:
        return "low"