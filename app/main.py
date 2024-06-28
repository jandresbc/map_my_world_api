from fastapi import FastAPI
# Routes
from app.routes.v1 import auth, locations, categories, recommendations

app = FastAPI(title="Map My World API", description="This API handles the all endpoints to manage the API map my world.", version="1.0")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(locations.router, prefix="/api/v1/locations", tags=["locations"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(recommendations.router, prefix="/api/v1/recommendations", tags=["recommendations"])

if __name__ == "__main__":
    import argparse
 
    parser = argparse.ArgumentParser()
    parser.add_argument("-md", "--mode", help="Modo de ejecución en la base de datos")
    args = parser.parse_args()
    
    from app.databases import db
    
    if args.mode == "drop_tables":
        db.drop_tables()
        exit()
    db.create_tables()