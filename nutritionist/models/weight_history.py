from pydantic import BaseModel
from datetime import datetime, timezone


class WeightHistory(BaseModel):
    user_id: int
    date: datetime = datetime.now(timezone.utc)
    weight_kg: str
