from pydantic import BaseModel
from datetime import date

class jogoSchema(BaseModel):
    nome: str
    descricao: str
    desenvolvedor: str
    lancamento: date