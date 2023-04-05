from .schemas import Filme, Avaliacao


filmes = [
    Filme(
        id_filme=0,
        titulo="Filme teste",
    ),
    Filme(
        id_filme=1,
        titulo="Filme teste: O retorno",
    ),
]

avaliacoes = [
    Avaliacao(
        id_avaliacao=0,
        id_filme=0,
        nota=10.0,
        comentario="Muito bom!",
    ),
    Avaliacao(
        id_avaliacao=1,
        id_filme=0,
        nota=8.0,
        comentario="Muito bom mesmo!",
    ),
    Avaliacao(
        id_avaliacao=2,
        id_filme=1,
        nota=0.0,
        comentario="Muito ruim!",
    ),
    Avaliacao(
        id_avaliacao=3,
        id_filme=1,
        nota=2.0,
        comentario="Ruim demais!",
    ),
]