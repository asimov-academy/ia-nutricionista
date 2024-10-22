from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional


class MealEntry(BaseModel):
    user_id: int
    timestamp: datetime = datetime.now(timezone.utc)
    meal_description: str
    image_path: Optional[str] = None
    calories: Optional[str] = None
    carbs: Optional[str] = None
    proteins: Optional[str] = None
    fats: Optional[str] = None
