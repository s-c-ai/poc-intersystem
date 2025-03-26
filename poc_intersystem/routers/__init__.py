from fastapi import APIRouter

from .database import router as database_router
from .users import router as users_router

router = APIRouter()
router.include_router(database_router)
router.include_router(users_router)
