import os
from unittest import TestCase
from unittest.mock import MagicMock, patch

from dataforseo_sdk.api_client.api_client_mixin import APIClientMixin
from dataforseo_sdk.api_client.api_credentials import APICredentials


class TestAPIClientMixin(TestCase):
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

    @patch("dataforseo_sdk.api_client.api_client_mixin.LocationService")
    def test_instantiate__with_credentials(self, mock_location_service):
        self.mock_location_service(mock_location_service)
        credentials = MagicMock(spec=APICredentials)

        api_client_mixer = MockAPIClientMixer(credentials=credentials)

        assert api_client_mixer.credentials == credentials

    @patch("dataforseo_sdk.api_client.api_client_mixin.LocationService")
    def test_instantiate__with_username_and_password(self, mock_location_service):
        self.mock_location_service(mock_location_service)
        username = "username"
        password = "password"

        api_client_mixer = MockAPIClientMixer(username=username, password=password)

        assert api_client_mixer.credentials.username == username
        assert api_client_mixer.credentials.password == password

    @patch("dataforseo_sdk.api_client.api_credentials_factory.Config")
    @patch("dataforseo_sdk.api_client.api_client_mixin.LocationService")
    def test_instantiate__without_credentials_uses_from_config(
        self, mock_location_service, mock_config
    ):
        self.mock_location_service(mock_location_service)
        username = "username_from_config"
        password = "password_from_config"
        mock_config.config = {"api_username": username, "api_password": password}
        api_client_mixer = MockAPIClientMixer()

        assert api_client_mixer.credentials.username == username
        assert api_client_mixer.credentials.password == password

    @patch("dataforseo_sdk.api_client.api_credentials_factory.Config")
    @patch("dataforseo_sdk.api_client.api_client_mixin.LocationService")
    def test_instantiate__sets_locale(self, mock_location_service, mock_config):
        self.mock_location_service(mock_location_service)

        api_client_mixer = MockAPIClientMixer()

        assert api_client_mixer.location_code == self.en_us_location_code
        assert api_client_mixer.language_code == self.en_us_language_code
        assert api_client_mixer.country_iso_code == self.en_us_country_iso_code

    @patch("dataforseo_sdk.api_client.api_credentials_factory.Config")
    @patch("dataforseo_sdk.api_client.api_client_mixin.LocationService")
    def test_instantiate__with_data_dir(self, mock_location_service, mock_config):
        self.mock_location_service(mock_location_service)
        data_dir = "/tmp/path/to/data"

        api_client_mixer = MockAPIClientMixer(data_dir=data_dir)

        assert api_client_mixer.data_dir == data_dir


class MockAPIClientMixer(APIClientMixin):
    pass
