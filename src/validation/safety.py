def validate_safety(plan: dict, patient_profile: dict) -> list[str]:
    """
    Validates that no unsafe food appears in the plan.
    This is a keyword-based safety check.
    """
    errors = []

    allergies = patient_profile.get("food_allergies", [])
    intolerances = patient_profile.get("food_intolerances", [])
    exclusions = (
        patient_profile.get("patient_infos", {})
        .get("dietary_history", {})
        .get("exclusions", [])
    )

    restricted = set(allergies + intolerances + exclusions)

    if not restricted:
        return []

    for meal in plan.get("meals", []):
        for item in meal.get("items", []):
            for r in restricted:
                if r.lower() in item.lower():
                    errors.append(
                        f"Unsafe food detected: '{r}' in item '{item}'"
                    )

    return errors
