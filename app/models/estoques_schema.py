from pydantic import BaseModel
from datetime import date

class estoqueSchema(BaseModel):
    quantidade: int
    status: bool
    data_atualizacao: date
    jogo_id: int