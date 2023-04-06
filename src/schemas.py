from pydantic import BaseModel, Field
from typing import Optional


class Filme(BaseModel):
    """Objeto Filme"""

    id_filme: Optional[int] = Field(
        title="ID único do filme na base de dados.",
        description="Propriedade automática. Inteiro positivo.",
        ge = 0,
    )
    titulo: str = Field(
        title="Título do filme.",
        max_length=100,
        example = "O Poderoso Chefão",
    )


class Avaliacao(BaseModel):
    """Avaliação de um filme feita por um usuário"""

    id_avaliacao: Optional[int] = Field(
        title="ID único da avaliação na base de dados.",
        description="Propriedade automática. Inteiro positivo.",
        ge = 0,

    )
    id_filme: int = Field(
        title="Identificador do filme avaliado.",
        description="Inteiro positivo.",
        ge = 0,
    )
    nota: float = Field(
        title="Nota atribuída ao filme.",
        description="Número real entre 0 e 10.",
        ge = 0,
        le = 10,
        example = 8.5,

    )
    comentario: str = Field(
        title="Comentario elaborado sobre o filme.",
        description="Texto livre com até 400 caracteres.",
        max_length=400,
        example = "Um clássico do cinema.",
    )
