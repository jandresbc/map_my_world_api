from sqlalchemy import Column, Integer, Float, DateTime
from app.databases import Base
import datetime

class Locations(Base):
    __tablename__ = 'locations'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float, index=True)
    lng = Column(Float, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
