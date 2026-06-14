from sqlalchemy.orm import Session
from app.models.estoque import Estoque
from app.models.estoques_schema import estoqueSchema

def listar_estoques(db: Session):
    return db.query(Estoque).all()