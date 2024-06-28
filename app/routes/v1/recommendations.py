from fastapi import APIRouter, Request
from app.schemas.JsonResponse import JsonDefaultResponse
from app.cruds.recommendations import get_unreviewed_location_category_pairs
from app.databases import db
from app.core import jwt

router = APIRouter()

@router.get("/get_recommendations")
@jwt.token_required
def get_recommendations(request: Request) -> JsonDefaultResponse:
    """In this endpoint you can get recommendations for new revisions

    Args:
        request (Request): This is all request parameters

    Returns:
        JsonDefaultResponse: Return the endpoint data in the correct format
    """
    recommendations = get_unreviewed_location_category_pairs()
    
    return {
        "status": True,
        "message": "This a recommendations",
        "data": recommendations
    }
