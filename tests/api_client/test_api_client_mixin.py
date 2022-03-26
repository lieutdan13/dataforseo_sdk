from unittest import TestCase
from unittest.mock import MagicMock, patch

from dataforseo_sdk.api_client.api_client_mixin import APIClientMixin
from dataforseo_sdk.api_client.api_credentials import APICredentials


class TestAPIClientMixin(TestCase):
    def test_instantiate__with_credentials(self):
        credentials = MagicMock(spec=APICredentials)

        api_client_mixer = MockAPIClientMixer(credentials=credentials)

        assert api_client_mixer.credentials == credentials

    def test_instantiate__with_username_and_password(self):
        username = "username"
        password = "password"

        api_client_mixer = MockAPIClientMixer(username=username, password=password)

        assert api_client_mixer.credentials.username == username
        assert api_client_mixer.credentials.password == password

    @patch("dataforseo_sdk.api_client.api_credentials_factory.Config")
    def test_instantiate__without_credentials_uses_from_config(self, mock_config):
        username = "username_from_config"
        password = "password_from_config"
        mock_config.config = {"api_username": username, "api_password": password}
        api_client_mixer = MockAPIClientMixer()

        assert api_client_mixer.credentials.username == username
        assert api_client_mixer.credentials.password == password

    @patch("dataforseo_sdk.api_client.api_credentials_factory.Config")
    def test_instantiate__with_data_dir(self, mock_config):
        data_dir = "/tmp/path/to/data"

        api_client_mixer = MockAPIClientMixer(data_dir=data_dir)

        assert api_client_mixer.data_dir == data_dir


class MockAPIClientMixer(APIClientMixin):
    pass
