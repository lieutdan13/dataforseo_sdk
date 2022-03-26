from unittest import TestCase
from unittest.mock import MagicMock, patch

from dataforseo_sdk.api_client.api_credentials import APICredentials
from dataforseo_sdk.locations.location_mixin import LocationMixin


class TestLocationMixin(TestCase):
    def setUp(self) -> None:
        self.en_us_locale = "en_us"
        self.en_us_location_code = 2840
        self.en_us_language_code = "en"
        self.en_us_country_iso_code = "US"
        self.mock_location_mixer = MockLocationMixer()
        self.mock_location_mixer.credentials = APICredentials(**self.api_credentials())
        return super().setUp()

    def api_credentials(self):
        return {"username": "api_username", "password": "api_password"}

    def mock_location_service(self, mock_location_service):
        self.mock_location_service_instance = MagicMock()
        self.mock_location_service_instance.locales = {
            self.en_us_locale: (
                self.en_us_location_code,
                self.en_us_language_code,
                self.en_us_country_iso_code,
            )
        }
        mock_location_service.return_value = self.mock_location_service_instance

    def test_locale__existing_locale(self):
        expected_locale = "en_ca"
        self.mock_location_mixer._locale = expected_locale

        assert self.mock_location_mixer.locale == expected_locale

    @patch("dataforseo_sdk.locations.location_mixin.Config")
    def test_locale(self, mock_config):
        expected_locale = "en_gb"
        mock_config.config = {"locale": expected_locale}

        assert self.mock_location_mixer.locale == expected_locale

    def test_location_code__existing(self):
        expected_location_code = self.en_us_location_code
        self.mock_location_mixer._location_code = expected_location_code

        assert self.mock_location_mixer.location_code == expected_location_code

    @patch("dataforseo_sdk.locations.location_mixin.Config")
    @patch("dataforseo_sdk.locations.location_mixin.LocationService")
    def test_location_code(self, mock_location_service, mock_config):
        mock_config.config = {"locale": self.en_us_locale}
        self.mock_location_service(mock_location_service)

        assert self.mock_location_mixer.location_code == self.en_us_location_code

    def test_language_code__existing(self):
        expected_language_code = self.en_us_language_code
        self.mock_location_mixer._language_code = expected_language_code

        assert self.mock_location_mixer.language_code == expected_language_code

    @patch("dataforseo_sdk.locations.location_mixin.Config")
    @patch("dataforseo_sdk.locations.location_mixin.LocationService")
    def test_language_code(self, mock_location_service, mock_config):
        mock_config.config = {"locale": self.en_us_locale}
        self.mock_location_service(mock_location_service)

        assert self.mock_location_mixer.language_code == self.en_us_language_code

    def test_country_iso_code__existing(self):
        expected_country_iso_code = self.en_us_country_iso_code
        self.mock_location_mixer._country_iso_code = expected_country_iso_code

        assert self.mock_location_mixer.country_iso_code == expected_country_iso_code

    @patch("dataforseo_sdk.locations.location_mixin.Config")
    @patch("dataforseo_sdk.locations.location_mixin.LocationService")
    def test_country_iso_code(self, mock_location_service, mock_config):
        mock_config.config = {"locale": self.en_us_locale}
        self.mock_location_service(mock_location_service)

        assert self.mock_location_mixer.country_iso_code == self.en_us_country_iso_code


class MockLocationMixer(LocationMixin):
    pass
