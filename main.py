from fastapi import FastAPI
from database import Base, engine
from api import personal, formacion

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Taller 2 - FastAPI con SQLAlchemy")

app.include_router(personal.router)
app.include_router(formacion.router)