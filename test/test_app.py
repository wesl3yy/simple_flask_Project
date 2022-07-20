import pytest


DATA = [
    {"username": "admin", "password": "123"},
    {"username": "admin", "password": "1"},
]


def test_login(client):
    with client:
        for user in DATA:
            response_client = client.post("/", json=user)
            assert response_client.status_code == 200
            if user == {"username": "admin", "password": "123"}:
                assert user == {"username": "admin", "password": "123"}
            else:
                assert user == {"username": "admin", "password": "1"}
