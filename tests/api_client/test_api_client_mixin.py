import os
from unittest import TestCase
from unittest.mock import MagicMock, patch

from dataforseo_sdk.api_client.api_client_mixin import APIClientMixin
from dataforseo_sdk.api_client.api_credentials import APICredentials


class TestAPIClientMixin(TestCase):
    def setUp(self) -> None:
        self.username_from_env = "username_from_env"
        os.environ["DFS_API_USERNAME"] = self.username_from_env
        self.password_from_env = "p@ssword_fRom_3nv"
        os.environ["DFS_API_PASSWORD"] = self.password_from_env

    def tearDown(self) -> None:
        if "DFS_API_USERNAME" in os.environ:
            del os.environ["DFS_API_USERNAME"]
        if "DFS_API_PASSWORD" in os.environ:
            del os.environ["DFS_API_PASSWORD"]
        if "DFS_DATA_DIR" in os.environ:
            del os.environ["DFS_DATA_DIR"]

    def mock_location_service(self, mock_location_service):
        self.en_us_locale = "en_us"
        self.en_us_location_code = 2840
        self.en_us_language_code = "en"
        self.en_us_country_iso_code = "US"
        self.mock_location_service_instance = MagicMock()
        self.mock_location_service_instance.locales = {
            self.en_us_locale: (
                self.en_us_location_code,
                self.en_us_language_code,
                self.en_us_country_iso_code,
            )
        }
        mock_location_service.return_value = self.mock_location_service_instance

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

    def test_instantiate__without_credentials_uses_environment_variables(self):
        api_client_mixer = MockAPIClientMixer()

        assert api_client_mixer.credentials.username == self.username_from_env
        assert api_client_mixer.credentials.password == self.password_from_env

    @patch("dataforseo_sdk.api_client.api_client_mixin.LocationService")
    def test_instantiate__sets_locale(self, mock_location_service):
        self.mock_location_service(mock_location_service)

        api_client_mixer = MockAPIClientMixer()

        assert api_client_mixer.location_code == self.en_us_location_code
        assert api_client_mixer.language_code == self.en_us_language_code
        assert api_client_mixer.country_iso_code == self.en_us_country_iso_code

    def test_instantiate__with_data_dir(self):
        data_dir = "/tmp/path/to/data"

        api_client_mixer = MockAPIClientMixer(data_dir=data_dir)

        assert api_client_mixer.data_dir == data_dir


class MockAPIClientMixer(APIClientMixin):
    pass
