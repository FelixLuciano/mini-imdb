from fastapi import APIRouter

from .avaliacoes import router as avaliacoes_router
from .filmes import router as filmes_router


router = APIRouter(prefix="/api")

router.include_router(avaliacoes_router)
router.include_router(filmes_router)
