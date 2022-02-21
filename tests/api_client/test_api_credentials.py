from unittest import TestCase

from dataforseo_sdk.api_client.api_credentials import APICredentials

class TestAPICredentials(TestCase):

    def test_instantiate(self):
        username = "username"
        password = "password"

        api_creds = APICredentials(username=username, password=password)

        assert api_creds.username == username
        assert api_creds.password == password