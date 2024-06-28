from pydantic import BaseModel

class JsonDefaultResponse(BaseModel):
    status: bool
    message: str
    data: dict