from sqlalchemy.orm import Session
from app.models.jogo import Jogo
from app.models.jogos_schema import jogoSchema
from fastapi import FastAPI, HTTPException

def listar_jogos(db: Session):
    return db.query(Jogo).all()

def listar_jogo(db: Session, id: int):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return db.query(Jogo).get({"id": id})

def criar_jogo(db: Session, jogo: Jogo):
    novo_jogo = Jogo(
        nome = jogo.nome,
        descricao = jogo.descricao,
        desenvolvedor = jogo.desenvolvedor,
        lancamento = jogo.lancamento
    )

    db.add(novo_jogo)
    db.commit()
    db.refresh(novo_jogo)

    return novo_jogo

def deletar_jogo(db, id):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    db.delete(jogo)
    db.commit()

    return {"mensagem": "Jogo removido com sucesso"}

def atualizar_jogo(db, id, jogo_request):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    jogo.nome = jogo_request.nome
    jogo.descricao = jogo_request.descricao
    jogo.desenvolvedor = jogo_request.desenvolvedor
    jogo.lancamento = jogo_request.lancamento

    db.commit()

    return jogo