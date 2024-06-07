from sqlalchemy import Column, String, ARRAY
from database import Base

class Offer(Base):
    __tablename__ = 'offer'

    link = Column(String)
    title = Column(String, primary_key=True)
    company = Column(String, primary_key=True)
    image = Column(String)
    tags = Column(ARRAY(String))
