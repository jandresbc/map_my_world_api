import azure.functions as func
from fastapi import FastAPI
from app.main import app as fastapi_app
import uvicorn

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True, access_log=False)