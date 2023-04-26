from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Filme(Base):
    __tablename__ = "filmes"

    id_filme = Column(Integer(), primary_key=True, autoincrement=True)
    titulo   = Column(String(45), nullable=False)


class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id_avaliacao = Column(Integer(), primary_key=True, autoincrement=True)
    id_filme     = Column(Integer(), ForeignKey("filmes.id_filme"), nullable=False)
    nota         = None
    comentario   = None
