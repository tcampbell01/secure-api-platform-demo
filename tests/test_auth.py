from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login_flow():
    email = "testuser@example.com"
    password = "TestPass123!"

    register = client.post(
        "/auth/register",
        json={"email": email, "password": password},
    )
    assert register.status_code == 200
    assert "access_token" in register.json()

    login = client.post(
        "/auth/login",
        json={"email": email, "password": password},
    )
    assert login.status_code == 200
    assert "access_token" in login.json()
