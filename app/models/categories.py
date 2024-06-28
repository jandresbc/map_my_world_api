from sqlalchemy import Column, Integer, String, DateTime
from app.databases import Base
import datetime

class Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
