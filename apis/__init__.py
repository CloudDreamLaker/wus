from fastapi import APIRouter

from . import utils

router = APIRouter(prefix='')

router.include_router(utils.router)