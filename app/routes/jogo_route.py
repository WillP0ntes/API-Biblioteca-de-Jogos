from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.jogos_schema import jogoSchema
from app.services.jogo_service import (
    listar_jogos,
    criar_jogo
)

router = APIRouter()

# conexão/sessão
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# GET
@router.get("/jogos")
def get_jogos(
    db: Session = Depends(get_db)
):
    return listar_jogos(db)

# POST
@router.post("/jogos")
def post_jogo(
    jogo: jogoSchema,
    db: Session = Depends(get_db)
):
    return criar_jogo(db, jogo)
