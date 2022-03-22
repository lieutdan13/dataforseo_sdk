from unittest import TestCase
from unittest.mock import patch

from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory


class TestAPICredentialsFactory(TestCase):
    @patch("dataforseo_sdk.api_client.api_credentials_factory.os")
    def test_credentials_from_environment(self, mock_os):
        username = "api_username"
        password = "api_password"
        mock_os.environ = {"DFS_API_USERNAME": username, "DFS_API_PASSWORD": password}
        credentials = APICredentialsFactory.credentials_from_environment()

        assert credentials.username == username
        assert credentials.password == password

    @patch("dataforseo_sdk.api_client.api_credentials_factory.os")
    def test_credentials_from_environment__no_env_vars_raises_keyerror(self, mock_os):
        mock_os.environ = {}
        with self.assertRaises(KeyError):
            APICredentialsFactory.credentials_from_environment()

    @patch("dataforseo_sdk.api_client.api_credentials_factory.os")
    def test_credentials_from_environment__missing_username_raises_keyerror(
        self, mock_os
    ):
        mock_os.environ = {"DFS_API_USERNAME": "test"}
        with self.assertRaises(KeyError):
            APICredentialsFactory.credentials_from_environment()

    @patch("dataforseo_sdk.api_client.api_credentials_factory.os")
    def test_credentials_from_environment__missing_password_raises_keyerror(
        self, mock_os
    ):
        mock_os.environ = {"DFS_API_PASSWORD": "test"}
        with self.assertRaises(KeyError):
            APICredentialsFactory.credentials_from_environment()

    @patch("dataforseo_sdk.api_client.api_credentials_factory.Config")
    def test_credentials_from_config(self, mock_config):
        username = "api_username"
        password = "api_password"
        mock_config.config = {"api_username": username, "api_password": password}

        credentials = APICredentialsFactory.credentials_from_config()

        assert credentials.username == username
        assert credentials.password == password
