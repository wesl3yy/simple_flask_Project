from unittest import mock

import pytest

from login.login_blueprints import check_login

DATA = [
    ("case1:test1", {"username": "admin", "password": "123"}, {"isValid": "True"}, 200),
    ("case2:test2", {"username": "admin", "password": "1"}, {"isValid": "False"}, 200),
]


@pytest.mark.parametrize("case, data, return_value, expect", DATA)
def test_app(client, case, data, return_value, expect):
    mock.patch("login.login_blueprints.check_login", return_value=data).start()
    response = client.post("/", json=data, content_type="application/json")
    assert expect == response.status_code
