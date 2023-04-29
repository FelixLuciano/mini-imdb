from dotenv import load_dotenv
from fastapi import FastAPI


load_dotenv()

from .database import Base, engine
from .views import router


app = FastAPI(
    title="Mini IMDB 🎬",
    description="Projeto da disciplina de Megadados",
    version="0.1.0",
)

app.include_router(router)
Base.metadata.create_all(engine)
