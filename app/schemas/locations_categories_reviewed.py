from pydantic import BaseModel
from datetime import datetime

class LocationsCategoriesReviewed(BaseModel):
    location_id: int
    category_id: int
    reviewed_at: datetime
