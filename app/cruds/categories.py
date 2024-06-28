from sqlalchemy.orm import Session
from app.models.categories import Categories
from app.schemas.categories import CategoryCreate

def get_category(db: Session, name: str):
    categories = db.session.query(Categories).filter(Categories.name == name).first()

    return categories

def create_category(db: Session, category: CategoryCreate) -> bool:
    try:
        db_category = Categories(name=category.name)
        db.session.add(db_category)
        db.session.commit()
        db.session.flush()
        
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False
    finally:
        db.session.close()
