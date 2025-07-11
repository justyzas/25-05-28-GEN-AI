from pydantic import BaseModel
from typing import Dict, Any


class IngestionBodyModel(BaseModel):
    text: str
    metadata: Dict[str, Any]
