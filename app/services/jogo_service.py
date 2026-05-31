from sqlalchemy.orm import Session
from app.models.jogo import Jogo
from app.models.jogos_schema import jogoSchema

def listar_jogos(db: Session):
    return db.query(Jogo).all()

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