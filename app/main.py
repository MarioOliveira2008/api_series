from fastapi import FastAPI
from app.database import Base, engine
from app.route.serie import serie

#Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(serie)

@app.get("/series")
async def health_check():
    return {"status": "API Online"}



