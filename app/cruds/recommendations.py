from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.engine.row import Row
from sqlalchemy import and_, or_, outerjoin
from app.models.locations_categories_reviewed import LocationsCategoriesReviewed
from app.models.locations import Locations
from app.models.categories import Categories
from datetime import datetime, timedelta
from app.databases import Database

def get_data(rows: Row ) -> list:
    """This function allows you to consult the data of a certain query made with SQLchemy

    Args:
        rows (Row): Sqlalchemy rows

    Returns:
        list: List of dictionary with the query data
    """
    db = Database()
    data_result = []
    
    for x in rows:
        location_data = db.session.query(
            Locations.id,
            Locations.lat, 
            Locations.lng
            ).filter(
                Locations.id == x[0]
            ).first()
        
        category_data = db.session.query(
            Categories.id,
            Categories.name
            ).filter(
                Categories.id == x[1]
            ).first()
        
        data_result.append({"Locations":{
            "id":location_data.id,
            "lat":location_data.lat,
            "lng":location_data.lng
        },"Category":{
            "id":category_data.id,
            "name":category_data.name
        }})
        
    return data_result

def get_unreviewed_location_category_pairs() -> dict:
    """_summary_

    Returns:
        dict: dictionary with the recommendations(Never reviewed and not reviewed recently - < 30 days)
    """
    db = Database()
    # Fecha límite de 30 días atrás
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    
    # Subconsulta para obtener las combinaciones de ubicación y categoría junto con la última fecha de revisión
    subquery = db.session.query(
        LocationsCategoriesReviewed.location_id,
        LocationsCategoriesReviewed.category_id,
        func.max(LocationsCategoriesReviewed.reviewed_at).label("last_reviewed")
    ).group_by(
        LocationsCategoriesReviewed.location_id,
        LocationsCategoriesReviewed.category_id
    ).subquery()

    # Combinaciones nunca revisadas (ausentes en la tabla de revisiones)
    never_reviewed = db.session.query(
        Locations.id.label("location_id"),
        Categories.id.label("category_id")
    ).select_from(Locations).join(
        Categories,
        # Especifica cómo se realiza el join
        and_(Locations.id == Categories.id)
    ).outerjoin(
        subquery,
        and_(Locations.id == subquery.c.location_id, Categories.id == subquery.c.category_id)
    ).filter(
        subquery.c.location_id.is_(None)
    ).limit(10).all()

    # Combinaciones revisadas hace más de 30 días y aquellas que nunca han sido revisadas
    not_reviewed_recently = db.session.query(
        subquery.c.location_id,
        subquery.c.category_id
    ).filter(
        or_(
            subquery.c.last_reviewed.is_(None),
            subquery.c.last_reviewed < thirty_days_ago
        )
    ).limit(10).all()
    
    never = get_data(never_reviewed)
    reviewed_recently = get_data(not_reviewed_recently)
    
    response = {
        "never_reviewed": never,
        "not_reviewed_recently": reviewed_recently
    }
    
    return response