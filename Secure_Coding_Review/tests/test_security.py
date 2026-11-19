
import sys
from pathlib import Path

import pytest

# Make the secure_app folder importable.
PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR / "secure_app"))

import app as secure_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Use a temporary database for every test.
    test_database = tmp_path / "test_users.db"
    monkeypatch.setattr(secure_app, "DATABASE", test_database)

    secure_app.initialize_database()
    secure_app.app.config["TESTING"] = True

    with secure_app.app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_secure_registration(client):
    response = client.post(
        "/register",
        data={"username": "jeddy", "password": "StrongPassword123!"}
    )
    assert response.status_code == 201


def test_short_password_rejected(client):
    response = client.post(
        "/register",
        data={"username": "jeddy", "password": "weak"}
    )
    assert response.status_code == 400


def test_duplicate_username_rejected(client):
    data = {"username": "jeddy", "password": "StrongPassword123!"}

    first = client.post("/register", data=data)
    second = client.post("/register", data=data)

    assert first.status_code == 201
    assert second.status_code == 409


def test_password_is_hashed(client):
    client.post(
        "/register",
        data={"username": "jeddy", "password": "StrongPassword123!"}
    )

    with secure_app.get_db() as db:
        user = db.execute(
            "SELECT password_hash FROM users WHERE username = ?",
            ("jeddy",)
        ).fetchone()

    assert user is not None
    assert user["password_hash"] != "StrongPassword123!"


def test_sql_injection_input_is_treated_as_data(client):
    response = client.get(
        "/search",
        query_string={"username": "' OR '1'='1"}
    )

    assert response.status_code == 200
    assert b"jeddy" not in response.data


def test_xss_input_is_escaped(client):
    malicious_name = "<script>alert(1)</script>"

    client.post(
        "/register",
        data={
            "username": malicious_name,
            "password": "StrongPassword123!"
        }
    )

    response = client.get(
        "/search",
        query_string={"username": malicious_name}
    )

    assert response.status_code == 200
    assert b"<script>" not in response.data
    assert b"&lt;script&gt;" in response.data
