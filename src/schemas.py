from pydantic import BaseModel, Field
from typing import Optional


class Filme(BaseModel):
    """Objeto Filme"""

    id_filme: Optional[int] = Field(
        title="ID único do filme na base de dados. Propriedade automática.",
    )
    titulo: str = Field(
        title="Título do filme.",
        max_length=100,
    )


class Avaliacao(BaseModel):
    """Avaliação de um filme feita por um usuário"""

    id_avaliacao: Optional[int] = Field(
        title="ID único da avaliação na base de dados. Propriedade automática.",
    )
    id_filme: int = Field(
        title="Identificador do filme avaliado.",
    )
    nota: float = Field(
        title="Nota, de 0 a 10, para o filme.",
    )
    comentario: str = Field(
        title="Crítica elaborada sobre o filme.",
        max_length=400,
    )
