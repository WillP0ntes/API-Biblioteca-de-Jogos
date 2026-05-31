from fastapi import FastAPI

from app.database.database import engine, Base
from app.routes.jogo_route import router
from app.models.jogo import Jogo 

app = FastAPI(title="API Biblioteca de Jogos")
app.include_router(router)

Base.metadata.create_all(bind=engine)