from sqlalchemy import Column, Integer, String, Date, Numeric, DateTime
form app.database.database import Base

class jogo(Base):
    __tablename__ = "Jogos"

    id = Column(Integer, primary_key=True, Index=True, autoincrement=True)
    nome = Column(String(40))
    descricao = Column(String())
    desenvolvedor = Column(String(40))
    lancamento = Column(Date)
