from typing import List

from fastapi import APIRouter, Body, Path, status, HTTPException
from fastapi.responses import JSONResponse

from ..data import filmes, avaliacoes
from ..schemas import Avaliacao


router = APIRouter(prefix="/avaliacoes", tags=["Avaliações"])


@router.get(
    path="/"
)
async def lista_avaliacoes() -> List[Avaliacao]:
    """Lista todas as avaliações na base de dados."""
    avaliacoes_serialized = [
        avaliacoe.dict()
        for avaliacoe in avaliacoes
    ]

    return JSONResponse(
        content=avaliacoes_serialized,
        headers={
            "Cashe-Control": "max-age=3600",
        },
    )


@router.get(
    path="/{id_filme}"
)
async def lista_avaliacoes_filme(
    id_filme: int = Path(
        description = "Identificador do filme a ser avaliado.",
        example = 0,
    ),
) -> List[Avaliacao]:
    """Lista todas as avaliações de um filme."""

    if not any(id_filme == f.id_filme for f in filmes):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado."
        )

    avaliacoes_filme = [
        avaliacao.dict() for avaliacao in avaliacoes if avaliacao.id_filme == id_filme
    ]

    return JSONResponse(
        content=avaliacoes_filme,
        headers={
            "Cashe-Control": "max-age=3600",
        },
    )


@router.post(
    path="/avaliacao",
    status_code=status.HTTP_201_CREATED,
)
async def cria_avaliacao(
    avaliacao: Avaliacao = Body(
        description="Informações da avaliação a ser registrada."
    ),
) -> Avaliacao:
    """Registra uma avaliação na base de dados."""

    # Auto incremento do ID
    avaliacao.id_avaliacao = avaliacoes[-1].id_avaliacao + 1

    return avaliacao


@router.delete(
    path="/{id_avaliacao}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def deleta_avaliacao(
    id_avaliacao: int = Path(
        description = "Identificador da avaliação a ser removida.",
        example = 0,
    ),
) -> None:
    """Remove uma avaliação da base de dados."""

    if not any(id_avaliacao == a.id_avaliacao for a in avaliacoes):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Avaliação não encontrada."
        )

    avaliacoes[:] = [
        avaliacao_
        for avaliacao_ in avaliacoes
        if avaliacao_.id_avaliacao != id_avaliacao
    ]

    return None


@router.put(
    path="/{id_avaliacao}",
    status_code=status.HTTP_200_OK,
)
async def atualiza_avaliacao(
    id_avaliacao: int = Path(
        description = "Identificador da avaliação a ser atualizada.",
        example = 0,
    ),
    avaliacao: Avaliacao = Body(description="Informações atualizadas."),
 ) -> Avaliacao:
    """Modifica uma avaliação da base de dados."""

    if not any(id_avaliacao == a.id_avaliacao for a in avaliacoes):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Avaliação não encontrada."
        )

    avaliacoes[:] = [
        avaliacao_
        for avaliacao_ in avaliacoes
        if avaliacao_.id_avaliacao != id_avaliacao
    ]

    avaliacoes.append(avaliacao)

    return avaliacao
