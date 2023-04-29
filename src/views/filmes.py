from typing import List

from fastapi import APIRouter, Body, Path, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from ..models import Filme as Filme_model
from ..schemas import Filme_base as Filme_base_schema
from ..schemas import Filme as Filme_schema
from ..database import SessionLocal


router = APIRouter(prefix="/filmes", tags=["Filmes"])
db = SessionLocal()


@router.get(
    path="/",
)
async def lista_filmes() -> List[Filme_schema]:
    """Lista todos os filmes na base de dados."""
    return db.query(Filme_model).all()


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    description="Informações do filme a ser registrado.",
    response_model=Filme_schema,
)
async def cria_filme(filme: Filme_base_schema):
    """Registra um filme na base de dados."""
    new_filme = Filme_model(**filme.dict())

    db.add(new_filme)
    db.commit()
    db.refresh(new_filme)

    return new_filme


@router.delete(
    path="/{id_filme}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def deleta_filme(
    id_filme: int = Path(
        description = "Identificador do filme a ser removido.",
        example = 0,
    ),
) -> None:
    """Remove um filme da base de dados."""

    try:
        filme = db.query(Filme_model)\
                .filter(Filme_model.id_filme == id_filme)\
                .one()

        db.delete(filme)
        db.commit()
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado."
        )


@router.put(
    path="/{id_filme}",
    status_code=status.HTTP_200_OK,
)
async def atualiza_filme(
    id_filme: int = Path(
        description = "Identificador do filme a ser modificado.",
        example = 0,
    ),
    filme: Filme_base_schema = Body(description="Informações atualizadas."),
) -> Filme_schema:
    """Modifica um filme da base de dados."""

    try:
        new_filme = Filme_model(id_filme=id_filme, **filme.dict())

        db.query(Filme_model).filter(Filme_model.id_filme == id_filme).update(new_filme)
        db.commit()
        db.refresh(new_filme)

        return new_filme
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado."
        )
