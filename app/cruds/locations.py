from sqlalchemy.orm import Session
from app.models.locations import Locations
from app.schemas.locations import LocationCreate

def get_location(db: Session, lat: float, lng: float):
    location = db.session.query(Locations).filter(Locations.lat == lat, Locations.lng == lng).first()
    
    return location

def create_location(db: Session, location: LocationCreate) -> bool:
    try:        
        db_location = Locations()
        db_location.lat = location.lat
        db_location.lng = location.lng
        
        db.session.add(db_location)
        db.session.commit()
        db.session.flush()
        
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False
    finally:
        db.session.close()
