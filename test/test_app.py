import unittest

from flask import redirect, url_for

from app import app
app.testing = True

class AppTestCase(unittest.TestCase):
    def test_client(self):
        self.client = app.test_client()
        response_client = self.client.get("/")
        assert response_client.status_code == 200

    def test_login(self):
        self.client = app.test_client()
        sent = self.client.post('/',data={'username':'admin','password':'123'},follow_redirects=True)
        received = self.client.post('/success')
        assert sent == received

if __name__ == "__main__":
    unittest.main()