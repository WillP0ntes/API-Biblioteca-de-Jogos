from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.estoques_schema import estoqueSchema
from app.services.estoque_service import (
    listar_estoques,
    listar_estoque,
    criar_estoque,
    deletar_estoque,
    atualizar_estoque
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

# GET by id
@estoque_router.get("/estoques/{id}")
def get_estoques(
    id: int,
    db: Session = Depends(get_db)
):
    return listar_estoque(db, id)

# POST
@estoque_router.post("/estoques")
def post_estoque(
    estoque: estoqueSchema,
    db: Session = Depends(get_db)
):
    return criar_estoque(db, estoque)

# DELETE
@estoque_router.delete("/estoques/{id}")
def delet_estoques(
    id: int,
    db: Session = Depends(get_db)
):
    return deletar_estoque(db, id)

# UPDATE
@estoque_router.put("/estoques/{id}")
def atualizar_estoques(
    id: int,
    estoque_request: estoqueSchema,
    db: Session = Depends(get_db)
):
    return atualizar_estoque(db, id, estoque_request)