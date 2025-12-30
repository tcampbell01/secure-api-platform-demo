from datetime import datetime, timedelta, timezone
import hashlib
import logging

import bcrypt
from jose import jwt

from app.core.config import settings

logger = logging.getLogger("security")

logger.warning("Loaded security module from %s", __file__)
logger.warning("JWT_SECRET length (chars) = %s", len(settings.jwt_secret))


# ---------- Password hashing ----------

def _pepper_and_prehash(password: str) -> bytes:
    """
    bcrypt has a strict 72-byte input limit.
    We permanently avoid it by pre-hashing to exactly 32 bytes
    using SHA-256 + a server-side pepper (JWT_SECRET).
    """
    if not isinstance(password, str):
        raise TypeError(f"password must be str, got {type(password)}")

    combined = (password + settings.jwt_secret).encode("utf-8")
    digest = hashlib.sha256(combined).digest()  # ALWAYS 32 bytes

    # Hard guarantees — if these fail, something is fundamentally wrong
    assert len(digest) == 32, f"Expected 32-byte digest, got {len(digest)}"
    assert len(digest) <= 72, f"bcrypt input too long: {len(digest)} bytes"

    return digest


def hash_password(password: str) -> str:
    pre = _pepper_and_prehash(password)
    logger.warning(
        "hash_password called (pwd chars=%s, prehash bytes=%s)",
        len(password),
        len(pre),
    )

    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(pre, salt)  # returns bytes: b"$2b$..."

    return hashed.decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    pre = _pepper_and_prehash(password)
    logger.warning(
        "verify_password called (pwd chars=%s, prehash bytes=%s)",
        len(password),
        len(pre),
    )

    return bcrypt.checkpw(pre, password_hash.encode("utf-8"))


# ---------- JWT handling ----------

def create_access_token(subject: str) -> str:
    """
    Create a signed JWT access token.
    """
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=settings.access_token_exp_minutes)

    payload = {
        "sub": subject,
        "iat": int(now.timestamp()),
        "exp": int(expire.timestamp()),
    }

    return jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )
