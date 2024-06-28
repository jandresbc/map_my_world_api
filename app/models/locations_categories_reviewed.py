from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.databases import Base
from datetime import datetime

class LocationsCategoriesReviewed(Base):
    __tablename__ = 'locations_categories_reviewed'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    reviewed_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    location = relationship("Locations")
    category = relationship("Categories")
