from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Personal(Base):
    __tablename__ = "personal"

    idPersona = Column(Integer, primary_key=True, index=True)
    idCargo = Column(Integer)
    nombre = Column(String)
    documento = Column(String)
    correo = Column(String)
    telefono = Column(String)
    estado = Column(Boolean)