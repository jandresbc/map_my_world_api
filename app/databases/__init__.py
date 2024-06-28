from .database import Database

db = Database()
Base = db.get_base()