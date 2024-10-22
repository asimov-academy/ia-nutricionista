from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional


class Report(BaseModel):
    user_id: int
    date: datetime = datetime.now(timezone.utc)
    content: str
