import os
from fastapi import FastAPI
from dotenv import load_dotenv

from app import models, database, routers

# Ładowanie zmiennych środowiskowych
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in environment variables")

# Tworzenie bazy danych (jeśli jeszcze nie istnieje)
models.Base.metadata.create_all(bind=database.engine)

# Inicjalizacja FastAPI
app = FastAPI(title="Movie API")

# Dołączanie routerów
app.include_router(routers.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Movie API"}
