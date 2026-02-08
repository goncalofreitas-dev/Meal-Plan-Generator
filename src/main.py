from dotenv import load_dotenv
from src.graph.graph import build_graph
from src.data.loaders import load_jsonl
from src.data.writers import save_output

import os

load_dotenv()

os.environ["LANGSMITH_TRACING"] = "true"

PATIENTS_PATH = "input_nutri_approval.jsonl"
FOOD_LISTS_PATH = "input_lists.jsonl"


def main():
    # Load input data
    patients = load_jsonl(PATIENTS_PATH)
    food_lists = load_jsonl(FOOD_LISTS_PATH)

    graph = build_graph()
    
    for idx, patient in enumerate(patients, start=1):
        print("\n" + "=" * 60)
        print(f"Processing patient {idx}/{len(patients)}: {patient.get('patient_name', 'unknown')}")
        print("=" * 60)

        initial_state = {
            "patient_profile": patient,
            "available_food_lists": food_lists,
            "current_plan": None,
            "validation_errors": [],
            "retry_count": 0,
        }

        result = graph.invoke(initial_state)
        
        output_path = save_output(
            result["current_plan"],
            patient.get("patient_name", f"patient_{idx}")
        )

        print(f"Output saved to: {output_path}")

        print("Execution finished.")
        print("Patient ID:", patient.get("patient_id", "unknown"))
        print("Retry count:", result["retry_count"])
        print("Final plan:")
        print(result["current_plan"])


if __name__ == "__main__":
    main()
