from fastapi import APIRouter

from .routes.avaliacoes import router as router_avaliacoes
from .routes.filmes import router as router_filmes


router = APIRouter()

router.include_router(router_filmes)
router.include_router(router_avaliacoes)
