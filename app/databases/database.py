from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import USER, PASS, HOST, PASS, DATABASE, PORT
import os

class Database:
    session = None
    base = None
    engine = None
    base_url = f"mysql+pymysql://{USER}:{PASS}@{HOST}/{DATABASE}"

    def __init__(self):
        self.base = declarative_base()
        self.engine = create_engine(self.base_url, pool_recycle = PORT)
        self.session = sessionmaker(bind=self.engine)
        self.session = self.session()
    
    def create_tables(self):
        self.base.metadata.create_all(self.engine)

    def drop_tables(self):
        self.base.metadata.drop_all(self.engine)
    
    def get_base(self):
        return self.base
    
if __name__ == "__main__":
    database = Database()
    
    database.create_tables()
