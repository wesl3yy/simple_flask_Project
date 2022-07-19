import pytest
from app import app as test_flask



@pytest.fixture()
def client():
    return test_flask.test_client()
