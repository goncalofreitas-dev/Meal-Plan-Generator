from pydantic import BaseModel, Field
from typing import List


class MealTotals(BaseModel):
    kcal: float = Field(..., ge=0)
    protein_g: float = Field(..., ge=0)
    carbs_g: float = Field(..., ge=0)
    fat_g: float = Field(..., ge=0)
    fiber_g: float = Field(..., ge=0)


class Meal(BaseModel):
    meal_type: str
    time: str  # HH:MM
    items: List[str]
    meal_totals: MealTotals


class DailyTotals(MealTotals):
    pass


class DailyMealPlan(BaseModel):
    daily_totals: DailyTotals
    meals: List[Meal]
