from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.estoque_schema import estoqueSchema

router = APIRouter()

# conexão/sessão
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()