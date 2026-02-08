def validate_daily_totals(plan: dict) -> list[str]:
    """
    Checks if daily_totals equal the sum of all meal_totals.
    """
    errors = []

    meals = plan.get("meals", [])
    daily = plan.get("daily_totals", {})

    summed = {
        "kcal": 0,
        "protein_g": 0,
        "carbs_g": 0,
        "fat_g": 0,
        "fiber_g": 0,
    }

    for meal in meals:
        totals = meal.get("meal_totals", {})
        for key in summed:
            summed[key] += totals.get(key, 0)

    for key, value in summed.items():
        if round(value, 2) != round(daily.get(key, 0), 2):
            errors.append(
                f"Daily total mismatch for {key}: expected {value}, got {daily.get(key)}"
            )

    return errors
