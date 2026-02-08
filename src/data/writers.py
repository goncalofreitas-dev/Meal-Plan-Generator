import json
from pathlib import Path


def save_output(plan: dict, patient_name: str):
    """
    Saves the final meal plan to outputs/<patient_name>.json
    """
    Path("outputs").mkdir(exist_ok=True)

    safe_name = patient_name.lower().replace(" ", "_")
    path = f"outputs/{safe_name}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)

    return path
