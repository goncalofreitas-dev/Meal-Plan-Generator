from typing import TypedDict, List, Optional, Dict, Any


class MealPlanState(TypedDict):
    # Input
    patient_profile: Dict[str, Any]
    available_food_lists: List[Dict[str, Any]]

    # Generation
    current_plan: Optional[Dict[str, Any]]

    # Validation & control
    validation_errors: List[str]
    retry_count: int
