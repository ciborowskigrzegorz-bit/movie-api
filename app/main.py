from fastapi import FastAPI
from app import models, database, routers

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Movie API")

app.include_router(routers.router)
