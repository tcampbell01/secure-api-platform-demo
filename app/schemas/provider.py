from pydantic import BaseModel


class ProviderCreate(BaseModel):
    name: str
    specialty: str | None = None
    city: str | None = None
    state: str | None = None


class ProviderOut(BaseModel):
    id: int
    name: str
    specialty: str | None
    city: str | None
    state: str | None

    class Config:
        from_attributes = True

