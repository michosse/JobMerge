from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import models
from typing import Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from scraper.run_spider import run_spider
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

models.Base.metadata.create_all(bind=engine)

class Offer(BaseModel):
    title: str
    company: str
    image: str
    tags: list[str]
    link: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/api/offers")
def get_offers(db: db_dependency)->list[Offer]:
    result = db.query(models.Offer).all()
    if not result:
        raise HTTPException(status_code=404, detail="Brak ofert")
    return result

@app.put("/api/reload")
def reaload_db():
    response = run_spider()
    return response