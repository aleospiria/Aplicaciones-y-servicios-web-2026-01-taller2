from pydantic import BaseModel
from typing import Optional
from datetime import date

class FormacionCreate(BaseModel):
    idPersona:        int
    nivelDeFormacion: str
    tituloObtenido:   str
    institucion:      str
    fechaFinal:       date

class FormacionUpdate(BaseModel):
    idPersona:        Optional[int]  = None
    nivelDeFormacion: Optional[str]  = None
    tituloObtenido:   Optional[str]  = None
    institucion:      Optional[str]  = None
    fechaFinal:       Optional[date] = None

class FormacionOut(FormacionCreate):
    idFormacion: int
    class Config:
        from_attributes = True