from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.database.database import Base

class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(40))
    descricao = Column(String(250))
    desenvolvedor = Column(String(40))
    lancamento = Column(Date)

    estoques = relationship(
        "Estoque",
        back_populates="jogos"
    )