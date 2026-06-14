from sqlalchemy.orm import Session
from app.models.estoque import Estoque
from app.models.estoques_schema import estoqueSchema

def listar_estoques(db: Session):
    return db.query(Estoque).all()

def listar_estoque(db: Session, id: int):
    return db.query(Estoque).get({"id": id})

def criar_estoque(db: Session, estoque: Estoque):
    novo_estoque = Estoque(
        quantidade = estoque.quantidade,
        status = estoque.status,
        data_atualizacao = estoque.data_atualizacao,
        jogo_id = estoque.jogo_id
    )

    db.add(novo_estoque)
    db.commit()
    db.refresh(novo_estoque)

    return novo_estoque

def deletar_estoque(db, id):
    estoque = db.query(Estoque).filter(Estoque.id == id).first()

    if not estoque:
        return {"erro": "Estoque não encontrado"}

    db.delete(estoque)
    db.commit()

    return {"mensagem": "Estoque removido com sucesso"}

def atualizar_estoque(db, id, estoque_request):

    estoque = db.query(Estoque).filter(Estoque.id == id).first()

    if not estoque:
        return {"erro": "Estoque não encontrado"}
    
    estoque.quantidade = estoque_request.quantidade
    estoque.status = estoque_request.status
    estoque.data_atualizacao = estoque_request.data_atualizacao
    estoque.jogo_id = estoque_request.jogo_id

    db.commit()

    return estoque