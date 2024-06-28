from pydantic import BaseModel

class LocationCreate(BaseModel):
    lat: float
    lng: float