from pydantic import BaseModel
from typing import Optional
from datetime import date

class PersonalCreate(BaseModel):
    idCargo:   int
    nombre:    str
    documento: str
    correo:    str
    telefono:  str
    estado:    bool

class PersonalUpdate(BaseModel):
    idCargo:   Optional[int]   = None
    nombre:    Optional[str]   = None
    documento: Optional[str]   = None
    correo:    Optional[str]   = None
    telefono:  Optional[str]   = None
    estado:    Optional[bool]  = None

class PersonalOut(PersonalCreate):
    idPersona: int
    class Config:
        from_attributes = True