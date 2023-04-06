from typing import List

from fastapi import APIRouter, Body, Path, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from ..data import filmes
from ..schemas import Filme


router = APIRouter(prefix="/filmes", tags=["Filmes"])


@router.get(
    path="/",
)
async def lista_filmes() -> List[Filme]:
    """Lista todos os filmes na base de dados."""
    filmes_serialized = [filme.dict() for filme in filmes]

    return JSONResponse(
        content=filmes_serialized,
        headers={
            "Cashe-Control": "max-age=3600",
        },
    )


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    description="Informações do filme a ser registrado.",
    response_model=Filme,

)
async def cria_filme(filme: Filme):
    """Registra um filme na base de dados."""

    # Auto incremento do ID
    filme.id_filme = filmes[-1].id_filme + 1

    return filme


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

    if not any(id_filme == f.id_filme for f in filmes):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado."
        )

    filmes[:] = [
        filme_
        for filme_ in filmes
        if filme_.id_filme != id_filme
    ]

    return None


@router.put(
    path="/{id_filme}",
    status_code=status.HTTP_200_OK,
)
async def atualiza_filme(
    id_filme: int = Path(
        description = "Identificador do filme a ser modificado.",
        example = 0,
    ),
    filme: Filme = Body(description="Informações atualizadas."),
) -> Filme:
    """Modifica um filme da base de dados."""

    if not any(id_filme == f.id_filme for f in filmes):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado."
        )

    filmes[:] = [
        filme_
        for filme_ in filmes
        if filme_.id_filme != id_filme
    ]

    filmes.append(filme)

    return filme
