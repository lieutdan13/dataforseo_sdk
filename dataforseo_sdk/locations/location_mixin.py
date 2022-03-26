from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory
from dataforseo_sdk.config import Config
from dataforseo_sdk.locations.location_service import LocationService


class LocationMixin:
    @property
    def __data_dir(self):
        if not getattr(self, "data_dir", None):
            self.data_dir = Config.config.get("data_dir")
        return self.data_dir

    @property
    def __credentials(self):
        if not getattr(self, "credentials", None):
            self.credentials = APICredentialsFactory.credentials_from_config()
        return self.credentials

    @property
    def locale(self):
        if not getattr(self, "_locale", None):
            self._locale = Config.config["locale"]
        return self._locale

    @property
    def _location_service(self):
        if not getattr(self, "__location_service", None):
            self.__location_service = LocationService(
                credentials=self.__credentials, data_dir=self.__data_dir
            )
        return self.__location_service

    @property
    def _location(self):
        if not getattr(self, "__location", None):
            self.__location = self._location_service.locales[self.locale]
        return self.__location

    @property
    def location_code(self):
        if not getattr(self, "_location_code", None):
            self._location_code, _, _ = self._location
        return self._location_code

    @property
    def language_code(self):
        if not getattr(self, "_language_code", None):
            _, self._language_code, _ = self._location
        return self._language_code

    @property
    def country_iso_code(self):
        if not getattr(self, "_country_iso_code", None):
            _, _, self._country_iso_code = self._location
        return self._country_iso_code
