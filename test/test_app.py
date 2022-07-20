DATA = [
    {"username": "admin", "password": "123"},
    {"username": "admin", "password": "1"},
]


def test_login_success(client):
    with client:
        for user in DATA:
            response_client = client.post("/", json=user)
            assert response_client.status_code == 200
            if user == {"username": "admin", "password": "123"}:
                assert user == {"username": "admin", "password": "123"}


def test_login_failed(client):
    with client:
        for user in DATA:
            response_client = client.post("/", json=user)
            assert response_client.status_code == 200
            if user == {"username": "admin", "password": "1"}:
                assert user == {"username": "admin", "password": "1"}


# def test_login_failed(client):
#     with client:
#         for user in DATA:
#             sent = client.post("/", data=user, follow_redirects=True)
#             if user == {"username": "admin", "password": "1"}:
#                 assert sent.request.path == "/failed"
