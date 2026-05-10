from fastapi import APIRouter
from .endpoints import create_file

router = APIRouter(prefix="/api/v1")
router.include_router(create_file.router)
