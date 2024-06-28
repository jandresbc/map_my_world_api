import jwt, datetime
from functools import wraps
from fastapi import Request
from fastapi.responses import JSONResponse
from .config import SECRET, KEY
import time

class jwt_token:
    payload = None
    expires = 1

    def __init__(self, expires=None):    
        expires = expires if expires is not None else self.expires

        delta = datetime.timedelta(hours=expires)
        
        date_exp = datetime.datetime.now() + delta
        exp = time.mktime(date_exp.timetuple())

        self.payload = {
            "datetime" : datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S'),
            "exp" : exp,
            "key" : KEY
        }

    def encoder(self, payload: dict = None) -> str | bool:
        self.payload["data"] = payload if payload is not None else None
        
        encoded_jwt = jwt.encode(self.payload, SECRET, algorithm="HS256")

        return encoded_jwt
    
    def decoder(self, encoded_jwt) -> dict:
        decode_jwt = dict(jwt.decode(encoded_jwt, SECRET, algorithms=["HS256"]))

        return decode_jwt
    
    def validate_token(self,token: str) -> bool:
        _token = dict(self.decoder(token))
        
        now = datetime.datetime.now()
        expiration_date = datetime.datetime.fromtimestamp(_token["exp"])

        if now <= expiration_date:
            return True
        
        return False
    
    def token_required(self, f):
        @wraps(f)
        async def decorated_function(*args, **kwargs) -> JSONResponse | bool:
            request: Request = kwargs.get("request")

            if request is None:
                return JSONResponse(
                    {"message": "The request does not respond to the 'Class Request' or does not send the variable 'request'"},
                    status_code=401
                )

            auth = request.headers.get("Authorization")
            
            if auth is None:
                return JSONResponse({"status":False,'message': 'Token is missing'}, status_code=401)
            
            try:
                token = auth.split('Bearer ')[1]
                
                if not self.validate_token(token):
                    return JSONResponse({"status":False,'message': 'Token is invalid or expired'}, status_code=401)
            except IndexError:
                return JSONResponse({"status":False,'message': 'Token format is invalid'}, status_code=401)
            except jwt.ExpiredSignatureError:
                return JSONResponse({"status":False,"message": "Token expired"}, status_code=401)
            except jwt.InvalidTokenError:
                return JSONResponse({"status":False,"message": "Token invalid"}, status_code=401)
                
            return f(*args, **kwargs)
        return decorated_function