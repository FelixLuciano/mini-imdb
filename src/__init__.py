from fastapi import FastAPI

from .view import router


app = FastAPI(
    title="Mini IMDB",
    description="Projeto da disciplina de Megadados",
    version="0.1.0",
)

app.include_router(router)
