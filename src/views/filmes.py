from typing import List

from fastapi import APIRouter, Body, Path, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..models import Filme as Filme_model
from ..schemas import Filme as Filme_Schema
from ..database import SessionLocal


router = APIRouter(prefix="/filmes", tags=["Filmes"])
db = SessionLocal()


@router.get(
    path="/",
)
async def lista_filmes() -> List[Filme_Schema]:
    """Lista todos os filmes na base de dados."""
    return db.query(Filme_model)\
             .all()


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    description="Informações do filme a ser registrado.",
    response_model=Filme_Schema,

)
async def cria_filme(filme: Filme_Schema):
    """Registra um filme na base de dados."""
    new_filme = Filme_model(**filme.dict())

    db.add(new_filme)
    db.commit()
    # db.refresh(new_filme)

    return filme



# @router.delete(
#     path="/{id_filme}",
#     status_code=status.HTTP_204_NO_CONTENT,
# )
# async def deleta_filme(
#     id_filme: int = Path(
#         description = "Identificador do filme a ser removido.",
#         example = 0,
#     ),
# ) -> None:
#     """Remove um filme da base de dados."""

#     if not any(id_filme == f.id_filme for f in filmes):
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Filme não encontrado."
#         )

#     filmes[:] = [
#         filme_
#         for filme_ in filmes
#         if filme_.id_filme != id_filme
#     ]

#     return None


# @router.put(
#     path="/{id_filme}",
#     status_code=status.HTTP_200_OK,
# )
# async def atualiza_filme(
#     id_filme: int = Path(
#         description = "Identificador do filme a ser modificado.",
#         example = 0,
#     ),
#     filme: Filme = Body(description="Informações atualizadas."),
# ) -> Filme:
#     """Modifica um filme da base de dados."""

#     if not any(id_filme == f.id_filme for f in filmes):
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Filme não encontrado."
#         )

#     filmes[:] = [
#         filme_
#         for filme_ in filmes
#         if filme_.id_filme != id_filme
#     ]

#     filmes.append(filme)

#     return filme
