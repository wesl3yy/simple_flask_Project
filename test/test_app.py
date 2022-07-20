DATA = [
    {"username": "admin", "password": "123"},
    {"username": "admin", "password": "1"},
]


def test_client(client):
    with client:
        response_client = client.get('/')
        assert response_client.status_code == 200


def test_login_success(client):
    with client:
        for user in DATA:
            sent = client.post("/", data=user, follow_redirects=True)
            if user == {"username": "admin", "password": "123"}:
                assert sent.request.path == "/success"


def test_login_failed(client):
    with client:
        for user in DATA:
            sent = client.post("/", data=user, follow_redirects=True)
            if user == {"username": "admin", "password": "1"}:
                assert sent.request.path == "/failed"
