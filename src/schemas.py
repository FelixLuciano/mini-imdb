from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, condecimal


class Classificação_enum(Enum):
    """"Faixas de classificação do Sistema de Classificação Indicativa Brasileiro"""
    LIVRE = "LIVRE"
    MENORES_DE_10_ANOS = "Não recomendado para menores de 10 anos"
    MENORES_DE_12_ANOS = "Não recomendado para menores de 12 anos"
    MENORES_DE_14_ANOS = "Não recomendado para menores de 14 anos"
    MENORES_DE_16_ANOS = "Não recomendado para menores de 16 anos"
    MENORES_DE_18_ANOS = "Não recomendado para menores de 18 anos"

class Filme_base(BaseModel):
    """Objeto Filme base"""

    titulo: str = Field(
        title="Título do filme.",
        max_length=100,
        example="O Poderoso Chefão",
    )
    ano: int = Field(
        title="Ano em que o filme foi lançado",
        ge=1_700,
        le=3_000,
        example=1972,
    )
    pais: str = Field(
        title="País em que o filme foi produzido",
        max_length=50,
        example="Brasil",
    )
    diretor: str = Field(
        title="Nome do diretor do filme",
        max_length=100,
        example="Francis Ford Coppola",
    )
    genero: str = Field(
        title="Gênero do filme",
        max_length=30,
        example="Drama, Crime",
    )
    idioma: str = Field(
        title="Idioma original do filme",
        max_length=30,
        example="pt-BR",
    )
    duracao: int = Field(
        title="Duração do filme em minutos",
        ge=1,
        le=360,
        example=176,
    )
    sinopse: str = Field(
        title="Breve descrição do enredo do filme",
        max_length=1_000,
        example='um clássico dirigido por Francis Ford Coppola que conta a história da família Corleone, uma poderosa máfia ítalo-americana em Nova York. A trama é repleta de conflitos entre as famílias mafiosas rivais, e apresenta temas como violência, poder, dinheiro, família e traição. Com um elenco de estrelas, incluindo Marlon Brando, Al Pacino, James Caan e Robert Duvall, o filme foi um sucesso comercial e crítico, vencendo três Oscars, incluindo o de Melhor Filme. "O Poderoso Chefão" é considerado um marco na história do cinema e um exemplo notável de uma obra-prima da arte cinematográfica.',
    )
    classificacao: Classificação_enum = Field(
        title="Classificação etária do filme em anos. Padrão: LIVRE",
        example=Classificação_enum.MENORES_DE_14_ANOS,
        default=Classificação_enum.LIVRE,
    )


class Filme(Filme_base):
    """Objeto Filme"""

    id_filme: Optional[int] = Field(
        title="ID único do filme na base de dados.",
        description="Propriedade automática. Inteiro positivo.",
        ge=1,
    )

    class Config:
        orm_mode = True


class Avaliacao_base(BaseModel):
    """Avaliação base de um filme feita por um usuário"""

    id_filme: int = Field(
        title="Identificador do filme avaliado.",
        description="Inteiro positivo.",
        ge=1,
    )
    nota: condecimal(ge=0, le=10, max_digits=1, decimal_places=1) = Field(
        title="Nota atribuída ao filme.",
        description="Número real entre 0 e 10.",
        example=8.5,
    )
    comentario: str = Field(
        title="Comentario elaborado sobre o filme.",
        description="Texto livre com até 400 caracteres.",
        max_length=400,
        example="Um clássico do cinema.",
    )


class Avaliacao(Avaliacao_base):
    """Avaliação de um filme feita por um usuário"""

    id_avaliacao: Optional[int] = Field(
        title="ID único da avaliação na base de dados.",
        description="Propriedade automática. Inteiro positivo.",
        ge=1,
    )

    class Config:
        orm_mode = True
