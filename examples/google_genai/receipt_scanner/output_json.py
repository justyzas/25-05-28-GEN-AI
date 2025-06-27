import json
from typing import Any

def output_result_json(result: Any):
    def convert(item):
        if hasattr(item, "model_dump"):  # Pydantic v2
            return item.model_dump()
        elif hasattr(item, "dict"):  # Pydantic v1
            return item.dict()
        return item

    if isinstance(result, list):
        serializable = [convert(item) for item in result]
    else:
        serializable = convert(result)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=4)
