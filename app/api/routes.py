from fastapi import APIRouter

from app.api.routes_auth import router as auth_router
from app.api.routes_providers import router as providers_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(providers_router, prefix="/providers", tags=["providers"])
