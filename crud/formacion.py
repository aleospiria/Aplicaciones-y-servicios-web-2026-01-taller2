from sqlalchemy.orm import Session
from models.formacion import Formacion
from schemas.formacion import FormacionCreate, FormacionUpdate

def crear_formacion(db: Session, data: FormacionCreate):
    obj = Formacion(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def listar_formacion(db: Session):
    return db.query(Formacion).all()

def obtener_formacion(db: Session, id: int):
    return db.query(Formacion).filter(Formacion.idFormacion == id).first()

def actualizar_formacion(db: Session, id: int, data: FormacionUpdate):
    obj = obtener_formacion(db, id)
    if not obj:
        return None
    for key, value in data.model_dump(exclude_none=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def eliminar_formacion(db: Session, id: int):
    obj = obtener_formacion(db, id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj