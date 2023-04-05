from typing import List

from fastapi import APIRouter, Body, Path, status

from ..data import filmes, avaliacoes
from ..schemas import Avaliacao


router = APIRouter(prefix="/avaliacoes", tags=["Avaliações"])


@router.get("/")
async def lista_avaliacoes() -> List[Avaliacao]:
    """Lista todas as avaliações na base de dados."""
    return avaliacoes


@router.get("/{id_filme}")
async def lista_avaliacoes_filme(id_filme: int = Path(description="Identificador do filme a ser avaliado.")):
    """Lista todas as avaliações de um filme."""
    avaliacoes_filme = [
        avaliacao for avaliacao in avaliacoes if avaliacao.id_filme == id_filme
    ]
    media_avaliacoes_filme = sum([aval.nota for aval in avaliacoes_filme]) / len(
        avaliacoes_filme
    )
    filme = [
        {
            "titulo": f.titulo,
            "media": media_avaliacoes_filme,
            "avaliacoes": [
                {
                    "nota": a.nota,
                    "comentario": a.comentario,
                }
                for a in avaliacoes_filme
            ],
        }
        for f in filmes
        if f.id_filme == id_filme
    ][0]

    return filme


@router.post(
    "/avaliacao",
    status_code=status.HTTP_201_CREATED,
    response_model=Avaliacao
)
async def cria_avaliacao(avaliacao: Avaliacao = Body(description="Informações da avaliação a ser registrada.")):
    """Registra uma avaliação na base de dados."""
    # Auto incremento do ID
    avaliacao.id_avaliacao = avaliacoes[-1].id_avaliacao + 1

    # Clamping da nota para faixa de 0 a 10
    avaliacao.nota = min(max(avaliacao.nota, 0.0), 10.0)

    avaliacoes.routerend(avaliacao)
    return avaliacao


@router.delete(
    "/{id_avaliacao}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None
)
async def deleta_avaliacao(id_avaliacao: int = Path(description="Identificador da avaliação a ser removida.")):
    """Remove uma avaliação da base de dados."""
    avaliacoes[:] = [a for a in avaliacoes if a.id_avaliacao != id_avaliacao]
    return None


@router.put(
    "/{id_avaliacao}",
    status_code=status.HTTP_200_OK,
    response_model=Avaliacao
)
async def atualiza_avaliacao(id_avaliacao: int = Path(description="Identificador da avaliação a ser atualizada."), avaliacao: Avaliacao = Body(description="Informações atualizadas.")):
    """Modifica uma avaliação da base de dados."""
    avaliacoes[:] = [a for a in avaliacoes if a.id_avaliacao != id_avaliacao]
    avaliacoes.routerend(avaliacao)
    return avaliacao
