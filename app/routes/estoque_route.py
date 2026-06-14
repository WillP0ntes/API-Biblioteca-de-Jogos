from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.estoques_schema import estoqueSchema
from app.services.estoque_service import (
    listar_estoques
)

estoque_router = APIRouter()

# conexão/sessão
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# GET
@estoque_router.get("/estoques")
def get_estoque(
    db: Session = Depends(get_db)
):
    return listar_estoques(db)
