from fastapi import FastAPI

from app.database.database import engine, Base
from app.routes.jogo_route import router
from app.routes.estoque_route import router
from app.models.jogo import Jogo 
from app.models.estoque import Estoque 

app = FastAPI(title="API Biblioteca de Jogos")
app.include_router(router)

Base.metadata.create_all(bind=engine)