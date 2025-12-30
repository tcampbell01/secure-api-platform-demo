from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth_deps import get_current_user_email
from app.db.deps import get_db
from app.models.provider import Provider
from app.schemas.provider import ProviderCreate, ProviderOut

router = APIRouter()


@router.get("/", response_model=list[ProviderOut])
def list_providers(
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user_email),
):
    return db.query(Provider).order_by(Provider.id.desc()).all()


@router.post("/", response_model=ProviderOut)
def create_provider(
    payload: ProviderCreate,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user_email),
):
    provider = Provider(**payload.model_dump())
    db.add(provider)
    db.commit()
    db.refresh(provider)
    return provider

