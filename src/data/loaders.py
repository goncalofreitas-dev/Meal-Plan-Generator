import json
from typing import List, Dict


def load_jsonl(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # JSON array
    if content.startswith("["):
        data = json.loads(content)
        if not isinstance(data, list):
            raise ValueError(f"{path} does not contain a JSON list")
        return data

    # JSONL
    data = []
    for idx, line in enumerate(content.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            data.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(
                f"[WARN] Skipping invalid JSON on line {idx} of {path}: {e}"
            )

    return data
