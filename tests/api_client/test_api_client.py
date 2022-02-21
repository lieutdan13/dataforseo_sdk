from unittest.mock import MagicMock, patch
from unittest import TestCase

from dataforseo_sdk.api_client.api_client import APIClient

LANGUAGES_AND_LOCATIONS_RESPONSE = """[
  {
    "location_code": 2012,
    "location_name": "Algeria",
    "location_code_parent": null,
    "country_iso_code": "DZ",
    "location_type": "Country",
    "available_languages": [
      {
        "available_sources": [
          "google"
        ],
        "language_name": "French",
        "language_code": "fr",
        "keywords": 16570680,
        "serps": 2013669
      }
    ]
  }
]"""


class TestAPIClient(TestCase):
    def setUp(self):
        username = "username"
        password = "password"
        self.creds = MockCreds(username, password)
        self.api_version = "v4"

    def test_client(self):
        api_client = APIClient(self.creds, api_version=self.api_version)

        assert api_client.credentials == self.creds
        assert api_client.api_version == self.api_version
        assert api_client.client.username == self.creds.username
        assert api_client.client.password == self.creds.password

    @patch("dataforseo_sdk.api_client.api_client.RestClient")
    def test_get(self, mock_rest_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get.return_value = LANGUAGES_AND_LOCATIONS_RESPONSE
        mock_rest_client.return_value = mock_client_instance

        api_client = APIClient(self.creds, api_version=self.api_version)
        endpoint = "dataforseo_labs/locations_and_languages"

        result = api_client.get(endpoint)

        mock_client_instance.get.assert_called_with(f"/{self.api_version}/{endpoint}")
        assert result == LANGUAGES_AND_LOCATIONS_RESPONSE


class MockCreds:
    def __init__(self, username, password):
        self.username = username
        self.password = password
