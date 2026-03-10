from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SeriesSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SeriesSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.put("/")
async def atualizar_serie(id: int, dados: SeriesSchema, db: Session = Depends(get_db)):
    serie = db.query(SerieModel).filter(SerieModel.id == id).first()
    
    for campo, valor in dados.model_dump().items():
        setattr (serie, campo, valor)
    
    db.commit()
    db.refresh(serie)
    return serie

@serie.delete("/")
async def apagar_serie(id: int, db: Session = Depends(get_db)):
    serie = db.query(SerieModel).filter(SerieModel.id == id).first()

    db.delete(serie)
    db.commit()

    return serie

