import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from Database import Database
from datetime import datetime, timezone

load_dotenv()

db = Database(os.getenv('USERDB'), os.getenv('PASSWORD'), os.getenv('DATABASE'))
db.connect()
db.base()

class Users(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    
class Tokens(db.Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    token = Column(String(100), nullable=False)
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
db.Base.metadata.create_all(db.engine)