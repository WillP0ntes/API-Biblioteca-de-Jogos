from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database.database import Base

class Estoque(Base):
    __tablename__ = "estoques"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quantidade = Column(Integer)
    ativo = Column(Boolean)
    data_atualizacao = Column(Date)

    jogo_id = Column(
        Integer,
        ForeignKey("jogos.id"),
        nullable=False
    )

    jogos = relationship(
        "Jogo",
        back_populates="estoque"
    )
