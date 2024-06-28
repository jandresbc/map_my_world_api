from app.core.jwt import jwt_token
from fastapi import APIRouter
from app.schemas.JsonResponse import JsonDefaultResponse

# Crear una instancia de jwt_token
jwt = jwt_token()

router = APIRouter()

# Definir una ruta protegida que requiera autenticación con token
@router.get("/")
def auth() -> JsonDefaultResponse:
    """This endpoint allows you to get a new authentication token. This token only available for 1 hour

    Returns:
        JsonDefaultResponse: Return the endpoint data in the correct format
    """
    token = jwt.encoder()
    
    if token is not False:
        return {"status":True,"message":"Token generate successfully",'data': {"token":token}}
    else:
        return {"status":False,"message":"Token wasn't generate",'data': {"token":None}}