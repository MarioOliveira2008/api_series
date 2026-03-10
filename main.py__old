from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"mensagem": "Ola, Mundo"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/soma/{a}/{b}")
async def soma(a: int, b: int):
    return{"resultado": a + b}

