from dataforseo_sdk.api_client.api_client import APIClient
from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory
from dataforseo_sdk.config import Config
from dataforseo_sdk.locations.location_service import LocationService


class APIClientMixin:
    def __init__(self, *args, **kwargs):
        self._set_data_dir(kwargs.get("data_dir"))
        self._set_credentials(
            credentials=kwargs.get("credentials"),
            username=kwargs.get("username"),
            password=kwargs.get("password"),
        )
        self.client = APIClient(credentials=self.credentials)
        self._set_locale()

    def _set_credentials(self, credentials=None, username=None, password=None):
        if credentials:
            self.credentials = credentials
        elif username and password:
            self.credentials = (
                APICredentialsFactory.credentials_from_username_and_password(
                    username=username, password=password
                )
            )
        else:
            self.credentials = APICredentialsFactory.credentials_from_environment()

    def _set_locale(self):
        location_service = LocationService()
        self.locale = location_service.locales[Config.config["locale"]]
        self.location_code, self.language_code, self.country_iso_code = self.locale

    def _set_data_dir(self, data_dir=None):
        self.data_dir = data_dir or Config.config["data_dir"]
