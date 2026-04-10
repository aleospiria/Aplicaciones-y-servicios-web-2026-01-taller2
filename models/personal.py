from sqlalchemy import Column, Integer, String, Boolean
from database import Base
import os
from dotenv import load_dotenv

load_dotenv()
SCHEMA = os.getenv("SCHEMA")

class Personal(Base):
    __tablename__ = "personal"
    __table_args__ = {"schema": SCHEMA}

    idPersona = Column(Integer, primary_key=True, index=True)
    idCargo = Column(Integer)
    nombre = Column(String)
    documento = Column(String)
    correo = Column(String)
    telefono = Column(String)
    estado = Column(Boolean)