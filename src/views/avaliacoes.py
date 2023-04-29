from typing import List

from fastapi import APIRouter, Body, Path, status, HTTPException
from sqlalchemy.exc import NoResultFound

from ..models import Avaliacao as Avaliacao_model
from ..models import Filme as Filme_model
from ..schemas import Avaliacao_base as Avaliacao_base_schema
from ..schemas import Avaliacao_filme as Avaliacao_filme_schema
from ..schemas import Avaliacao as Avaliacao_schema
from ..database import SessionLocal


router = APIRouter(prefix="/avaliacoes", tags=["Avaliações"])
db = SessionLocal()


@router.get(
    path="/"
)
async def lista_avaliacoes() -> List[Avaliacao_schema]:
    """Lista todas as avaliações na base de dados."""

    return db.query(Avaliacao_model).all()


@router.get(
    path="/{id_filme}"
)
async def lista_avaliacoes_filme(
    id_filme: int = Path(
        description = "Identificador do filme a ser avaliado.",
        example = 0,
    ),
) -> List[Avaliacao_filme_schema]:
    """Lista todas as avaliações de um filme."""

    return db.query(Avaliacao_model)\
             .filter(Avaliacao_model.id_filme == id_filme)\
             .all()


@router.post(
    path="/{id_filme}",
    status_code=status.HTTP_201_CREATED,
)
async def cria_avaliacao(
    id_filme: int = Path(
        description = "Identificador do filme a ser avaliado.",
        example = 1,
    ),
    avaliacao: Avaliacao_base_schema = Body(
        description="Informações da avaliação a ser registrada."
    ),
) -> Avaliacao_schema:
    """Registra uma avaliação na base de dados."""

    try:
        db.query(Filme_model)\
          .filter(Filme_model.id_filme == id_filme)\
          .first()
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado."
        )

    new_avaliacao = Avaliacao_model(id_filme=id_filme, **avaliacao.dict())

    db.add(new_avaliacao)
    db.commit()
    db.refresh(new_avaliacao)

    return new_avaliacao


@router.delete(
    path="/{id_avaliacao}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def deleta_avaliacao(
    id_avaliacao: int = Path(
        description = "Identificador da avaliação a ser removida.",
        example = 1,
    ),
) -> None:
    """Remove uma avaliação da base de dados."""

    try:
        avaliacao = db.query(Avaliacao_model)\
                        .filter(Avaliacao_model.id_avaliacao == id_avaliacao)\
                        .one()

        db.delete(avaliacao)
        db.commit()
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Avaliação não encontrada."
        )


@router.put(
    path="/{id_avaliacao}",
    status_code=status.HTTP_200_OK,
)
async def atualiza_avaliacao(
    id_avaliacao: int = Path(
        description = "Identificador da avaliação a ser atualizada.",
        example = 0,
    ),
    avaliacao: Avaliacao_base_schema = Body(description="Informações atualizadas."),
 ) -> Avaliacao_schema:
    """Modifica uma avaliação da base de dados."""

    try:
        new_avaliacao = db.query(Avaliacao_model)\
                          .filter(Avaliacao_model.id_avaliacao == id_avaliacao)\
                          .one()
    
        for key, value in avaliacao.dict().items():
            setattr(new_avaliacao, key, value)

        db.add(new_avaliacao)
        db.commit()
        db.refresh(new_avaliacao)
        
        return new_avaliacao
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado."
        )
