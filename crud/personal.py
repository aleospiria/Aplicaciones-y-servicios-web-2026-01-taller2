from sqlalchemy.orm import Session
from models.personal import Personal
from schemas.personal import PersonalCreate, PersonalUpdate

def crear_personal(db: Session, data: PersonalCreate):
    obj = Personal(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def listar_personal(db: Session):
    return db.query(Personal).all()

def obtener_personal(db: Session, id: int):
    return db.query(Personal).filter(Personal.idPersona == id).first()

def actualizar_personal(db: Session, id: int, data: PersonalUpdate):
    obj = obtener_personal(db, id)
    if not obj:
        return None
    for key, value in data.model_dump(exclude_none=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def eliminar_personal(db: Session, id: int):
    obj = obtener_personal(db, id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj