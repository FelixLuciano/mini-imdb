from sqlalchemy.orm import Session

import models
import schemas


def lista_filmes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Filme)\
             .offset(skip)\
             .limit(limit)\
             .all()


def cria_filme(db: Session, filme: schemas.Filme):
    new_filme = models.Filme(**filme.dict(), id=0)

    db.add(new_filme)
    db.commit()
    db.refresh(new_filme)

    return new_filme


def lista_avaliacoes_filme(db: Session, id_filme: int, skip: int = 0, limit: int = 100):
    return db.query(models.Avaliacao)\
             .filter(models.Avaliacao.id_filme == id_filme)\
             .offset(skip)\
             .limit(limit)\
             .all()
