from fastapi import APIRouter

from . import pdftopng

router = APIRouter(prefix='/utils')

router.include_router(pdftopng.router)