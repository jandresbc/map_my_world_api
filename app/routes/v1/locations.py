from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.locations import LocationCreate
from app.schemas.JsonResponse import JsonDefaultResponse
from app.cruds.locations import get_location, create_location
from app.databases import db
from app.core import jwt

router = APIRouter()

@router.post("/create")
@jwt.token_required
def create_new_location(request: Request, location: LocationCreate) -> JsonDefaultResponse:
    """In this endpoint you can create a new location

    Args:
        request (Request): This is all request parameters
        location (LocationCreate): This is all locations parameters, in the correct format, available in the your schemas

    Returns:
        JsonDefaultResponse: Return the endpoint data in the correct format
    """
    db_location = get_location(db, location.lat, location.lng)
    
    if db_location:
        return {"status":True,"message":"Location already registered","data":{}}
    
    create = create_location(db, location)
    
    if create:
        return {"status":True,"message":"Location was created","data":{}}
    else:
        return {"status":True,"message":"Location wasn't created due to error","data":{}}
