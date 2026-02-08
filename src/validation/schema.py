from pydantic import ValidationError
from src.schemas.meal_plan import DailyMealPlan


def validate_schema(plan: dict) -> list[str]:
    """
    Validates the generated plan against the Pydantic schema.
    Returns a list of validation error messages.
    """
    try:
        DailyMealPlan.model_validate(plan)
        return []
    except ValidationError as e:
        return [str(err["msg"]) for err in e.errors()]
