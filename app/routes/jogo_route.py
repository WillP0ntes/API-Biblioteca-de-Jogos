from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.jogos_schema import jogoSchema
from app.services.jogo_service import (
    listar_jogos,
    listar_jogo,
    criar_jogo,
    atualizar_jogo,
    deletar_jogo
)

jogo_router = APIRouter()

# conexão/sessão
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# GET
@jogo_router.get("/jogos")
def get_jogos(
    db: Session = Depends(get_db)
):
    return listar_jogos(db)

# GET by id
@jogo_router.get("/jogos/{id}")
def get_jogos(
    id: int,
    db: Session = Depends(get_db)
):
    return listar_jogo(db, id)

# POST
@jogo_router.post("/jogos")
def post_jogo(
    jogo: jogoSchema,
    db: Session = Depends(get_db)
):
    return criar_jogo(db, jogo)

@jogo_router.delete("/jogos/{id}")
def delet_jogos(
    id: int,
    db: Session = Depends(get_db)
):
    return deletar_jogo(db, id)

@jogo_router.put("/jogos/{id}")
def atualizar_jogos(
    id: int,
    jogo_request: jogoSchema,
    db: Session = Depends(get_db)
):
    return atualizar_jogo(db, id, jogo_request)