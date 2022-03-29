from unittest import TestCase
from unittest.mock import MagicMock, patch

from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory


class TestAPICredentialsFactory(TestCase):
    def test_credentials_from_config__no_env_vars_raises_keyerror(self):
        with self.assertRaises(KeyError):
            APICredentialsFactory.credentials_from_config()

    @patch("dataforseo_sdk.api_client.api_credentials_factory.Config")
    def test_credentials_from_config(self, mock_config):
        username = "api_username"
        password = "api_password"
        mock_config.config = {"api_username": username, "api_password": password}

        credentials = APICredentialsFactory.credentials_from_config()

        assert credentials.username == username
        assert credentials.password == password

    def test_credentials_from_username_and_password(self):
        username = "api_username_from_args"
        password = "api_password_from_args"

        credentials = APICredentialsFactory.credentials_from_username_and_password(
            username=username, password=password
        )

        assert credentials.username == username
        assert credentials.password == password

    def test_credentials_from_all_credentials__use_credentials(self):
        expected_credentials = MagicMock()

        credentials = APICredentialsFactory.credentials_from_all_credentials(
            credentials=expected_credentials
        )

        assert credentials == expected_credentials

    def test_credentials_from_all_credentials__use_username_and_password(self):
        username = "username"
        password = "password"

        credentials = APICredentialsFactory.credentials_from_all_credentials(
            username=username, password=password
        )

        assert credentials.username == username
        assert credentials.password == password

    @patch("dataforseo_sdk.api_client.api_credentials_factory.Config")
    def test_credentials_from_all_credentials__missing_password_uses_config(
        self, mock_config
    ):
        username = "username"
        password = None
        config_username = "username_from_config"
        config_password = "password_from_config"

        mock_config.config = {
            "api_username": config_username,
            "api_password": config_password,
        }
        credentials = APICredentialsFactory.credentials_from_all_credentials(
            username=username, password=password
        )

        assert credentials.username == config_username
        assert credentials.password == config_password
