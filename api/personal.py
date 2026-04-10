from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.personal import PersonalCreate, PersonalUpdate, PersonalOut
import crud.personal as crud

router = APIRouter(prefix="/personal", tags=["Personal"])

@router.post("/", response_model=PersonalOut)
def crear(data: PersonalCreate, db: Session = Depends(get_db)):
    return crud.crear_personal(db, data)

@router.get("/", response_model=list[PersonalOut])
def listar(db: Session = Depends(get_db)):
    return crud.listar_personal(db)

@router.get("/{id}", response_model=PersonalOut)
def obtener(id: int, db: Session = Depends(get_db)):
    obj = crud.obtener_personal(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    return obj

@router.put("/{id}", response_model=PersonalOut)
def actualizar(id: int, data: PersonalUpdate, db: Session = Depends(get_db)):
    obj = crud.actualizar_personal(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    return obj

@router.delete("/{id}", response_model=PersonalOut)
def eliminar(id: int, db: Session = Depends(get_db)):
    obj = crud.eliminar_personal(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    return obj