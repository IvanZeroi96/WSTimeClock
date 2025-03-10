from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URI

engine = create_engine(DB_URI, pool_size=10, max_overflow=20, echo=True)
Session = sessionmaker(bind=engine)

def get_db_session():
    return Session()