from app.db.session import Base, engine
from app.models.user import User  # noqa: F401
from app.models.provider import Provider  # noqa: F401


def init() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init()

