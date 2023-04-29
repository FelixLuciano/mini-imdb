from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
# from sqlalchemy.orm import relationship

from .database import Base


class Filme(Base):
    __tablename__ = "filmes"

    id_filme      = Column(Integer(), primary_key=True, autoincrement=True)
    titulo        = Column(String(45), nullable=False)
    ano           = Column(Integer(), nullable=False)
    pais          = Column(String(50), nullable=False)
    diretor       = Column(String(100), nullable=False)
    genero        = Column(String(30), nullable=False)
    idioma        = Column(String(30), nullable=False)
    duracao       = Column(Integer(), nullable=False)
    sinopse       = Column(String(1_000), nullable=False)
    classificacao = Column(String(50))


class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id_avaliacao = Column(Integer(), primary_key=True, autoincrement=True)
    id_filme     = Column(Integer(), ForeignKey("filmes.id_filme"), nullable=False)
    nota         = Column(DECIMAL(3, 1), nullable=False)
    comentario   = Column(String(1_000), nullable=False)
