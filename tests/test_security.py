import pytest

from app.core.security import (
    hash_password,
    verify_password,
    _pepper_and_prehash,
)

def test_password_is_hashed_and_verifiable():
    password = "TestPass123!"

    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("wrongpassword", hashed)


def test_bcrypt_input_never_exceeds_72_bytes():
    long_password = "A" * 500  # deliberately extreme

    prehashed = _pepper_and_prehash(long_password)

    # bcrypt hard limit safety check
    assert len(prehashed) <= 72


def test_hashes_are_non_deterministic():
    password = "TestPass123!"

    h1 = hash_password(password)
    h2 = hash_password(password)

    # bcrypt salt should differ
    assert h1 != h2
