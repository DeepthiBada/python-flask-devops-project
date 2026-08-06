import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../app")
    )
)

from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Welcome to the Python Flask DevOps Project!"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "UP"


def test_version():
    client = app.test_client()
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json["version"] == "1.0.0"
