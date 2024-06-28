from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.categories import CategoryCreate
from app.schemas.JsonResponse import JsonDefaultResponse
from app.cruds.categories import get_category, create_category
from app.databases import db
from app.core import jwt

router = APIRouter()

@router.post("/create")
@jwt.token_required
def create_new_category(request: Request, category: CategoryCreate) -> JsonDefaultResponse:
    """In this endpoint you can create a new category

    Args:
        request (Request): This is all request parameters
        category (CategoryCreate): This is all category parameters, in the correct format, available in the your schemas

    Returns:
        JsonDefaultResponse: Return the endpoint data in the correct format
    """
    db_category = get_category(db, category.name)
    if db_category:
        return {"status":True,"message":"Category already registered","data":{}}
    
    create_cat = create_category(db, category)
    
    if create_cat:
        return {"status":True,"message":"Category was created","data":{}}
    else:
        return {"status":True,"message":"Category wasn't created due to error","data":{}}
