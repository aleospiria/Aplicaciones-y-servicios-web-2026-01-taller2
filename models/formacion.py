from sqlalchemy import Column, Integer, String, Date
from database import Base
import os
from dotenv import load_dotenv

load_dotenv()
SCHEMA = os.getenv("SCHEMA")

class Formacion(Base):
    __tablename__ = "formacion"
    __table_args__ = {"schema": SCHEMA}

    idFormacion = Column(Integer, primary_key=True, index=True)
    idPersona = Column(Integer)
    nivelDeFormacion = Column(String)
    tituloObtenido = Column(String)
    institucion = Column(String)
    fechaFinal = Column(Date)