from dotenv import load_dotenv
import os

load_dotenv()  # ładuje zmienne z pliku .env

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY=supersecretkey

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Movie API")

app.include_router(routers.router)
