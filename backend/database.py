import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DB_ADDRESS = os.getenv('DATABASE_HOST','localhost')
URL_DATABASE = f'postgresql://postgres:admin@{DB_ADDRESS}:5432/jobs'
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()