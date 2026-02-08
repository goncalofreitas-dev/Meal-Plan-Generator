def validate_targets(plan: dict, patient_profile: dict) -> list[str]:
    """
    Validates daily totals against patient targets using tolerances.
    """
    errors = []

    daily = plan.get("daily_totals", {})

    target_kcal = patient_profile.get("dee_goal")
    target_macros = patient_profile.get("macronutrient_distribution_in_grams", {})
    target_fiber = patient_profile.get("fiber_quantity_in_grams")

    # --- Tolerances ---
    KCAL_TOLERANCE = 0.05      # ±5%
    MACRO_TOLERANCE = 0.10     # ±10%
    FIBER_MIN_RATIO = 0.90    # at least 90%

    # Calories
    if target_kcal:
        kcal = daily.get("kcal", 0)
        if not (target_kcal * (1 - KCAL_TOLERANCE) <= kcal <= target_kcal * (1 + KCAL_TOLERANCE)):
            errors.append(
                f"Calories out of range: {kcal} kcal (target {target_kcal})"
            )

    # Macronutrients
    macro_map = {
        "protein_g": "protein",
        "carbs_g": "carbohydrate",
        "fat_g": "fat",
    }

    for plan_key, target_key in macro_map.items():
        target_value = target_macros.get(target_key)
        if target_value:
            value = daily.get(plan_key, 0)
            if not (target_value * (1 - MACRO_TOLERANCE) <= value <= target_value * (1 + MACRO_TOLERANCE)):
                errors.append(
                    f"{plan_key} out of range: {value} g (target {target_value})"
                )

    # Fiber
    if target_fiber:
        fiber = daily.get("fiber_g", 0)
        if fiber < target_fiber * FIBER_MIN_RATIO:
            errors.append(
                f"Fiber too low: {fiber} g (target {target_fiber})"
            )

    return errors
