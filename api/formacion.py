from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.formacion import FormacionCreate, FormacionUpdate, FormacionOut
import crud.formacion as crud

router = APIRouter(prefix="/formacion", tags=["Formacion"])

@router.post("/", response_model=FormacionOut)
def crear(data: FormacionCreate, db: Session = Depends(get_db)):
    return crud.crear_formacion(db, data)

@router.get("/", response_model=list[FormacionOut])
def listar(db: Session = Depends(get_db)):
    return crud.listar_formacion(db)

@router.get("/{id}", response_model=FormacionOut)
def obtener(id: int, db: Session = Depends(get_db)):
    obj = crud.obtener_formacion(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Formación no encontrada")
    return obj

@router.put("/{id}", response_model=FormacionOut)
def actualizar(id: int, data: FormacionUpdate, db: Session = Depends(get_db)):
    obj = crud.actualizar_formacion(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Formación no encontrada")
    return obj

@router.delete("/{id}", response_model=FormacionOut)
def eliminar(id: int, db: Session = Depends(get_db)):
    obj = crud.eliminar_formacion(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Formación no encontrada")
    return obj