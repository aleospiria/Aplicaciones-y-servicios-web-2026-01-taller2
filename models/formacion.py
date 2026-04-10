from sqlalchemy import Column, Integer, String, Date
from database import Base

class Formacion(Base):
    __tablename__ = "formacion"

    idFormacion = Column(Integer, primary_key=True, index=True)
    idPersona = Column(Integer)
    nivelDeFormacion = Column(String)
    tituloObtenido = Column(String)
    institucion = Column(String)
    fechaFinal = Column(Date)