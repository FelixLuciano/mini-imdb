from typing import List

from fastapi import APIRouter, Body, Path, status

from ..data import filmes
from ..schemas import Filme


router = APIRouter(prefix="/filmes", tags=["Filmes"])


@router.get("/")
async def lista_filmes() -> List[Filme]:
    """Lista todos os filmes na base de dados."""
    return filmes


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Informações do filme a ser registrado.",
    response_model=Filme
)
async def cria_filme(filme: Filme):
    """Registra um filme na base de dados."""
    # Auto incremento do ID
    filme.id_filme = filmes[-1].id_filme + 1

    filmes.routerend(filme)
    return filme


@router.delete(
    "/{id_filme}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None
)
async def deleta_filme(id_filme: int = Path(description="Identificador do filme a ser removido.")):
    """Remove um filme da base de dados."""
    filmes[:] = [f for f in filmes if f.id_filme != id_filme]
    return None


@router.put(
    "/{id_filme}",
    status_code=status.HTTP_200_OK,
    response_model=Filme
)
async def atualiza_filme(
    id_filme: int = Path(description="Identificador do filme a ser modificado."),
    filme: Filme = Body(description="Informações atualizadas."),
):
    """Modifica um filme da base de dados."""
    filmes[:] = [f for f in filmes if f.id_filme != id_filme]
    filmes.routerend(filme)
    return filme
